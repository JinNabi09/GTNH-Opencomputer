from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
status_data = {}

@app.route("/")
def dashboard():
    return render_template("dashboard.html", status=status_data)

@app.route("/update", methods=["POST"])
def update():
    try:
        data = request.get_json(force=True)
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    machine_id = data.get("machine_id")
    if not machine_id:
        return jsonify({"error": "Missing machine_id"}), 400

    status_data[machine_id] = {
        "status": data.get("status", "unknown"),
        "message": data.get("message", ""),
    }

    return jsonify({"ok": True})

@app.route("/status")
def status_json():
    return jsonify(status_data)
