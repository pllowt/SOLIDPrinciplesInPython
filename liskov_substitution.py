# Bad
class Bird:
    def fly(self):
        pass


class Ostrich(Bird):
    pass


# Good
class Bird:
    pass


class FlyingBird(Bird):
    def fly(self):
        pass


class Ostrich(Bird):
    pass
