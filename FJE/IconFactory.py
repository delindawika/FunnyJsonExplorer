class IconFactory:
    def create_branch(self):
        pass
    def create_leaf(self):
        pass

class PokerFaceFactory(IconFactory):
    def create_branch(self):
        return ('♢')
    def create_leaf(self):
        return ('♤')

class MoonSunFactory(IconFactory):
    def create_branch(self): 
        return ('☾')
    def create_leaf(self):
        return ('☼')
