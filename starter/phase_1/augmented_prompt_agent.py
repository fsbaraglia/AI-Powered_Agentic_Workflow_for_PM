# TODO: 1 - Import the AugmentedPromptAgent class
from workflow_agents.base_agents import AugmentedPromptAgent
import os
from dotenv import load_dotenv
from openai import APIError

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

try:
    # TODO: 2 - Instantiate an object of AugmentedPromptAgent with the required parameters
    augmented_agent = AugmentedPromptAgent(openai_api_key, persona)

    # TODO: 3 - Send the 'prompt' to the agent and store the response in a variable named 'augmented_agent_response'
    augmented_agent_response = augmented_agent.respond(prompt)

    # Print the agent's response
    print(augmented_agent_response)

except ValueError as e:
    print(f"Configuration error: {e}")
except APIError as e:
    print(f"OpenAI API error: {e}")

# TODO: 4 - Add a comment explaining:
# - What knowledge the agent likely used to answer the prompt.
# - How the system prompt specifying the persona affected the agent's response.
# The agent used its own pre-trained knowledge to answer (Paris is the capital of France).
# The system prompt shaped the tone and format: the response begins with "Dear students,"
# because the persona instructed the LLM to behave as a college professor addressing a class.
