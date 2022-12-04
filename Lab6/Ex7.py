coins = [1, 3, 4, 10, 50, 100]

#7.1
n = int(input("Сумма: "))
answer = {}
coins_r = reversed(coins)
for coin in coins_r:
    count = n // coin
    if count > 0:
        answer[coin] = count
    n = n % coin
print(answer)

#7.2
n = int(input("Сумма: "))
lookup = [float("inf")] * (n+1)
lookup[0] = 0

for m in range(1, n+1):
    for i in range(len(coins)):
        if m >= coins[i] and lookup[m-coins[i]] + 1 < lookup[m]:
            lookup[m] = lookup[m-coins[i]] + 1

answer = {}

while (n > 0):
    for i in range(len(coins)):
        if lookup[n-coins[i]] == lookup[n] - 1:
            n -= coins[i]
            if coins[i] in answer:
                answer[coins[i]] += 1
            else:
                answer[coins[i]] = 1
            break

sorted_tuple = sorted(answer.items(), key=lambda x: -x[0])
print(dict(sorted_tuple))
