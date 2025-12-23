from task.app.client import DialClient
from task.constants import DEFAULT_MODEL, DEFAULT_SYSTEM_PROMPT, DIAL_ENDPOINT
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

USER_MESSAGE = "Describe the sound that the color purple makes when it's angry"

def run(
        deployment_name: str,
        print_request: bool = True,
        print_only_content: bool = False,
        message: str = None,
        user_message: str = None,
        **kwargs
) -> dict:
    client = DialClient(endpoint=DIAL_ENDPOINT, deployment_name=deployment_name)
    conversation = Conversation()
    conversation.add_message(Message(Role.SYSTEM, message or DEFAULT_SYSTEM_PROMPT))
    conversation.add_message(Message(Role.USER, user_message or USER_MESSAGE))

    ai_message = client.get_completion(
        messages=conversation.get_messages(),
        print_request=print_request,
        print_only_content=print_only_content,
        **kwargs
    )
    
    return {
        "model": deployment_name,
        "content": ai_message.content,
        "temperature": kwargs.get("temperature")
    }

if __name__ == "__main__":
    try:
        response = run(deployment_name=DEFAULT_MODEL)
        print(f"    Response: {response['content']}")
    except Exception as e:
        print(f"    Failed to run model {DEFAULT_MODEL}: {e}")
