def is_fibonacci(n):
    if n < 0:
        return False

    a, b = 0, 1
    while b < n:
        a, b = b, a + b

    return b == n or n == 0

# Testando o número 21
numero = 21

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
