#!/usr/bin/env python
"""
Test for task/6-task-frequency_penalty.py
"""
import importlib.util
import pytest

spec = importlib.util.spec_from_file_location(
    "task_frequency_penalty",
    "task/6-task-frequency_penalty.py"
)
task_frequency_penalty = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task_frequency_penalty)

FREQUENCY_PENALTY_VALUES = [-2.0, -1.0, 0.0, 1.0, 2.0]

@pytest.mark.parametrize("freq_penalty", FREQUENCY_PENALTY_VALUES)
def test_frequency_penalty(freq_penalty):
    try:
        print(f"--- Testing with frequency_penalty: {freq_penalty} ---")
        response = task_frequency_penalty.run(
            deployment_name='gpt-4o',
            user_message="Test message for frequency penalty",
            print_request=False,
            print_only_content=True,
            frequency_penalty=freq_penalty,
        )
        assert response is not None, "Response should not be None"
        assert isinstance(response, dict), "Response should be a dictionary"
        assert 'content' in response, "Response should have content key"
        assert response['content'] is not None, "Response content should not be None"
        assert len(response['content'].strip()) > 0, "Response content should not be empty"
        
    except Exception as e:
        raise e    

if __name__ == "__main__":
    for freq_penalty in FREQUENCY_PENALTY_VALUES:
        test_frequency_penalty(freq_penalty)
    