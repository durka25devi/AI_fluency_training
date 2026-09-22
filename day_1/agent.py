import sys
import json

sys.stdout.reconfigure(encoding="utf-8")

from config import client, MODEL
from tools import TOOLS, get_course_fee, calculator


SYSTEM_PROMPT = """
You are a college fee assistant.

Rules:
1. Never guess a course fee. Always use get_course_fee.
2. Use calculator for arithmetic.
3. Available course codes: CS101, AI202, DS303.
4. If no tool is needed, answer directly.
"""


def agent(question, max_steps=6):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(1, max_steps + 1):

        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                tools=TOOLS,
                tool_choice="auto",
                temperature=0,
            )

        except Exception as e:
            error_message = str(e)

            if "getaddrinfo failed" in error_message:
                return (
                    "ERROR: Unable to connect to the Groq API. "
                    "Please check your internet connection, DNS settings, "
                    "and Groq API configuration."
                )

            if "Connection error" in error_message:
                return (
                    "ERROR: Could not connect to the LLM provider. "
                    "Please check your internet connection and API configuration."
                )

            return f"ERROR: {error_message}"

        message = response.choices[0].message

        # Normal answer without a tool
        if not message.tool_calls:
            return message.content

        # Add assistant tool request
        messages.append(message)

        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name

            # Handle malformed Groq tool names
            if "<|channel|>" in tool_name:
                tool_name = tool_name.split("<|channel|>")[0]

            try:
                args = json.loads(tool_call.function.arguments)
            except json.JSONDecodeError:
                result = "ERROR: Invalid tool arguments."
                print(
                    f" step {step}: {tool_name} -> {result}"
                )

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result,
                    }
                )
                continue

            # Execute get_course_fee
            if tool_name == "get_course_fee":

                try:
                    result = get_course_fee(**args)
                except Exception as e:
                    result = f"ERROR: {e}"

            # Execute calculator
            elif tool_name == "calculator":

                try:
                    result = calculator(**args)
                except Exception as e:
                    result = f"ERROR: {e}"

            else:
                result = f"ERROR: Unknown tool '{tool_name}'"

            print(
                f" step {step}: "
                f"{tool_name}({args}) -> {result}"
            )

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result),
                }
            )

    return "ERROR: Maximum number of agent steps reached."


if __name__ == "__main__":

    questions = [
        "What is the fee for AI202?",

        "What is the total fee for CS101 and AI202 "
        "after a 10% scholarship?",

        "Is DS303 more expensive than CS101, and by how much?",

        "Write a two-line welcome message for new AI students.",
    ]

    print(
        f"\n=== SYSTEM 3: AI AGENT | "
        f"provider: groq | model: {MODEL} ===\n"
    )

    for question in questions:

        print(f"Q: {question}")

        answer = agent(question)

        print("A:", answer)

        print("-" * 70)