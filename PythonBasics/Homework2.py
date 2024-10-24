def get_count_unique_letters_for_keys(**kwargs):

    unique_letters = set()
    for key, value in kwargs.items():
        unique_letters.update(key)

    return len(unique_letters)

valid_bush_names = ['храст', 'bush', 'shrub']

def function_that_says_ni(*args, **kwargs):
    cost = 0
    has_named = False

    # execute for kwargs(named)
    count = get_count_unique_letters_for_keys(**kwargs)

    for name, dictionary in kwargs.items():
        if 'name' in dictionary and dictionary.get('name').lower() in valid_bush_names: #Good bush
            cost += dictionary.get('cost', 0)
            has_named = True

    # execute for args(positional)
    for arg in args:
        if type(arg) is not dict:
            continue

        dictionary = dict(arg)

        if 'name' in dictionary and dictionary['name'].lower() in valid_bush_names:
            cost += dictionary.get('cost', 0)

    if cost == 0 or cost > 42:
        return 'Ni!'
    if has_named and count % (cost // 1) != 0:
        return 'Ni!'

    return f'{cost:.2f}лв'

