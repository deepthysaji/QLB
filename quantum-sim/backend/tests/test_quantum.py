import unittest
from quantum_exec import execute_circuit  # Adjust the import based on your actual function location

class TestQuantumExecution(unittest.TestCase):

    def test_execute_circuit_valid(self):
        circuit_description = {
            "num_qubits": 2,
            "circuit": [
                ["H", 0],
                ["CNOT", [0, 1]],
                ["Z", 1]
            ]
        }
        result = execute_circuit(circuit_description)
        self.assertIn('state_vector', result)
        self.assertIn('probabilities', result)

    def test_execute_circuit_invalid(self):
        circuit_description = {
            "num_qubits": 2,
            "circuit": [
                ["INVALID_GATE", 0]
            ]
        }
        with self.assertRaises(ValueError):
            execute_circuit(circuit_description)

if __name__ == '__main__':
    unittest.main()