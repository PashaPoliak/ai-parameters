import sys
import os

from task.constants import DEFAULT_MODEL, DEFAULT_SYSTEM_PROMPT, DIAL_ENDPOINT
from task.util import save_to_file_json_response
sys.path.insert(0, os.path.abspath('.'))

from task.app.client import DialClient
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

USER_MESSAGE = "Explain the key components of parameter top_p for LLM. Keep your response brief but informative."

def create_conversation(user_message):
    """
    Helper function to create a conversation with system and user messages
    """
    conversation = Conversation()
    conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
    conversation.add_message(Message(Role.USER, user_message))
    return conversation


def get_completion_with_params(client, conversation, **kwargs):
    """
    Helper function to call client.get_completion with common parameters
    """
    return client.get_completion(
        messages=conversation.get_messages(),
        print_request=False,
        print_only_content=True,
        temperature=0.7,
        **kwargs
    )


def run(top_p=1.0):
    """
    Run function that accepts top_p parameter for testing
    """
    client = DialClient(
        endpoint=DIAL_ENDPOINT,
        deployment_name=DEFAULT_MODEL,
    )
    
    conversation = create_conversation(USER_MESSAGE)
    result = get_completion_with_params(client, conversation, top_p=top_p)
    
    return result


def run_additional_parameters():
    """
    Additional task: Practice with other parameters from OpenAI and Anthropic.
    For instance OpenAI have `reasoning_effort` and Anthropic `thinking`, and there are many others like citations, etc...
    
    Note: The DIAL API supports standard OpenAI parameters. For provider-specific parameters,
    they might need to be passed differently depending on the implementation.
    """
        
    client = DialClient(
        endpoint=DIAL_ENDPOINT,
        deployment_name=DEFAULT_MODEL,
    )
    
    conversation1 = create_conversation(USER_MESSAGE)
    result1 = get_completion_with_params(client, conversation1, top_p=0.1)
    
    conversation2 = create_conversation(USER_MESSAGE)
    result2 = get_completion_with_params(client, conversation2, top_p=0.9)
    
    conversation3 = create_conversation(USER_MESSAGE)
    result3 = get_completion_with_params(client, conversation3)
    
    print("while higher top_p values allow for more diverse and creative responses.")
    
    return [
        {"response": result1.content if hasattr(result1, 'content') else result1},
        {"response": result2.content if hasattr(result2, 'content') else result2},
        {"response": result3.content if hasattr(result3, 'content') else result3}
    ]

if __name__ == "__main__":
    save_to_file_json_response(run_additional_parameters())
