from tree_sitter import Language, Parser, Node

def print_function_info(node: Node, indent: str):
    # Print function or class name
    name_node = node.child_by_field_name('name')
    name = name_node.text.decode('utf8') if name_node else "<unnamed>"
    print(f"{indent}Type: {node.type}, Name: {name}")

    # Optionally, print details about parameters, return type, etc.

    # Print details about the function or class body
    body_node = node.child_by_field_name('body')
    if body_node:
        print(f"{indent}Body:")
        print_structure(body_node, indent + "  ")

def print_structure(node: Node, indent: str):
    for child in node.children:
        if child.type in ['function_definition', 'class_definition']:
            print_function_info(child, indent)
        elif child.type in ['if_statement', 'for_statement', 'while_statement']:
            # You can add more conditions or types as needed
            print(f"{indent}{child.type} [Start: {child.start_point}, End: {child.end_point}]")

def get_code_overview(file_path: str):
    PY_LANGUAGE = Language('build/my-languages.so', 'python')
    parser = Parser()
    parser.set_language(PY_LANGUAGE)

    with open(file_path, 'rb') as file:
        source_code = file.read()

    tree = parser.parse(source_code)
    root_node = tree.root_node
    print(f"Overview of {file_path}:")
    print_structure(root_node, "")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python code_overview.py <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    get_code_overview(file_path)
