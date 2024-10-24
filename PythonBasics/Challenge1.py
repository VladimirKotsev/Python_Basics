def type_check(arg_type):
    def decorator(*types):
        # types = tuple(...) => slow lookup speed ~O(n)
        def inner(func):
            def wrapper(*args, **kwargs):
                # Check input types
                if arg_type == 'in':
                    expected_types_str = ', '.join([str(t) for t in types])
                    # Check args
                    for arg in args:
                        if arg not in types: # slow
                            print(f'Invalid input arguments, expected {expected_types_str}!')
                            break

                    #Check kwargs
                    for key, value in kwargs.items():
                        if value not in types: # slow
                            print(f'Invalid input arguments, expected {expected_types_str}!')
                            break

                result = func(*args, **kwargs)

                # Check output type
                if arg_type == 'out':
                    expected_types_str = ', '.join([str(t) for t in types])
                    if not isinstance(result, types):
                        print(f'Invalid output value, expected {expected_types_str}!')

                return result

            return wrapper

        return inner

    return decorator
