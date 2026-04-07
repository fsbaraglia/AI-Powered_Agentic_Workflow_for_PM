# TODO: 1 - Import the KnowledgeAugmentedPromptAgent and RoutingAgent
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent, RoutingAgent
import os
from dotenv import load_dotenv
from openai import APIError

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

try:
    persona = "You are a college professor"

    # TODO: 2 - Define the Texas Knowledge Augmented Prompt Agent
    knowledge = "You know everything about Texas"
    texas_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

    # TODO: 3 - Define the Europe Knowledge Augmented Prompt Agent
    knowledge = "You know everything about Europe"
    europe_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

    # TODO: 4 - Define the Math Knowledge Augmented Prompt Agent
    persona = "You are a college math professor"
    knowledge = "You know everything about math, you take prompts with numbers, extract math formulas, and show the answer without explanation"
    math_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

    agents = [
        {
            "name": "texas agent",
            "description": "Answer a question about Texas",
            # TODO: 5 - Call the Texas Agent to respond to prompts
            "func": lambda x: texas_agent.respond(x)
        },
        {
            "name": "europe agent",
            "description": "Answer a question about Europe",
            # TODO: 6 - Define a function to call the Europe Agent
            "func": lambda x: europe_agent.respond(x)
        },
        {
            "name": "math agent",
            "description": "When a prompt contains numbers, respond with a math formula",
            # TODO: 7 - Define a function to call the Math Agent
            "func": lambda x: math_agent.respond(x)
        }
    ]

    routing_agent = RoutingAgent(openai_api_key, agents)

    # TODO: 8 - Print the RoutingAgent responses to the following prompts:
    #           - "Tell me about the history of Rome, Texas"
    #           - "Tell me about the history of Rome, Italy"
    #           - "One story takes 2 days, and there are 20 stories"
    print(routing_agent.route("Tell me about the history of Rome, Texas"))
    print(routing_agent.route("Tell me about the history of Rome, Italy"))
    print(routing_agent.route("One story takes 2 days, and there are 20 stories"))

except ValueError as e:
    print(f"Configuration error: {e}")
except APIError as e:
    print(f"OpenAI API error: {e}")
