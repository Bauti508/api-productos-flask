from flask import Flask, jsonify, request 

app = Flask(__name__)

productos = []



@app.route("/productos", methods=["POST"])
def enviar():
    data = request.json 
    nuevo = {"id": len(productos) + 1, **data}
    productos.append(nuevo)
    return jsonify(nuevo)

@app.route("/productos", methods=["GET"])
def obtener():
    return jsonify(productos)

@app.route("/productos/<int:id>", methods=["GET"])
def obtener_id(id):
   
    for item in productos:
        if item ["id"] == id:
            return jsonify(item)
    return jsonify({"error": "pagina no encontrada"}), 404

@app.route("/productos/<int:id>", methods=["PUT"])
def modificar(id):
    data = request.get_json()
    for item in productos:
        if item ["id"] == id:
            item.update(data)
            return jsonify(item)
    return jsonify({"error": "pagina no encontrada"}), 404

@app.route("/productos/<int:id>", methods=["DELETE"])
def eliminar(id):
   
    for item in productos:
        if item ["id"] == id:
            productos.remove(item)
            return jsonify({"mensaje": "producto eliminado"})
    return jsonify ({"error": "pagina no encontrada"}), 404

@app.route("/productos/categoria/<categoria>", methods=["GET"])
def categoria(categoria):
    
    resultado = [c for c in productos if c ["categoria"].lower() == categoria.lower()]

    if resultado:
        return jsonify(resultado)

    return jsonify({"error": "no se encontro la pagina"}), 404

@app.route("/productos/stock_bajo", methods=["GET"])
def stock_bajo ():
    resultado = [s for s in productos if s ["stock"] < 5]
    
    if resultado:
       return jsonify (resultado)
    return jsonify({"error": "no se encontro la pagina"}), 404

@app.route("/productos/nombre", methods=["GET"])
def nombre():
    nombre = request.args.get("nombre")

    if not nombre:  
        return jsonify({"error": "pagina no encontrada"}), 404


    resultado = [p for p in productos if p["nombre"].lower() == nombre.lower()]

    if resultado:

        return jsonify(resultado)

    return jsonify({"error": "pagina no encontrada"}), 404

if __name__ == "__main__":
    app.run (debug=True)