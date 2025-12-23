#!/usr/bin/env python
"""
Test for task/5-task-max_tokens.py
"""
import importlib.util
import pytest

spec = importlib.util.spec_from_file_location(
    "task_max_tokens",
    "task/5-task-max_tokens.py"
)
task_max_tokens = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task_max_tokens)

MAX_TOKENS_VALUES = [10, 50, 100, 200]

USER_MESSAGE = "What is token when we are working with LLM?"

run = task_max_tokens.run

@pytest.mark.parametrize("max_tokens", MAX_TOKENS_VALUES)
def test_max_tokens(max_tokens):
    try:
        response = task_max_tokens.run(
            deployment_name='gpt-4o',
            max_tokens=max_tokens,
            print_request=False,
            print_only_content=False,
        )
        
        assert response is not None, "Response should not be None"
        assert hasattr(response, 'content'), "Response should have content attribute"
        assert response.content is not None, "Response content should not be None"
        assert len(response.content.strip()) > 0, "Response content should not be empty"
        
    except Exception as e:
        print(f"ERROR: Error in Task 5 - Max Tokens Parameter: {str(e)}")
        raise e

if __name__ == "__main__":
    for max_tokens in MAX_TOKENS_VALUES:
        test_max_tokens(max_tokens)