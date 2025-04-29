from flask import Flask, render_template
from config.dynamodb_config import get_dynamodb_table

app = Flask(__name__)
table = get_dynamodb_table()

@app.route("/")
def dashboard():
    response = table.scan()
    shipments = sorted(response.get("Items", []), key=lambda x: x["timestamp"], reverse=True)
    return render_template("dashboard.html", shipments=shipments)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

