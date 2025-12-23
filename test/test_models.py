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

def verify(ai_response):
    assert ai_response is not None, f"AI response is None"
    assert isinstance(ai_response, dict), f"AI response is not a dictionary"
    assert "content" in ai_response, f"AI response does not have content key"
    assert ai_response["content"] is not None, f"AI response content is None"
    assert isinstance(ai_response["content"], str), f"AI response content is not a string"
    assert len(ai_response["content"].strip()) > 0, f"AI response content is empty"
    assert "role" in ai_response, f"AI response does not have role key"
    assert ai_response["role"] == 'assistant' or ai_response["role"] == 'AI', f"AI response role is not correct"


def test_models():
    """
    Test function to run different models and display results.
    This separates the testing logic from the main execution block for better maintainability.
    """
    print("Starting model tests...")
    success_count = 0
    total_count = len(MODELS_TO_TRY)
    
    for model in MODELS_TO_TRY:
        try:
            print(f"\n--- Testing model: {model} ---")
            ai_response = run(
                deployment_name=model,
                print_request=False,
                print_only_content=True,
            )
            print(f"AI Response received successfully for model: {model}")
            success_count += 1
            verify(ai_response)
            
        except Exception as e:
            print(f"An error occurred during execution for model {model}: {str(e)}")
            continue
    
    print(f"\nTest Summary: {success_count}/{total_count} models tested successfully")
    assert success_count > 0, f"At least one model should work. {total_count - success_count} models failed."


if __name__ == "__main__":
    test_models()
