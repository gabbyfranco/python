#DONE: declare variables

bill = 175.00

tax_rate = 15

#DONE: calculate total tax
total_tax = (bill * tax_rate)/100.00

#DONE: print the total tax
print('Total tax', total_tax)

#TODO: create a reusable function

def calculate_tax(bill, tax_rate):
    return (bill * tax_rate) / 100.00