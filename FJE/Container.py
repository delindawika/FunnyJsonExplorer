class Container:
    def __init__(self, name, icon=None, level=0):
        self.name = name
        self.icon = icon
        self.level = level
        self.children = []

    def add(self, component):
        self.children.append(component)

    def draw(self):
        icon_display = f"{self.icon} " if self.icon else ""
        indent = "  " * self.level
        print(f"{indent}{icon_display}{self.name}")
        for child in self.children:
            child.draw()

    def apply_icon(self, container_icon, leaf_icon):
        if self.icon is None:
            self.icon = container_icon
        for child in self.children:
            if isinstance(child, Container):
                child.apply_icon(container_icon, leaf_icon)
            else:
                child.icon = leaf_icon
