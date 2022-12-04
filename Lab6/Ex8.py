bank = {1: 400, 3: 250, 4: 100, 10: 100, 50: 75, 100: 10}
coins = [1, 3, 4, 10, 50, 100]

clients_number = int(input("Количество клиентов: "))

for c in range(clients_number):
    print("Клиент", c+1)
    sum = int(input("Сумма: "))
    lookup = [float("inf")] * (sum+1)
    lookup[0] = 0
    for m in range(1, sum+1):
        for i in range(len(coins)):
            if m >= coins[i] and lookup[m-coins[i]] + 1 < lookup[m]:
                lookup[m] = lookup[m-coins[i]] + 1

    answer = {}
    while (sum > 0):
        for i in range(len(coins)):
            if lookup[sum-coins[i]] == lookup[sum] - 1:
                sum -= coins[i]
                if coins[i] in answer:
                    answer[coins[i]] += 1
                else:
                    answer[coins[i]] = 1
                break

    answer_keys = list(answer.keys())
    bank_c = bank.copy()

    status = True
    for coin in answer_keys:
        bank_c[coin] -= answer[coin]
        if bank_c[coin] < 0:
            status = False
            break

    if status:
        bank = bank_c
        sorted_tuple = sorted(answer.items(), key=lambda x: -x[0])
        print("Выдача: ", dict(sorted_tuple))
        print("Банк:", bank)
    else:
        print("Недостаточно купюр для выдачи такой суммы")
