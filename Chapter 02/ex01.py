import ast


class SimpleInterpreter(ast.NodeVisitor):
    def __init__(self):
        self.result = 0

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        elif isinstance(node.op, ast.Sub):
            return left - right
        else:
            raise ValueError(f"Unsupported operation: {type(node.op)}")

    def visit_Num(self, node):
        return node.value  # Виправлено deprecation warning через використання n. Лексер пайтону попередив, що цей праметр буде застарілим у майбутніх версіях. Тому використовується node.value замість node.n.

    def interpret(self, code):
        tree = ast.parse(code)
        return self.visit(tree.body[0].value)


if __name__ == '__main__':
    # Тестуємо інтерпретатор
    interpreter = SimpleInterpreter()
    print(interpreter.interpret("3 + 2"))  # Виведе: 6 Але виводить 5.
