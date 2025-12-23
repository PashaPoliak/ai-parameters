from task.app.client import DialClient
from task.constants import DEFAULT_MODEL, DEFAULT_SYSTEM_PROMPT, DIAL_ENDPOINT
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

USER_MESSAGE = "Explain the water cycle in simple terms for children"

def run(
        deployment_name: str,
        print_request: bool = True,
        print_only_content: bool = False,
        user_message: str = None,
        **kwargs
) -> dict:
    client = DialClient(
        endpoint=DIAL_ENDPOINT,
        deployment_name=deployment_name,
    )
    conversation = Conversation()
    conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
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
        "frequency_penalty": kwargs.get("frequency_penalty")
    }

if __name__ == "__main__":
    response = run(
        deployment_name=DEFAULT_MODEL,
        user_message=USER_MESSAGE,
        print_request=False,
        print_only_content=True,
        frequency_penalty=0.0
        )
    print(f"Response: {response['content']}")
