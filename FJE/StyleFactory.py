from Style import TreeStyle,RectangleStyle
# Abstract Factory
class StyleFactory:
    def create_style(self):
        pass
    
# Concrete Factories
class TreeFactory(StyleFactory):
    def create_style(self):
        return TreeStyle()

class RectangleFactory(StyleFactory):
    def create_style(self):
        return RectangleStyle()
