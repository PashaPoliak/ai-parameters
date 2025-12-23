#!/usr/bin/env python
"""
Test for top_p parameter functionality in DIAL API
"""
import importlib.util
import sys
import os

sys.path.insert(0, os.path.abspath('.'))

from task.app.client import DialClient
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role
from task.constants import DEFAULT_MODEL, DEFAULT_SYSTEM_PROMPT, DIAL_ENDPOINT


def test_top_parameter():
    """Test the top_p parameter functionality"""
    try:
        client = DialClient(
            endpoint=DIAL_ENDPOINT,
            deployment_name=DEFAULT_MODEL,
        )
        
        conversation = Conversation()
        conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
        conversation.add_message(Message(Role.USER, "Explain what top_p parameter does in AI models. Be concise."))
        
        response_low = client.get_completion(
            messages=conversation.get_messages(),
            print_request=False,
            print_only_content=True,
            temperature=0.7,
            top_p=0.1
        )
        
        conversation = Conversation()
        conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
        conversation.add_message(Message(Role.USER, "Explain what top_p parameter does in AI models. Be concise."))
        
        response_high = client.get_completion(
            messages=conversation.get_messages(),
            print_request=False,
            print_only_content=True,
            temperature=0.7,
            top_p=0.9
        )
        
        conversation = Conversation()
        conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
        conversation.add_message(Message(Role.USER, "Explain what top_p parameter does in AI models. Be concise."))
        
        # Test with default top_p (1.0)
        print("\n--- Testing with default top_p (1.0) ---")
        response_default = client.get_completion(
            messages=conversation.get_messages(),
            print_request=False,
            print_only_content=True,
            temperature=0.7
        )
        
        if response_low and response_high and response_default:
            print("\nSUCCESS: All top_p parameter tests completed successfully")
            print("top_p=0.1: More focused responses")
            print("top_p=0.9: More diverse responses")
            print("top_p=1.0: Default behavior")
            
            return {
                'low_top_p': response_low,
                'high_top_p': response_high,
                'default_top_p': response_default
            }
        else:
            print("ERROR: One or more responses were not received properly")
            return False
            
    except Exception as e:
        print(f"ERROR: Error in top_p parameter test: {str(e)}")
        return False


def test_top_p_range():
    """Test different values in the valid top_p range"""
    print("\nTesting different top_p values in valid range (0.0 to 1.0)...")
    
    try:
        client = DialClient(
            endpoint=DIAL_ENDPOINT,
            deployment_name=DEFAULT_MODEL,
        )
        
        test_values = [0.1, 0.3, 0.5, 0.7, 0.9, 1.0]
        responses = {}
        
        for top_p_val in test_values:
            print(f"\n--- Testing with top_p={top_p_val} ---")
            conversation = Conversation()
            conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
            conversation.add_message(Message(Role.USER, f"Explain top_p parameter with value {top_p_val}. Be brief."))
            
            response = client.get_completion(
                messages=conversation.get_messages(),
                print_request=False,
                print_only_content=True,
                temperature=0.7,
                top_p=top_p_val
            )
            
            responses[top_p_val] = response
        
        print(f"\nSUCCESS: Tested {len(test_values)} different top_p values successfully")
        return responses
        
    except Exception as e:
        print(f"ERROR: Error in top_p range test: {str(e)}")
        return False


def test_top_p_with_temperature():
    """Test that top_p and temperature work together as expected (though not recommended)"""
    print("\nTesting top_p with temperature parameter interaction...")
    
    try:
        client = DialClient(
            endpoint=DIAL_ENDPOINT,
            deployment_name=DEFAULT_MODEL,
        )
        
        conversation = Conversation()
        conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
        conversation.add_message(Message(Role.USER, "What is the relationship between temperature and top_p?"))
        
        # Test with both parameters (not recommended but should work)
        response = client.get_completion(
            messages=conversation.get_messages(),
            print_request=False,
            print_only_content=True,
            temperature=0.5,
            top_p=0.8
        )
        
        if response:
            print("SUCCESS: top_p and temperature parameters work together")
            return True
        else:
            print("ERROR: Failed to get response with both parameters")
            return False
            
    except Exception as e:
        print(f"ERROR: Error in top_p and temperature interaction test: {str(e)}")
        return False


def run_all_top_p_tests():
    """Run all top_p parameter tests"""
    print("="*60)
    print("RUNNING TOP_P PARAMETER TESTS")
    print("="*60)
    
    results = []
    
    # Test basic top_p functionality
    result1 = test_top_p_parameter()
    results.append(("Basic top_p functionality", result1 is not False))
    
    # Test different values in range
    result2 = test_top_p_range()
    results.append(("top_p range values", result2 is not False))
    
    # Test interaction with temperature
    result3 = test_top_p_with_temperature()
    results.append(("top_p and temperature interaction", result3 is not False))
    
    # Summary
    print("\n" + "="*60)
    print("TOP_P TEST SUMMARY")
    print("="*60)
    
    passed = 0
    for test_name, test_result in results:
        status = "PASS" if test_result else "FAIL"
        print(f"{test_name}: {status}")
        if test_result:
            passed += 1
    
    print(f"\nPassed: {passed}/{len(results)} tests")
    
    if passed == len(results):
        print("All top_p parameter tests PASSED!")
        return True
    else:
        print("Some top_p parameter tests FAILED!")
        return False


if __name__ == "__main__":
    run_all_top_p_tests()
    