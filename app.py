from flask import Flask, request, jsonify
from generator import InvoiceGenerator

app = Flask(__name__)

@app.route("/")
def index():
    return {"status": "AI Invoice Pro API", "version": "1.0"}

@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.json
    inv = InvoiceGenerator()
    inv.set_company(**data.get("company", {}))
    inv.set_client(**data.get("client", {}))
    inv.set_invoice(**data.get("invoice", {}))
    for item in data.get("items", []):
        inv.add_item(**item)
    return jsonify(inv.save())

if __name__ == "__main__":
    app.run(debug=True)
