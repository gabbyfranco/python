# Conditional statements

This reading introduces you to the conditional statements of **_if, else and elif_**_**.

_**If**_
In keeping with the light switch example, the state of the switch can be stored with a Boolean value of **_True_** or _**False**_.

+   On = True

+   Off = False

_#Light is currently off_
**_current = False_**

**_if current:_**
    **_current = False_**
    **_print('Turning light off')_**

**_if not current:_**
    **_current = True_**
    **_print('Turning light on')_**

The code snippet above has a variable called _**current**_ which keeps track of the state of the light - on or off. The first _**if**_ statement will check if the light is on and if it is, the flow will go inside the condition and set the **_current_** variable to False - turning the light off. In the above code snippet, the value of the _**current**_ variable is initially set to **_False_**, so this condition is not met.

The second **_if_** statement will check if the light is off and if it is, the flow will go inside the condition and will set the **_current_** varaible to _**True**_- turning the light on. 

## If else
The above code works fine but it can be rewritten more effectively by using another condition called _**else**_. The following code is an example:

**_current = False_**

**_if current:_**
    _**current = False**_
    **_print('Turning light off')_**
**_else:_** 
    **_current = True_**
    **_print('Turning light on')_**

The _**else**_ statement has made your code a bit easier to read and given that the flow relates to the same condition, it makes more sense to combine them as part of a single unit.

## elif
Python also has another condition called _**elif**_ which helps when you have multiple conditions to satisfy. The light switch example is pretty straightforward in that you only have to check for the state of on or off - _**True**_ or **_False_**. In certain conditions, it may not be that easy. Thankfully _**elif**_ is here to help.

Let's say you want to give a certain discount to customers if they spend over $100. You will also provide an extra discount if that customer is part of a loyalty program. If the customer is not part of the loyalty program and did not spend over a $100, a service charge of 5% is applied.

loyalty_customer = True
total_bill = 124

***if loyalty_customer and total_bill > 100:***
    ***#give 20% discount***
    ***total_bill = total_bill - (float(total_bill)/ 100) * 20***
***elif total_bill > 100:***
    ***#give 10% discount***
    ***total_bill = total_bill - (float(total_bill)/ 100) * 10***
***else:***
    ***#sorry no discount, 5% service charge applied.***
   ***print('Sorry, no discount ...')***

***print('Total Bill: ', float(total_bill))***

The above code snippet first checks to see if the customer is part of the loyalty program and if they are spending over $100. If both conditions are met, a discount of 20% is applied to the bill. The ***elif*** statement will only be executed if the first ***if*** condition is not met. The ***elif*** statement will only check if the bill is over $100 and if it is, it will apply a discount of 10%  to the bill.

The final ***else*** statement is only executed if neither of the other two conditions are met. In this case, a charge of 5% is applied to the bill.