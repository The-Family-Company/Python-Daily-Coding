amount=float(input("enter to be pay"))

if (amount>1000):
    print("you get 5% discount")
    amount_pay=amount=(0.05*amount)
    print("after discount amount:",amount_pay)
elif (amount>2000):
    print("you get 8% discount")
    amount_pay=amount=(0.08*amount)
    print("after discount amount:",amount_pay)
else:
    print("sorry,no discount")    