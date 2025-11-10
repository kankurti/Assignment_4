from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB (make sure MongoDB is running)
client = MongoClient("mongodb://localhost:27017/")
db = client["tododb"]
collection = db["items"]

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    if not item_name or not item_description:
        return jsonify({"message": "Missing data"}), 400

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })
    return jsonify({"message": "To-Do item saved successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
