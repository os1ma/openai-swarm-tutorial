import json

from dotenv import load_dotenv
from swarm import Agent, Swarm

load_dotenv()

client = Swarm()


def instructions(context_variables):
    user_name = context_variables["user_name"]
    return f"Help the user, {user_name}, do whatever they want."


agent = Agent(
    instructions=instructions,
)
response = client.run(
    agent=agent,
    messages=[{"role": "user", "content": "Hi!"}],
    context_variables={"user_name": "John"},
)

print(response)
print(json.dumps(response.messages, indent=2))
