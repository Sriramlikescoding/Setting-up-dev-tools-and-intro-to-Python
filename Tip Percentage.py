def total_amount(bill_amount,tip_percent):
    total = bill_amount*(1+0.01*tip_percent)
    total = round(total,2)
    print(f"Please pay ${total}")


total_amount(150,20)