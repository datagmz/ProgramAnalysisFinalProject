import json
import os

from logger_config import log
from config import Config

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + "/local.config.json") as f:
    config_data = json.load(f)

try:
    config = Config(**config_data)
except ValueError as e:
    log.error("%s", e)
    exit(1)

API_KEY = config.AZURE_OPENAI_KEY
API_ENDPOINT = config.AZURE_OPENAI_ENDPOINT
DEPLOYMENT_NAME = config.AZURE_OPENAI_DEPLOYMENT_NAME

import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
import semantic_kernel.utils.logging as sk_logging
from semantic_kernel.contents.chat_history import ChatHistory

import asyncio

async def main():
    kernel = sk.Kernel()

    chat_completion = AzureChatCompletion(
        api_key=API_KEY,
        endpoint=API_ENDPOINT,
        deployment_name=DEPLOYMENT_NAME
        )
    kernel.add_service(chat_completion)

    # Add chat history
    history = ChatHistory()

    # Start the chat loop
    print("Welcome to the Azure OpenAI Chat! Type 'exit' or 'quit' to end the session.\n")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Add user input to chat history
        history.add_user_message(user_input)

        # Generate AI response
        output = await chat_completion.get_chat_message_content(
            chat_history=history,
            settings=chat_completion.instantiate_prompt_execution_settings(),
            kernel=kernel
            )

        print("AI:", output)

if __name__ == "__main__":
    asyncio.run(main())





