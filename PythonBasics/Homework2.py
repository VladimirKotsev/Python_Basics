def get_count_unique_letters_for_keys(**kwargs):

    unique_letters = set()
    for key, value in kwargs.items():
        unique_letters.update(key)

    return len(unique_letters)

def function_that_says_ni(*args, **kwargs):

    cost = 0
    count = get_count_unique_letters_for_keys(**kwargs)
    print(len(args))
    print(len(kwargs))

    if len(args) == 0:
        #execute for named arguments

        for key, value in args:
            print(f'{key} -> {value}')
    else:
        #execute for one dictionary
        for key in args:
            print(f'{key} -> {args[key]}')


function_that_says_ni(ab={"name": "храст", "cost": 1.80}, bc={"name": "храст", "cost": 1}, c ={"name": "не съм храст", "cost": 3})
