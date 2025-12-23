#!/usr/bin/env python
"""
Test script to verify all task implementations work correctly with different parameter data
"""
import os
import sys
import pytest

sys.path.insert(0, os.path.abspath('.'))

def run_task(task_path, description):
    """Run a single task implementation"""
    print(f"\n{'='*60}")
    print(f"Testing: {description}")
    print(f"File: {task_path}")
    print('='*60)
    
    try:
        with open(task_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        exec(content, {"__name__": "__main__"})
        print(f"SUCCESS: {description} completed successfully")
        return True
    except Exception as e:
        print(f"ERROR: Error in {description}: {str(e)}")
        return False

def test_all_tasks():
    """Test all task implementations"""
    print("Testing all task implementations with different parameter data...")
    
    tasks = [
        ("task/1-task-models.py", "Task 1 - Models"),
        ("task/2-task-n.py", "Task 2 - N Parameter"),
        ("task/3-task-temperature.py", "Task 3 - Temperature Parameter"),
        ("task/4-task-seed.py", "Task 4 - Seed Parameter"),
        ("task/5-task-max_tokens.py", "Task 5 - Max Tokens Parameter"),
        ("task/6-task-frequency_penalty.py", "Task 6 - Frequency Penalty Parameter"),
        ("task/7-task-presence_penalty.py", "Task 7 - Presence Penalty Parameter"),
        ("task/8-task-stop.py", "Task 8 - Stop Parameter"),
        ("task/9-task-additional-parameters.py", "Task 9 - Additional Parameters"),
    ]
    
    success_count = 0
    total_count = len(tasks)
    
    for task_path, description in tasks:
        if run_task(task_path, description):
            success_count += 1
    
    print(f"\n{'='*60}")
    print(f"Test Results: {success_count}/{total_count} tasks passed")
    print('='*60)
    
    assert success_count == total_count, f"{total_count - success_count} tasks failed"
    print("All implementations are working correctly!")

def main():
    """Main function to run tests as a script"""
    try:
        test_all_tasks()
        return True
    except AssertionError as e:
        print(str(e))
        return False

if __name__ == "__main__":
    main()