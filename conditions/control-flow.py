bill_total = 95

discount1 = 10

if bill_total > 100:
    print("Bill is greater than 100!!!")
    bill_total = bill_total - discount1
else: 
    print("Bill is less than 100!")
    
    
print("Total bill:" + str(bill_total))