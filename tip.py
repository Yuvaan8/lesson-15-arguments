def total_calc(bill_amount,perc_amount):
    total = bill_amount*(1 + 0.01*perc_amount)
    total = round(total, 2)
    print(f'Please pay ${total}')
total_calc(150,20)