fibonacci = [0, 1]
target_number = 4181

while max(fibonacci) < target_number:
    for i in range(2):
        fibonacci_len = len(fibonacci)
        fibonacci.append(fibonacci[fibonacci_len - 1] + fibonacci[fibonacci_len - 2])

print(f'O número {"" if target_number in fibonacci else "não " }pertence à sequência de Fibonacci.')
