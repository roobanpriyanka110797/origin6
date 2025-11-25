from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit-contact", methods=["POST"])
def submit_contact():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No data received"}), 400

    contacts_file = "contacts.json"


    if os.path.exists(contacts_file):
        with open(contacts_file, "r") as f:
            try:
                contacts = json.load(f)
            except json.JSONDecodeError:
                contacts = []
    else:
        contacts = []


    contacts.append(data)


    with open(contacts_file, "w") as f:
        json.dump(contacts, f, indent=2)

    return jsonify({"message": "Success"}), 200


if __name__ == "__main__":
    app.run(debug=True)
