from flask import Flask, request, jsonify
from quantum_exec import execute_circuit

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()
    if not data or 'circuit' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    circuit_description = data['circuit']
    result = execute_circuit(circuit_description)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)