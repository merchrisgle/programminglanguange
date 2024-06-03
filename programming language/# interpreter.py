# interpreter.py

class Interpreter:
    def __init__(self):
        self.variables = {}

    def evaluate_expression(self, expression):
        try:
            return eval(expression, {}, self.variables)
        except Exception as e:
            return f"Error: {str(e)}"

    def execute(self, code):
        lines = code.split('\n')
        output = []
        for line in lines:
            if '=' in line:
                var, expr = line.split('=')
                var = var.strip()
                expr = expr.strip()
                self.variables[var] = self.evaluate_expression(expr)
                output.append(f"{var} = {self.variables[var]}")
            else:
                output.append(self.evaluate_expression(line))
        return output

if __name__ == "__main__":
    with open('sample.mylang', 'r') as file:
        code = file.read()
    interpreter = Interpreter()
    result = interpreter.execute(code)
    for line in result:
        print(line)
