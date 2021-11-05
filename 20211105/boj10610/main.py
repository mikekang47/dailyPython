n = int(''.join(sorted(list(input()), reverse=True)))
print(n if n % 30 == 0 else -1)
