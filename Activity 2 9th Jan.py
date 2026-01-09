actual_cost=float(input("Please Enter the Actual Price: "))
sales_amount=float(input("Please enter the Sales Price: "))
if sales_amount>actual_cost:
    amount=sales_amount-actual_cost
    print("Total Profit is:",amount)

else:
    print("No Profit!")