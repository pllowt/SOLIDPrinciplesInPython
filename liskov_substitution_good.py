
# Good
class Bird:
    def do_bird_thing(self):
        print("I'm a bird")


class FlyingBird(Bird):
    def fly(self):
        print("I am flying! Flap flap")

class NonFlyingBird(Bird):
    pass

class Ostrich(NonFlyingBird):
    pass
