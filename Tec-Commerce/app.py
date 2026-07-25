from flask import Flask, render_template, request, session, redirect, url_for
import json

app = Flask(__name__)
app.secret_key = "tec-commerce-secret-key"


# Load products from JSON
def load_products():
    with open("products.json", "r", encoding="utf-8") as file:
        return json.load(file)


@app.route("/")
def home():
    products = load_products()
    return render_template("index.html", products=products)


@app.route("/products")
def products():
    products = load_products()

    search = request.args.get("search", "").lower()

    if search:
        filtered = [
            p for p in products
            if search in p["name"].lower()
            or search in p["category"].lower()
        ]
    else:
        filtered = products

    return render_template("products.html", products=filtered)


@app.route("/product/<int:id>")
def product(id):
    products = load_products()

    product = next((p for p in products if p["id"] == id), None)

    if not product:
        return "Product Not Found"

    return render_template("product.html", product=product)


@app.route("/cart")
def cart():

    cart = session.get("cart", [])

    products = load_products()

    cart_items = []

    total = 0

    for item in cart:

        product = next((p for p in products if p["id"] == item["id"]), None)

        if product:
            subtotal = product["price"] * item["quantity"]

            total += subtotal

            cart_items.append({
                "product": product,
                "quantity": item["quantity"],
                "subtotal": subtotal
            })

    return render_template(
        "cart.html",
        cart_items=cart_items,
        total=total
    )


@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):

    cart = session.get("cart", [])

    found = False

    for item in cart:
        if item["id"] == id:
            item["quantity"] += 1
            found = True
            break

    if not found:
        cart.append({
            "id": id,
            "quantity": 1
        })

    session["cart"] = cart

    return redirect(url_for("cart"))


@app.route("/remove/<int:id>")
def remove(id):

    cart = session.get("cart", [])

    cart = [item for item in cart if item["id"] != id]

    session["cart"] = cart

    return redirect(url_for("cart"))


@app.route("/checkout", methods=["GET", "POST"])
def checkout():

    if request.method == "POST":

        session.pop("cart", None)

        return redirect(url_for("success"))

    return render_template("checkout.html")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)