#### Inbank Software Engineer Intern - assignment

Author: Jan Ulrich Sütt

The API is implemented using Python Flask framework to provide lightweight web app functionality.
Simple front-end application for using the functionality is served through the same python application.

Run the server from `python main.py`

The application is accessible on port 5000:
http://127.0.0.1:5000/


##### How I approached the problem

The desired loan conditions are collected from the form on index.html.
The server validates the input and checks the personal number for calculating the decision.
Person is also checked for having a debt.

The LoanCalculator class first determines if loan under given conditions is possible and additionally always calculates the maximum amount for the given period of time. It also finds suitable period for the given amount, which is shown to the user only in case of negative loan decision.

The maximum loan amount is calculated prior to making loan decision under given conditions.
To calculate maximum amount, a mathematical approach following this formula is used:

**credit score = (credit modifier / loan amount) * loan period**

As the credit score has to be bigger or equal to 1 for positive decision, it is necessary to find the maximum loan amount for which the equality is true:

**(credit modifier / loan amount) * loan period >= 1**

This is done by transforming the formula and finding the intercept for loan amount parameter as follows:

**(credit modifier / loan amount) * loan period = 1**

**(credit modifier / loan amount) = 1 * loan period**

**loan amount = (credit modifier * loan period) / 1**

**loan amount = credit modifier * loan period**

Alternatively, inefficient iterative approach could be used, which would have resulted in sequentially decreasing the loan amount, until credit score becomes larger or equal to 1.

The minimum period for given amount is calculated using a similar approach, by using the following formula transformation:

**loan period = loan amount / credit modifier**

As the amount and period are expected to be entered as integers, the results are also rounded
(minimum is rounded up and maximum is rounded down).

