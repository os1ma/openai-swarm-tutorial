from dotenv import load_dotenv
from swarm import Agent, Swarm
from swarm.repl import run_demo_loop

load_dotenv()

client = Swarm()


def transfer_to_agent_b():
    return agent_b


agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent.",
    functions=[transfer_to_agent_b],
)

agent_b = Agent(
    name="Agent B",
    instructions="Only speak in Haikus.",
)

run_demo_loop(agent_a, stream=True)
