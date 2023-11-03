"""
Liskov substitution:
    Subtypes must be substitutable for their base types.
"""


# Bad
class Bird:
    def do_bird_thing(self):
        print("I'm a bird")

    def fly(self):
        print("I am flying! Flap flap")


class Ostrich(Bird):
    def fly(self):
        pass
