from task.app.client import DialClient
from task.constants import DEFAULT_SYSTEM_PROMPT, DIAL_ENDPOINT
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

USER_MESSAGE = "Explain the key components of a Large Language Model architecture"

def run(
        deployment_name: str,
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
        messages=conversation.get_messages(),
        print_request=print_request,
        print_only_content=print_only_content,
        **kwargs
    )

if __name__ == "__main__":
        stop_seq = ["\n\n", "architecture"]
        response = run(
            deployment_name='gpt-4o',
            print_request=False,
            print_only_content=True,
            stop=stop_seq,
        )
        print(f"Response: {response.content}")