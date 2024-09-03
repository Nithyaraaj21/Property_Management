from flask import Flask, jsonify

app = Flask(__name__)

# Dummy data
properties = {
    'Property 1': {
        'location': '123 Main St',
        'type': 'Apartment',
        'size': '1200 sq ft',
        'status': 'Occupied'
    }
}

maintenance_requests = [
    {'id': 1, 'status': 'Pending', 'description': 'Leaky faucet in kitchen'},
]

financials = {
    'rent_due': '2024-09-05',
    'amount_due': '$1200',
    'payment_history': [
        {'date': '2024-08-01', 'amount': '$1200'}
    ]
}

@app.route('/properties', methods=['GET'])
def get_properties():
    return jsonify(properties)

@app.route('/maintenance', methods=['GET'])
def get_maintenance_requests():
    return jsonify(maintenance_requests)

@app.route('/financials', methods=['GET'])
def get_financials():
    return jsonify(financials)

if __name__ == '__main__':
    app.run(debug=True)
