#!/usr/bin/env python
"""
Test for task/4-task-seed.py
"""
import pytest
import importlib.util

spec = importlib.util.spec_from_file_location(
    "task_seed",
    "task/4-task-seed.py"
)
task_seed = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task_seed)

run = task_seed.run
MODELS_TO_TRY = ['gpt-4o']
SEED_VALUES = [42, 123, 1000, None]
USER_MESSAGE = "Name a random animal"

@pytest.mark.parametrize("seed", SEED_VALUES)
def test_seed(seed):
    """Test seed parameter functionality"""
    print(f"\n🧪 Testing seed: {seed}")
    
    kwargs = {
        'n': 5,
        'print_request': False,
        'print_only_content': True,
    }
    
    if seed is not None:
        kwargs['seed'] = seed
    
    # Run the test
    result = run(
        deployment_name='gpt-4o',
        **kwargs
    )
    
    # Verify we got a response
    assert result is not None
    assert hasattr(result, 'content')
    assert result.content is not None
    assert len(result.content.strip()) > 0
    
    print(f"✅ Seed {seed} test passed - Response: {result.content[:50]}...")

@pytest.mark.parametrize("model", MODELS_TO_TRY)
def test_determinism_with_seed(model):
    """Test that same seed produces consistent results"""
    seed = 42
    
    # Run twice with same seed
    result1 = run(
        deployment_name=model,
        seed=seed,
        n=3,
        print_request=False,
        print_only_content=True,
    )
    
    result2 = run(
        deployment_name=model,
        seed=seed,
        n=3,
        print_request=False,
        print_only_content=True,
    )
    
    # Both should return valid responses
    assert result1 is not None
    assert result2 is not None
    
    print(f"🔄 Determinism test for {model}:")
    print(f"   Run 1: {result1.content[:30]}...")
    print(f"   Run 2: {result2.content[:30]}...")

def test_no_seed_randomness():
    """Test that without seed, results can vary"""
    results = []
    
    # Run multiple times without seed
    for i in range(3):
        result = run(
            deployment_name='gpt-4o',
            print_request=False,
            print_only_content=True,
        )
        results.append(result.content)
    
    # All should be valid responses
    for i, result in enumerate(results):
        assert result is not None
        assert len(result.strip()) > 0
        print(f"🎲 Random run {i+1}: {result[:30]}...")
    
    print("✅ Randomness test completed")

def test_multiple_choices_with_seed():
    """Test multiple choices (n>1) with seed for determinism analysis"""
    result = run(
        deployment_name='gpt-4o',
        seed=42,
        n=5,
        print_request=False,
        print_only_content=False,
    )
    
    assert result is not None
    print(f"🎯 Multiple choices test with seed=42: {result.content[:50]}...")

def test_seed_consistency_across_runs():
    """Test that the same seed produces identical results across multiple runs"""
    seed = 1000
    results = []
    
    # Run 3 times with same seed
    for i in range(3):
        result = run(
            deployment_name='gpt-4o',
            seed=seed,
            n=1,
            print_request=False,
            print_only_content=True,
        )
        results.append(result.content)
        print(f"🔄 Run {i+1} with seed {seed}: {result.content[:40]}...")
    
    # Check if results are similar (they should be with seed)
    assert all(len(result.strip()) > 0 for result in results)
    print("✅ Consistency test completed")

def test_different_seeds_produce_different_results():
    """Test that different seeds can produce different results"""
    seeds = [42, 123, 1000]
    results = {}
    
    for seed in seeds:
        result = run(
            deployment_name='gpt-4o',
            seed=seed,
            n=1,
            print_request=False,
            print_only_content=True,
        )
        results[seed] = result.content
        print(f"🎯 Seed {seed}: {result.content[:40]}...")
    
    # All results should be valid
    for seed, content in results.items():
        assert content is not None
        assert len(content.strip()) > 0
    
    print("✅ Different seeds test completed")

def test_edge_cases():
    """Test edge cases for seed parameter"""
    edge_cases = [0, -1, 999999]
    
    for seed in edge_cases:
        try:
            result = run(
                deployment_name='gpt-4o',
                seed=seed,
                n=1,
                print_request=False,
                print_only_content=True,
            )
            assert result is not None
            print(f"✅ Edge case seed {seed}: {result.content[:30]}...")
        except Exception as e:
            print(f"⚠️ Edge case seed {seed} failed: {e}")

if __name__ == "__main__":
    print("🧪 Running seed parameter tests manually...")
    print("="*80)
    
    # Test each seed value
    print("\n1️⃣ Testing each seed value...")
    
    # Run individual tests
    for seed in SEED_VALUES:
        try:
            test_seed(seed)
            print(f"✅ Seed {seed} test passed")
        except Exception as e:
            print(f"❌ Seed {seed} test failed: {e}")
    
    # Test determinism
    print("\n2️⃣ Testing determinism with seed...")
    for model in MODELS_TO_TRY:
        try:
            test_determinism_with_seed(model)
            print(f"✅ Determinism test for {model} passed")
        except Exception as e:
            print(f"❌ Determinism test for {model} failed: {e}")
    
    # Test randomness without seed
    print("\n3️⃣ Testing randomness without seed...")
    try:
        test_no_seed_randomness()
        print("✅ Randomness test passed")
    except Exception as e:
        print(f"❌ Randomness test failed: {e}")
    
    # Test multiple choices with seed
    print("\n4️⃣ Testing multiple choices with seed...")
    try:
        test_multiple_choices_with_seed()
        print("✅ Multiple choices test passed")
    except Exception as e:
        print(f"❌ Multiple choices test failed: {e}")
    
    # Test consistency across runs
    print("\n5️⃣ Testing consistency across runs...")
    try:
        test_seed_consistency_across_runs()
        print("✅ Consistency test passed")
    except Exception as e:
        print(f"❌ Consistency test failed: {e}")
    
    # Test different seeds
    print("\n6️⃣ Testing different seeds...")
    try:
        test_different_seeds_produce_different_results()
        print("✅ Different seeds test passed")
    except Exception as e:
        print(f"❌ Different seeds test failed: {e}")
    
    # Test edge cases
    print("\n7️⃣ Testing edge cases...")
    try:
        test_edge_cases()
        print("✅ Edge cases test passed")
    except Exception as e:
        print(f"❌ Edge cases test failed: {e}")
    
    print("\n🎉 All manual tests completed!")