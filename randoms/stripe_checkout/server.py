#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, redirect, request,render_template, jsonify

import stripe
# This is your test secret API key.
stripe.api_key = ''
webhook_secret = ''

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://localhost:4242'


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'inr',
                        'unit_amount': 123000,
                        'product_data': {
                            'name': 'membership',
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/concel',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON payload from the request
    payload = request.get_json()

    # Access the required data from the payload
    name = payload['data']['object']
    #print(name)
    print(name['payment_status'])
    print(name['amount_total']/100)
    #payment_status = payload['payment_status']
    #amount_total = payload['amount_total']

    #print(f"{name} {payment_status} the amount {amount_total}")

    # Return a response (optional)
    return jsonify({'success': True}), 200
    

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(port=4242)