import pytest
import importlib.util
import os

# Get the absolute path to the task file
task_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "task", "1-task-models.py")

spec = importlib.util.spec_from_file_location(
    "task_models",
    task_file_path
)
task_models = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task_models)

run = task_models.run

MODELS_TO_TRY = [
    "gpt-4o",
    "claude-3-5-haiku@20241022",
    "gemini-2.0-flash",
]

@pytest.mark.parametrize("model", MODELS_TO_TRY)
def test_model_response_contains_correct_model(model):
    result = run(
        deployment_name=model,
        print_request=False,
        print_only_content=True
    )

    assert result is not None
    assert isinstance(result, dict)
    assert "model" in result
    assert result["model"] == model
