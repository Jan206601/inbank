from flask import Flask, jsonify, request, render_template

from loan_calculator import *

app = Flask(__name__)


# API endpoint for getting loan decision
@app.route('/api/check_loan', methods=['POST'])
def check_loan():
    # Read POST form data
    personal_code = request.form['personal_code']
    amount = int(request.form['amount'])
    period = int(request.form['period'])

    # Check if personal code found in imaginary database
    if not LoanCalculator().personal_code_known(personal_code):
        response = {'decision': None, 'error_message': 'Personal code unknown'}
        return jsonify(response)

    # Check if person has debt
    if LoanCalculator().person_has_debt(personal_code):
        response = {'decision': None, 'error_message': 'Person is in debt! No loan available.'}
        return jsonify(response)

    # Check if desired amount and period are in allowed range
    if not LoanCalculator().amount_in_allowed_range(amount):
        return jsonify({'decision': None,
                        'error_message': f'Amount must not be under {MINIMUM_AMOUNT}€ or over {MAXIMUM_AMOUNT}€.'})
    if not LoanCalculator().period_in_allowed_range(period):
        return jsonify({'decision': None,
                        'error_message': f'Period must not be under {MINIMUM_PERIOD} or over {MAXIMUM_PERIOD} months.'})

    # Check whether loan is possible under the desired conditions
    decision = LoanCalculator().get_loan_decision(personal_code, amount, period)
    # Calculate personal maximum possible amount for the desired period
    possible_maximum_amount = LoanCalculator().get_maximum_amount(personal_code, period)
    # Calculate personal possible period for the desired period
    possible_period = LoanCalculator().get_suitable_period_for_amount(personal_code, amount)

    # Process form data and return response as JSON
    response = {
        'decision': decision,
        'maximum_amount_for_period': possible_maximum_amount,
        'minimum_period_for_amount': possible_period
    }
    return jsonify(response)


@app.route('/')
def index():
    # Render the HTML file for front-end
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
