import re
import random


class Kid(type):
    """Represents a dynamic metaclass for kid with instance tracking."""

    _all_instances = {}

    def __new__(cls, name, bases, dict):
        """Create a new class type."""
        if '__call__' not in dict:
            raise NotImplementedError(f'Class {name} should implement __call__!')

        dict['instances'] = {}
        return type.__new__(cls, name, bases, dict)

    def __call__(cls, *args, **kwargs):
        """Create an instances and tracking them by their ID."""
        instance = super(Kid, cls).__call__(*args, **kwargs)
        instance_id = id(instance)
        instance.years = 0
        instance.id = instance_id
        instance.is_naughty = False

        for attr_name in dir(instance):
            if not attr_name.startswith('_'):  # Public methods
                attr = getattr(instance, attr_name)
                if callable(attr):
                    wrapped_method = Kid._wrap_method(attr, instance)
                    setattr(instance, attr_name, wrapped_method)

        cls.instances[instance_id] = instance
        Kid._all_instances[instance_id] = instance
        return instance

    @staticmethod
    def _wrap_method(method, instance):
        """Wrap a method to catch exceptions and mark the instance as naughty."""
        def wrapped(*args, **kwargs):
            try:
                return method(*args, **kwargs)
            except:
                instance.is_naughty = True
                raise

        return wrapped

    @classmethod
    def kids_grow(cls):
        """All kids grow with one passed year."""
        for kid_id, kid in Kid._all_instances.items():
            kid.years += 1

    @classmethod
    def gift_presents(cls, kids_requests, most_wanted):
        """Gift presents to all kids."""
        for kid_id, kid in Kid._all_instances.items():

            if kid.is_naughty:
                kid('coal')
                kid.is_naughty = False
                continue
            if kid.years > 5:
                Kid._all_instances.pop(kid_id)
                continue

            if kid_id in kids_requests:
                kid(kids_requests[kid_id])
            else:
                kid(most_wanted)


class Santa(object):
    """Represents an abstract Santa class."""

    def __new__(cls):
        """Create a new singleton instance of Santa."""
        if not hasattr(cls, '_instance'):
            cls._instance = super(Santa, cls).__new__(cls)

            cls._instance.kids_requests = {}
            cls._instance.wishlist = {}

        return cls._instance

    def __call__(self, kid, wish):
        """Kid calls for a Christmas present wish."""
        match = re.search(r'["\']([a-zA-Z0-9 ]+)["\']', wish)
        if match:
            gift = match.group(1)
            self.kids_requests[id(kid)] = gift
            self._add_gift_to_wishlist(gift)

    def __matmul__(self, letter):
        """Kid writes a letter with a Christmas present wish."""
        # id_match = re.search(r'^\s*\d+\s*$', letter)
        id_match = re.search(r'\s*(\d+)\s*', letter)
        gift_match = re.search(r'["\']([a-zA-Z0-9 ]+)["\']', letter)

        if gift_match and id_match:
            gift = gift_match.group(1)
            kid_id = int(id_match.group(0))

            self.kids_requests[kid_id] = gift
            self._add_gift_to_wishlist(gift)

    def __iter__(self):
        """Iterate over requests of kids."""
        return iter(self.kids_requests.values())

    def xmas(self):
        """Take presents to the kids method."""
        if self.kids_requests and self.wishlist:
            # max_key = max(self.wishlist, key=self.wishlist.get)
            max_key = Santa._get_most_wanted_present(self.wishlist)
            Kid.gift_presents(self.kids_requests, max_key)
            self.kids_requests.clear()
            self.wishlist.clear()

        Kid.kids_grow()

    def _add_gift_to_wishlist(self, gift):
        """Help method for adding to Santa's wishes."""
        if gift not in self.wishlist:
            self.wishlist[gift] = 1
        else:
            self.wishlist[gift] += 1

    @staticmethod
    def _get_most_wanted_present(wishlist):
        """Get random present wish of most wanted present."""
        max_value = max(wishlist.values())
        max_keys = [key for key, value in wishlist.items() if value == max_value]
        random_max_key = random.choice(max_keys)  # Chooses random from list with the same value

        return random_max_key