from Container import Container
class Style:
    def draw(self, container):
        pass

# Concrete Products for Styles
class TreeStyle(Style):
    def draw(self, container):
        for i, child in enumerate(container.children):
            is_last_child = (i == len(container.children) - 1)
            if isinstance(child, Container):
                self._draw_tree(child, "", is_last_child)
            else:
                leaf_branch = "└─" if is_last_child else "├─"
                value_display = f": {child.value}" if child.value else ""
                print(f"{leaf_branch}{child.icon} {child.name}{value_display}")

    def _draw_tree(self, container, indent, is_last):
        icon_display = f"{container.icon} " if container.icon else ""
        branch = "└─" if is_last else "├─"
        print(f"{indent}{branch}{icon_display}{container.name}")
        indent += "  " if is_last else "│ "
        for i, child in enumerate(container.children):
            is_last_child = (i == len(container.children) - 1)
            if isinstance(child, Container):
                self._draw_tree(child, indent, is_last_child)
            else:
                leaf_branch = "└─" if is_last_child else "├─"
                value_display = f": {child.value}" if child.value else ""
                print(f"{indent}{leaf_branch}{child.icon} {child.name}{value_display}")


class RectangleStyle(Style):
    def draw(self, container):
        lines = []
        self._build_lines(container, lines, "", True)
        self._print_lines(lines)

    def _build_lines(self, container, lines, indent, is_last_child):
        for i, child in enumerate(container.children):
            is_last_child = (i == len(container.children) - 1)
            if isinstance(child, Container):
                if indent == "":
                    lines.append(f"┌─ {child.icon}{child.name} {'─' * (43 - len(child.icon) - len(child.name))}┐")
                else:
                    lines.append(f"{indent}├─{child.icon}{child.name} {'─' * (48 - len(indent) - 4 - len(child.icon) - len(child.name))}┤")
                
                new_indent = indent + "│  " 
                self._build_lines(child, lines, new_indent, is_last_child)
            else:
                leaf_branch = "└─" if is_last_child else "├─"
                value_display = f": {child.value}" if child.value else ""
                lines.append(f"{indent}{leaf_branch}{child.icon}{child.name}{value_display} {'─' * (47 - len(indent) - len(leaf_branch) - len(child.icon) - len(child.name) - len(value_display) - 1)}┤")


    def _print_lines(self, lines):
        for line in lines:
            print(line)
