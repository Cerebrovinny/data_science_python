house_buyed = 1000000
good_credit = True

if good_credit:
    down_payment = 0.1 * house_buyed
else:
    down_payment = 0.2 * house_buyed
print(f"Down payment: {down_payment}")