from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def execute_circuit(circuit_description):
    # Extract number of qubits and circuit operations from the description
    num_qubits = circuit_description['num_qubits']
    operations = circuit_description['circuit']

    # Create a QuantumCircuit object
    qc = QuantumCircuit(num_qubits)

    # Add operations to the circuit
    for operation in operations:
        gate = operation[0]
        targets = operation[1]

        if gate == "H":
            qc.h(targets)
        elif gate == "CNOT":
            qc.cx(targets[0], targets[1])
        elif gate == "Z":
            qc.z(targets)
        else:
            raise ValueError(f"Invalid gate: {gate}")

    # Save the statevector and run simulation
    qc.save_statevector()
    backend = AerSimulator()
    state_vector = backend.run(qc).result().get_statevector()
    
    # Get probabilities using shots-based simulation
    qc_with_measure = qc.copy()
    qc_with_measure.measure_all()
    counts = backend.run(qc_with_measure, shots=1024).result().get_counts()
    total_shots = sum(counts.values())
    probabilities = {state: count/total_shots for state, count in counts.items()}

    return {
        "state_vector": state_vector.tolist(),
        "probabilities": probabilities
    }