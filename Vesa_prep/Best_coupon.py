X = int(input())
discount_10_percent = 0.90 * X
discount_flat_100 = X - 100
min_amount_to_pay = min(discount_10_percent, discount_flat_100)
print(int(min_amount_to_pay))
