def format(original: str) -> str:
    return original.replace(' ', '_').replace('.', '') + '.py'


original = input('Problem Title > ')
print(format(original))