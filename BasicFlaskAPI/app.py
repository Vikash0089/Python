from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# In-memory Product DB
products = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Mouse", "price": 500},
]

# ---------- UI ----------
@app.route("/")
def home():
    return render_template("index.html")


# ---------- API CRUD ----------

# Get all products
@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(products)


# Get product by ID
@app.route("/api/products/<int:pid>", methods=["GET"])
def get_product(pid):
    product = next((p for p in products if p["id"] == pid), None)
    return jsonify(product) if product else ({"error": "Not found"}, 404)


# Create product
@app.route("/api/products", methods=["POST"])
def create_product():
    data = request.json
    new_id = max(p["id"] for p in products) + 1 if products else 1

    new_product = {
        "id": new_id,
        "name": data["name"],
        "price": data["price"],
    }

    products.append(new_product)
    return jsonify(new_product), 201


# Update product
@app.route("/api/products/<int:pid>", methods=["PUT"])
def update_product(pid):
    product = next((p for p in products if p["id"] == pid), None)
    if not product:
        return {"error": "Not found"}, 404

    data = request.json
    product["name"] = data.get("name", product["name"])
    product["price"] = data.get("price", product["price"])
    return jsonify(product)


# Delete product
@app.route("/api/products/<int:pid>", methods=["DELETE"])
def delete_product(pid):
    global products
    products = [p for p in products if p["id"] != pid]
    return {"message": "Product deleted"}


if __name__ == "__main__":
    app.run(debug=True)
