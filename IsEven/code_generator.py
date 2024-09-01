def generate(size):
    code = ''

    code += 'def is_even(number):\n\t'
    code += 'if number < 0: raise ValueError(\"I don\'t know\")\n\t'

    for _1 in range(size):
        code += f"elif number == {_1}: return {'True' if _1 % 2 == 0 else 'False'}\n\t"

    code += 'else: raise ValueError(\"I don\'t know\")\n'

    return code


if __name__ == '__main__':
    code = generate(10 ** 6 + 1)
    with open('code.py', 'w') as f:
        f.write(code)
    print(code)
