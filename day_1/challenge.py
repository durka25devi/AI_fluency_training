from workflow import workflow
from agent import agent


QUESTION = (
    "I can pay Rs. 30,000. "
    "Which two courses can I take together within this budget?"
)


print("=== CHALLENGE ===")
print("Q:", QUESTION)


print("\n--- WORKFLOW ---")

try:
    workflow_result = workflow(QUESTION)
    print(workflow_result)

except Exception as e:
    print("Workflow Error:", e)


print("\n--- AGENT ---")

try:
    agent_result = agent(QUESTION)
    print(agent_result)

except Exception as e:
    print("Agent Error:", e)