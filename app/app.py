from flask import Flask, jsonify, request

app = Flask(__name__)

customers = [{"id": 1, "name": "John Doe"}]

@app.route("/customers", methods=["GET"])
def get_customers():
    return jsonify(customers)

@app.route("/customers", methods=["POST"])
def create_customer():
    data = request.json
    customers.append(data)
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)