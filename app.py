from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    return html

@app.route('/<path:filename>')
def serve_static(filename):
    # servir archivos CSS, JPG, PNG o JS del mismo nivel
    if filename.endswith(".css"):
        with open(filename, "r", encoding="utf-8") as f:
            return Response(f.read(), mimetype="text/css")
    elif filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
        with open(filename, "rb") as f:
            return Response(f.read(), mimetype="image/jpeg")
    elif filename.endswith(".js"):
        with open(filename, "r", encoding="utf-8") as f:
            return Response(f.read(), mimetype="application/javascript")
    else:
        return "Archivo no permitido", 404

if __name__ == "__main__":
    app.run(debug=True)
