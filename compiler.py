import re


class Token(object):
    def __init__(self, value):
        self.value = value
        if self.value in "+-*/":
            self.type = "OPERATOR"
        else:
            self.type = "NUMBER"

    def __repr__(self):
        return '[' + self.value + ']'


class Node(object):
    def __init__(self, token):
        self.token = token
        self.left = None
        self.right = None

    def __repr__(self):
        return self.vis()

    def vis(self, indent=2):
        subtree = str(self.token)
        if self.left:
            ws = '\n' + ''.join(' ' for _ in range(indent))
            subtree = subtree + ws + self.left.vis(indent + 2) + ws + self.right.vis(indent=indent + 2)
        return subtree


def scan(text):
    return [Token(symbol.strip()) for symbol in re.split('([+*-/])', text)]


def parse(tokens):
    # We build a tree
    if len(tokens) == 1:
        return Node(tokens[0])
    for i, token in enumerate(tokens):
        # Look for a plus or minus, these are the most important signs because they take least precedence
        if token.value in "+-":
            # Create a new node with the operator on top and the remaining tokens split as its children
            root = Node(token)
            root.left = parse(tokens[:i])
            root.right = parse(tokens[i + 1:])
            return root  # Return the subtree
    for i, token in enumerate(tokens):
        # If there are no more plus or minus signs in the equation, look for multiplication and division
        if token.value in "*/":
            root = Node(token)
            root.left = parse(tokens[:i])
            root.right = parse(tokens[i + 1:])
            return root


def visit(node):
    # Traverses a tree in postfix manner and returns a linear representation of the tree as a list of tokens
    if node.left:
        return visit(node.left) + visit(node.right) + [node.token]
    return [node.token]


def compile(tokens):
    instructions = []
    for token in tokens:
        if token.value == "+":
            instructions.append("add")
        elif token.value == "-":
            instructions.append("sub")
        elif token.value == "*":
            instructions.append("mul")
        elif token.value == "/":
            instructions.append("div")
        elif token.type == "NUMBER":
            instructions.append("put " + str(token.value))
    instructions.append("end")
    return instructions