class LockPicker_6MI0600278:
    """Represents a lock picker and points checker."""

    def __init__(self, lock):
        self.lock = lock

    def unlock(self):
        try:
            self.lock.pick()
        except TypeError as ex:
            # In expected we know number of elements wanted

            args = [ None ] * ex.expected # Creates a list with the right number of arguments

        while True:
            try:
                self.lock.pick(args)
                break # No errors
            except TypeError as ex: # Wrong argument type
                args[ex.position] = ex.expected() # The type is callable and gives default type value
            except ValueError as ex: # Wrong value
                args[ex.position] = ex.expected # Sets the right value to a position
