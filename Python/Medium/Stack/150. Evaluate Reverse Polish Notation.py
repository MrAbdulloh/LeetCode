def evalRPN(tokens: list) -> int:
    stack = []

    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return int(stack[0])


# tokens = ["4", "13", "5", "/", "+"]
tokens = ["18"]
print(evalRPN(tokens))
