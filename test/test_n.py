#!/usr/bin/env python

import os
import sys
import pytest
import importlib.util

sys.path.insert(0, os.path.abspath("."))

spec = importlib.util.spec_from_file_location(
    "task_2_n",
    "task/2-task-n.py"
)
task_2_n = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task_2_n)

run = task_2_n.run

MODELS_TO_TRY = [
    "gpt-4o",
    "claude-3-5-haiku@20241022",
    "gemini-2.0-flash",
]

N_VALUES = [1, 2, 3]

@pytest.mark.parametrize("model", MODELS_TO_TRY)
@pytest.mark.parametrize("n", N_VALUES)
def test_n_parameter(model, n):
    result = run(
        deployment_name=model,
        n=n,
        print_request=False,
        print_only_content=True,
    )

    assert result is not None
    assert isinstance(result, dict)

    assert result["model"] == model
    assert result["n"] == n

    assert "choices" in result
    assert isinstance(result["choices"], list)
    assert len(result["choices"]) == n

    for i, choice in enumerate(result["choices"]):
        assert choice["index"] == i
        assert "content" in choice
        assert isinstance(choice["content"], str)
