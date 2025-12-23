import sys
import os

# Only add to path if __file__ is defined (when run as a script)
if '__file__' in globals():
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
else:
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath('.'))))

from task.app.client import DialClient
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role
from task.constants import DEFAULT_SYSTEM_PROMPT, DIAL_ENDPOINT, DEFAULT_MODEL

USER_MESSAGE = "What LLMs can do?"

def run(
        deployment_name: str = None,
        message: str = USER_MESSAGE,
        print_request: bool = True,
        print_only_content: bool = False,
        **kwargs
) -> dict:
    if deployment_name is not None and not isinstance(deployment_name, str):
        raise TypeError("deployment_name must be a string or None")
    
    model_name = deployment_name or DEFAULT_MODEL
    
    client = DialClient(endpoint=DIAL_ENDPOINT, deployment_name=model_name)

    conversation = Conversation()
    conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
    conversation.add_message(Message(Role.USER, message or USER_MESSAGE))

    try:
        ai_message = client.get_completion(
            messages=conversation.get_messages(),
            print_request=print_request,
            print_only_content=print_only_content,
            **kwargs
        )
        return {
            "model": model_name,
            "content": ai_message.content,
            "role": ai_message.role.value
        }
    except Exception as e:
        print(f"Error occurred while getting AI completion: {str(e)}")
        raise

if __name__ == "__main__":
    model = DEFAULT_MODEL
    print(f"Running model: {model}")
    try:
        response = run(deployment_name=model, message=USER_MESSAGE)
        print(f"Response from {model}: {response}")
    except Exception as e:
        print(f"Failed to run model {model}: {e}")

# The main goal of this task is to explore the functional capabilities of DIAL to be able to work with different
# LLMs through unified API
