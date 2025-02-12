class DoNothing:
    """Represents a cool change for pass keyword."""

    def __getattr__(self, _):
        return self

    def __call__(self, *args, **kwargs):
        pass


skip = DoNothing()


class Material:
    """Represents a parent class for materials."""

    material_density_values = {
        'Steel': 7700,
        'Concrete': 2500,
        'Brick': 2000,
        'Stone': 1600,
        'Wood': 600
    }

    def __init__(self, mass):
        self.mass = mass
        # works more dynamically
        self.density = Material.material_density_values[self.__class__.__name__]
        self.used = False

    @property
    def volume(self):
        return self.mass / self.density


class Brick(Material):
    """Represents a class for a brick."""

    skip


class Concrete(Material):
    """Represents a class for a concrete."""

    skip()


class Wood(Material):
    """Represents a class for a wood."""

    skip.skip


class Stone(Material):
    """Represents a class for a stone."""

    skip


class Steel(Material):
    """Represents a class for a steel."""

    skip


class Factory:
    """Represents a factory for creating materials and alloys."""

    _created_classes = {
        'Brick': Brick,
        'Concrete': Concrete,
        'Steel': Steel,
        'Wood': Wood,
        'Stone': Stone
    }
    _instances = []

    def __init__(self):
        self.created_materials = []
        self._instances.append(self)

    def __del__(self):
        if self in self._instances:
            self._instances.remove(self)

    def __create_materials_from_named(self, kwargs):
        return_tuple = ()
        for key, value in kwargs.items():
            if key not in self._created_classes:
                raise ValueError(f'Invalid material class name: {key}')

            material_class = self._created_classes[key]
            material = material_class(value)
            self._created_materials.add(material)  # add to a set
            self._all_created_materials.add(material)  # add to a set with all
            return_tuple += (material,)

        return return_tuple

    def __create_materials_from_positional(self, args):
        class_types = [type(obj).__name__ for obj in args]
        class_types = [cls for item in class_types for cls in item.split('_')]
        sorted_class_types = sorted(class_types)
        class_name = '_'.join(sorted_class_types)

        if class_name in self._created_classes:
            # mark all materials as used
            [setattr(material, 'used', True) for material in args]
            mass = sum(material.mass for material in args)
        else:
            density = 0
            for material in args:
                material.used = True
                density += Material.material_density_values[type(material).__name__]

            Material.material_density_values[str(class_name)] = density / len(args)  # set the class density
            new_material_class = type(str(class_name), (Material,), {})  # dynamic class
            self._created_classes[class_name] = new_material_class  # add a new class
            mass = sum(material.mass for material in args)

        return_material = self._created_classes[class_name](mass)
        self._created_materials.add(return_material)  # add to a set
        self._all_created_materials.add(return_material)  # add to a set with all
        return return_material

    def __call__(self, *args, **kwargs):
        if not args and not kwargs:
            raise ValueError('Factory cannot be called without arguments')
        if args and kwargs:
            raise ValueError('Factory cannot be called with both positional and named arguments')

        if args:  # positional
            if any(material.used for material in args):
                raise AssertionError('Cannot use already used material for alloy')

            return self.__create_materials_from_positional(args)

        if kwargs:  # named
            return self.__create_materials_from_named(kwargs)

    def can_build(self, quantity):
        volume = 0
        for material in self._created_materials:
            if material.used is False:
                volume += material.volume

        return volume >= quantity

    @staticmethod
    def can_build_together(quantity):
        volume = 0
        for material in Factory._all_created_materials:
            if not material.used:
                volume += material.volume

        return volume >= quantity