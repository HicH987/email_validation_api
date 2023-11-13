from flask import Flask, request, jsonify
from validate_email import validate_email


app = Flask(__name__)


@app.route("/")
def home():
    return "HELLO from flask api"


@app.route("/validate_email", methods=["GET"])
def validate_email_endpoint():
    email = request.args.get("email")

    if email is None:
        return jsonify({"error": "No email provided in the URL"}), 400

    try:
        is_valid = validate_email(
            email_address=email,
            check_format=True,
            check_blacklist=True,
            check_dns=True,
            check_smtp=True,
        )
        return jsonify({"email": email, "is_valid": is_valid})
    except Exception as e:
        return jsonify({"email": email, "error": str(e)}), 500



if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")