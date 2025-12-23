from task.app.client import DialClient
from task.constants import DEFAULT_MODEL, DEFAULT_SYSTEM_PROMPT, DIAL_ENDPOINT
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

USER_MESSAGE = "What is token when we are working with LLM?"

def run(
        deployment_name: str,
        max_tokens: int = 0,
        print_request: bool = True,
        print_only_content: bool = False,
        **kwargs
) -> None:
    client = DialClient(
        endpoint=DIAL_ENDPOINT,
        deployment_name=deployment_name,
    )
    conversation = Conversation()
    conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
    conversation.add_message(Message(Role.USER, USER_MESSAGE))

    return client.get_completion(
        max_tokens=max_tokens,
        messages=conversation.get_messages(),
        print_request=print_request,
        print_only_content=print_only_content,
        **kwargs
    )

if __name__ == "__main__":
    response = run(deployment_name=DEFAULT_MODEL, max_tokens=1)
    print(f"Response: {response.content}")
    