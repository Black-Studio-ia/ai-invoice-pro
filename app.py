from flask import Flask, request, jsonify, send_file
from generator import InvoiceGenerator
import os

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/generate', methods=['POST'])
def generate_invoice():
    data = request.json
    
    inv = InvoiceGenerator()
    
    inv.set_company(**data.get('company', {}))
    inv.set_client(**data.get('client', {}))
    inv.set_invoice(**data.get('invoice', {}))
    
    for item in data.get('items', []):
        inv.add_item(**item)
    
    result = inv.save()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
