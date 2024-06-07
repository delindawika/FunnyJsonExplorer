import json
import argparse
from Container import Container
from Leaf import Leaf
from StyleFactory import TreeFactory,RectangleFactory
from IconFactory import PokerFaceFactory,MoonSunFactory

# Client Code
class FunnyJsonExplorer:
    def __init__(self, style, icon_family):
        self.container = None
        self.style = style
        self.icon_family = icon_family

    def _load(self, json_file):
        with open(json_file, 'r') as file:
            json_data = json.load(file)
        self.container = self.build_json_tree(json_data)

    def build_json_tree(self, json_data, level=0):
        container = Container("root", level=level)
        for key, value in json_data.items():
            if isinstance(value, dict):
                subcontainer = self.build_json_tree(value, level + 1)
                subcontainer.name = key
                container.add(subcontainer)
            else:
                leaf = Leaf(key, value)
                container.add(leaf)
        return container

    def show(self):

        if self.style == 'tree':
            self.factory = TreeFactory()
        elif self.style == 'rectangle':
            self.factory = RectangleFactory()

        style = self.factory.create_style()

        if self.icon_family == 'poker-face':
            self.icon=PokerFaceFactory()
        elif self.icon_family == 'moon-sun':
            self.icon=MoonSunFactory()


        branch=self.icon.create_branch()
        leaf=self.icon.create_leaf()
        self.container.apply_icon(branch,leaf)
        style.draw(self.container)


def main():
    parser = argparse.ArgumentParser(description="Funny JSON Explorer")
    parser.add_argument('-f', '--file', required=True, help="Path to the JSON file")
    parser.add_argument('-s', '--style', choices=['tree', 'rectangle'], default='tree', help="Visualization style")
    parser.add_argument('-i', '--icon', choices=['poker-face', 'moon-sun'], default='poker-face', help="Icon family for visualization")

    args = parser.parse_args()

    explorer = FunnyJsonExplorer(args.style, args.icon)
    explorer._load(args.file)
    explorer.show()

if __name__ == "__main__":
    main()

