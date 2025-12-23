#!/usr/bin/env python
"""
Test for task/8-task-stop.py
"""
import importlib.util
import pytest

spec = importlib.util.spec_from_file_location(
    "task_stop",
    "task/8-task-stop.py"
)
task_stop = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task_stop)

run = task_stop.run

MODELS_TO_TRY = ['gpt-4o']
STOP_SEQUENCES = ["\n\n", ".", "LLM", ["\n\n", "architecture"]]

@pytest.mark.parametrize("stop_seq", STOP_SEQUENCES)
def test_stop(stop_seq):
    try:
        print(f"--- Testing with stop sequence: {repr(stop_seq)} ---")
        result = task_stop.run(
            deployment_name=MODELS_TO_TRY[0],
            print_request=False,
            print_only_content=True,
            stop=stop_seq,
        )
        assert result is not None, f"Result should not be None for stop sequence: {repr(stop_seq)}"
        assert hasattr(result, 'content') or isinstance(result, str), f"Result should have content for stop sequence: {repr(stop_seq)}"        
        result_content = getattr(result, 'content', result) if hasattr(result, '__dict__') else str(result)
        print(f"Success with stop sequence: {repr(stop_seq)}, result length: {len(result_content) if result_content else 0}")
    except Exception as e:
        print(f"ERROR: Error in Task 8 - Stop Parameter with stop_seq {repr(stop_seq)}: {str(e)}")
        raise


if __name__ == "__main__":
    for stop_seq in STOP_SEQUENCES:
        test_stop(stop_seq)