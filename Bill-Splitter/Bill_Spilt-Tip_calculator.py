print("Welcome to the Bill-Split calculator!")
bill=float(input("What was the total bill? $ "))
tip=int(input("How much tip would you like to give? 10, 12, or 15?"))
people=int(input("How many people to split the bill?"))

tip_in_per=(tip/100)*bill
total_bill=bill+tip_in_per
Total_amount_per=round(total_bill/people,2)

print(f"How many people to split the bill? ${Total_amount_per}")