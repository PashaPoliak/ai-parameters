#!/usr/bin/env python
"""
Test for task/7-task-presence_penalty.py
"""
import importlib.util
import pytest

spec = importlib.util.spec_from_file_location(
    "task_presence_penalty",
    "task/7-task-presence_penalty.py"
)
task_presence_penalty = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task_presence_penalty)

PRESENCE_PENALTY_VALUES = [-2.0, -1.0, 0.0, 1.0, 2.0]

@pytest.mark.parametrize("pres_penalty", PRESENCE_PENALTY_VALUES)
def test_presence_penalty(pres_penalty):
    try:
        print(f"--- Testing with presence_penalty: {pres_penalty} ---")
        response = task_presence_penalty.run(
            deployment_name='gpt-4o',
            print_request=False,
            print_only_content=True,
            presence_penalty=pres_penalty,
        )
        assert response is not None, "Response should not be None"
        assert hasattr(response, 'content'), "Response should have content attribute"
        assert response.content is not None, "Response content should not be None"
        assert len(response.content.strip()) > 0, "Response content should not be empty"
        
    except Exception as e:
        raise e

if __name__ == "__main__":
    for pres_penalty in PRESENCE_PENALTY_VALUES:
        test_presence_penalty(pres_penalty)