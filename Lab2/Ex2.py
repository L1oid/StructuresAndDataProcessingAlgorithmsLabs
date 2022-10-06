def tribonacci(n):
    if n in (0, 1):
        return 0
    elif n in (2, 3):
        return 1
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

print(tribonacci(0))
print(tribonacci(1))
print(tribonacci(3))
print(tribonacci(5))
print(tribonacci(6))
print(tribonacci(12))
print(tribonacci(17))