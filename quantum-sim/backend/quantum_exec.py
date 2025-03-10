def execute_quantum_circuit(circuit_description):
    from qiskit import QuantumCircuit, Aer, execute

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

    # Use the Aer simulator to execute the circuit
    simulator = Aer.get_backend('aer_simulator')
    result = execute(qc, backend=simulator, shots=1024).result()

    # Get the state vector and measurement probabilities
    state_vector = result.get_statevector()
    counts = result.get_counts(qc)

    # Convert counts to probabilities
    probabilities = [counts.get(key, 0) / 1024 for key in qc.measurement]

    return {
        "state_vector": state_vector.tolist(),
        "probabilities": probabilities
    }