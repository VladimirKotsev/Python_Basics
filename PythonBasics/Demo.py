def get_count_unique_letters_for_keys(**kwargs):

    unique_letters = set()
    for key, value in kwargs.items():
        unique_letters.update(key)

    return len(unique_letters)

def function_that_says_ni(*args, **kwargs):

    cost = 0
    count = get_count_unique_letters_for_keys(**kwargs)
    #print(len(args))
    #print(len(kwargs))

    if len(args) == 0:
        #execute for named arguments
        for name, dict in kwargs.items():
            for key, value in dict.items():
                print(f'{key} -> {value}')
    else:
        #execute for one dictionary
        for arg in args:
            dictionary = dict(arg)
            if 'name' not in dictionary:
                return 'Ni'
            if dictionary['name'] != 'храст' and dictionary['name'] != 'bush' and dictionary['name'] != 'shrub':
                return 'Ni'
            if 'cost' in dictionary:
                if dictionary['cost'] > 42:
                    return 'Ni'
                else:
                    cost += dictionary['cost']
            if count % cost != 0:
                return 'Ni'



    return f'{cost:.2f}лв'

    # unique_letters = set()
    # for key, dicts in kwargs.items():
    #     #get bush cost
    #
    #     if 'cost' in dicts:
    #         if dicts['cost'] > 42:
    #             #bush too expensive
    #             return "Ni"
    #
    #     if 'name' not in dicts:
    #         #not a valid bush
    #         return 'Ni'
    #     else:
    #         if kwargs['name'] != 'храст' and kwargs['name'] != 'bush' and kwargs['name'] != 'shrub':
    #             #checks for a valid bush
    #             return 'Ni'
    #
    #     #get unique letter count
    #     unique_letters.add(key)
    #     count = len(unique_letters)
    #     print(count)
    #
    #     if count % cost != 0:
    #         return 'Ni'
    #     else:
    #         cost += dicts['cost']




print(function_that_says_ni(ab={"name": "храст", "cost": 1.80}, bc={"name": "храст", "cost": 1}, c ={"name": "не съм храст", "cost": 3}))


#print(function_that_says_ni({"name": "храст", "cost": 1}))
