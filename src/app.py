from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
        { "label": "My first task", "done": False },
        { "label": "My second task", "done": False },
        { "label": "My third task", "done": False }
]

@app.route('/todos', methods=['GET'])
def handle_Todos():
    resp = jsonify(todos) 
    return resp

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos), 201

'''METODO DELETE'''
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    
    # Valido si la posición que viene de la URL es válida
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Tarea no encontrada"}), 404
    
    # Si lo encuentro borro el todo y retorno la lista actualizada
    del todos[position]
    return jsonify(todos), 200


if __name__=='__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)