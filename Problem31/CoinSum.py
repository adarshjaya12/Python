coins = [1, 2, 5, 10, 20, 50, 100, 200]


def count_change(amount, n):
    if amount == 0:
        return 1
    elif amount < 0 or n == 0:
        return 0
    else:
        return count_change(amount, n - 1) + count_change(
            amount - coins[n - 1], n);


print count_change(200, len(coins))