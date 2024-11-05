class HauntedMansion:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value) # Calls bottom method/function

    def __getattr__(self, name):
        if not name.startswith("spooky_"):
            return "Booooo, only ghosts here!" # Not a valid attribute

        original_name = name[len("spooky_"):] # Get attribute names in dict after "spooky_"
        if f"spooky_{original_name}" in self.__dict__:
            return self.__dict__[f"spooky_{original_name}"] # Returns valid attribute

        return "Booooo, only ghosts here!" # Not a valid attribute

    def __setattr__(self, name, value):
        self.__dict__[f"spooky_{name}"] = value # Sets the attribute with prefix "spooky_"