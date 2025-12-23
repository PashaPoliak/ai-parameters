#!/usr/bin/env python
"""
Test for task/3-task-temperature.py
"""
import pytest
import importlib.util
import os

task_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "task", "3-task-temperature.py")

spec = importlib.util.spec_from_file_location(
    "task_temperature",
    task_file_path
)
task_temperature = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task_temperature)

run = task_temperature.run

MODELS_TO_TRY = "gemini-2.0-flash"
USER_MESSAGE = "Describe the sound that the color purple makes when it's angry"
TEMPERATURE_VALUES = [0.0, 1.0, 2.0]

@pytest.mark.parametrize("temperature", TEMPERATURE_VALUES)
def test_temperature_parameter(temperature):
    """Test the temperature parameter with different values"""
    result = run(
        deployment_name=MODELS_TO_TRY,
        print_request=True,
        print_only_content=True,
        user_message=USER_MESSAGE,
        temperature=temperature
    )
    
    assert result is not None
    assert isinstance(result, dict)
    assert "model" in result
    assert "temperature" in result
    assert result["model"] == MODELS_TO_TRY
    assert result["temperature"] == temperature

if __name__ == "__main__":
    try:
        for temp in TEMPERATURE_VALUES:
            run(
                user_message=USER_MESSAGE,
                deployment_name=MODELS_TO_TRY,
                print_request=False,
                print_only_content=True,
                temperature=temp,
            )
        print("SUCCESS: Task 3 - Temperature Parameter completed successfully")
    except Exception as e:
        print(f"ERROR: Error in Task 3 - Temperature Parameter: {str(e)}")
