from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def guardar_celular():
    data = request.get_json()
    celular = data.get("celular", "Sin número")
    print(f"Recibido: {celular}")
    return jsonify({"status": "ok", "celular": celular})
