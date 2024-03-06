from flask import Flask, request, jsonify
import jwt
import re

app = Flask(__name__)

def is_prime(n):
    n = int(n) # Converte n para um inteiro
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def validate_jwt(token):
    try:
        payload = jwt.decode(token, options={"verify_signature": False})
        if len(payload) != 3:
            return False
        if not re.match("^[a-zA-Z\s]*$", payload.get("Name", "")):
            return False
        if payload.get("Role") not in ["Admin", "Member", "External"]:
            return False
        if not is_prime(payload.get("Seed", 0)):
            return False
        if len(payload.get("Name", "")) > 256:
            return False
        return True
    except jwt.DecodeError:
        return False

@app.route('/validate', methods=['POST'])
def validate():
    token = request.json.get('token')
    if not token:
        return jsonify({"valid": False, "reason": "Token not provided"}), 400
    valid = validate_jwt(token)
    return jsonify({"valid": valid})

if __name__ == '__main__':
    app.run(debug=True)
