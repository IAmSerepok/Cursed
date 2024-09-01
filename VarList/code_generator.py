def generate(size):
    code = 'class List:\n\t'

    for _1 in range(size):
        code += f'a{_1} = None\n\t'

    code += '\n\tdef get(self, index):\n\t\t'
    code += 'if index == 0: return self.a0\n\t\t'

    for _1 in range(1, size):
        code += f'elif index == {_1}: return self.a{_1}\n\t\t'

    code += 'else: raise ValueError(\'List index is out of range\')\n'

    code += '\n\tdef set(self, index, value):\n\t\t'
    code += 'if index == 0: self.a0 = value\n\t\t'

    for _1 in range(1, size):
        code += f'elif index == {_1}: self.a{_1} = value\n\t\t'

    code += 'else: raise ValueError(\'List index is out of range\')\n'

    return code


if __name__ == '__main__':
    code = generate(5)
    with open('code.py', 'w') as f:
        f.write(code)
    print(code)
