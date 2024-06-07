# Component Classes
class Leaf:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.icon = None

    def draw(self):
        value_display = f": {self.value}" if self.value else ""
        print(f"  {self.icon} {self.name}{value_display}")