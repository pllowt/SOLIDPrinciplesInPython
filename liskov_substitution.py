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
        print("I can't fly! I'm an ostrich!")


if __name__ == "__main__":
    sparrow = Bird()
    dave_the_ostrich = Ostrich()
    sparrow.fly()
    sparrow.do_bird_thing()
    dave_the_ostrich.fly()
    dave_the_ostrich.do_bird_thing()
