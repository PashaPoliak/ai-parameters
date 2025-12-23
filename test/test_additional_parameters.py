#!/usr/bin/env python
"""
Test for task/9-task-additional-parameters.py - top_p parameter
"""
import importlib.util
import pytest

spec = importlib.util.spec_from_file_location(
    "task_additional_parameters",
    "task/9-task-additional-parameters.py"
)
task_additional_parameters = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task_additional_parameters)

TOP_P_VALUES = [-1, 0.1, 1.0]

@pytest.mark.parametrize("top_p", TOP_P_VALUES)
def test_top_p_parameter(top_p):
    """Test the top_p parameter with different values"""
    try:
        response = task_additional_parameters.run(top_p=top_p)
        
        if top_p >= 0 and top_p <= 1:
            assert response is not None, "Response should not be None for valid top_p values"
            assert hasattr(response, 'content'), "Response should be a Message object with content"
            assert response.content is not None, "Response content should not be None"
            assert len(response.content.strip()) > 0, "Response content should not be empty"
        elif top_p < 0 or top_p > 1:
            pass

    except Exception as e:
        if top_p < 0 or top_p > 1:
            print(f"Expected error for invalid top_p value {top_p}: {str(e)}")
        else:
            raise e

if __name__ == "__main__":
    for top_p in TOP_P_VALUES:
        test_top_p_parameter(top_p)
