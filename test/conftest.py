def Param(param_list):
    """Parameterized decorator to run function with different parameters."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # For this implementation, we'll just return the function as-is
            # The actual parameterized execution would happen in the test framework
            return func(*args, **kwargs)
        wrapper.param_list = param_list
        return wrapper
    return decorator