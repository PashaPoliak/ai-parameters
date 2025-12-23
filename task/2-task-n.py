import json
import os
import requests
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role
from task.constants import API_KEY, DEFAULT_MODEL, DEFAULT_SYSTEM_PROMPT, DIAL_ENDPOINT

USER_MESSAGE = "Why is the snow white?"

def run(
    deployment_name: str,
    print_request: bool = True,
    print_only_content: bool = False,
    **kwargs
):
    endpoint = DIAL_ENDPOINT.format(model=deployment_name)
    
    conversation = Conversation()
    conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
    conversation.add_message(Message(Role.USER, USER_MESSAGE))

    request_data = {
        "messages": [msg.to_dict() for msg in conversation.get_messages()],
        **kwargs,
    }
    headers = {
        "api-key": API_KEY,
        "Content-Type": "application/json"
    }
    
    response = requests.post(url=endpoint, headers=headers, json=request_data, timeout=60)

    if response.status_code == 200:
        data = response.json()
        choices = data.get("choices", [])
        
        if choices:
            n = kwargs.get("n", 1)
            
            print("\n" + "="*50 + " RESPONSE " + "="*50)
            if print_only_content:
                for choice in choices:
                    content = choice.get("message", {}).get("content", "")
                    print(content)
            else:
                print(json.dumps(data, indent=2, sort_keys=True))
            print("="*108)
            
            messages = []
            for choice in choices:
                content = choice.get("message", {}).get("content", "")
                messages.append(Message(Role.AI, content))
            
            return {
                "model": deployment_name,
                "n": n,
                "choices": [
                    {
                        "index": i,
                        "role": msg.role.value,
                        "content": msg.content
                    }
                    for i, msg in enumerate(messages)
                ]
            }
        raise ValueError("No Choice has been present in the response")
    else:
        raise Exception(f"HTTP {response.status_code}: {response.text}")

if __name__ == "__main__":
    model = DEFAULT_MODEL
    print(f"Running model: {model}")
    try:
        response =  run(
            deployment_name=model,
            n=2,
            print_request=True,
            print_only_content=False,
        )
        print(f"Response from {model}: {response}")
    except Exception as e:
        print(f"Failed to run model {model}: {e}")
