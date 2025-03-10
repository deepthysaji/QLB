# Quantum Circuit Simulator

## Overview
The Quantum Circuit Simulator is a web-based application that allows users to build and execute quantum circuits using a Qiskit-powered backend. The application features a user-friendly interface for constructing circuits and visualizing results.

## Project Structure
```
quantum-sim
├── backend
│   ├── app.py               # Main Flask application
│   ├── quantum_exec.py      # Circuit execution using Qiskit
│   ├── tests
│   │   └── test_quantum.py  # Unit tests for quantum execution
│   └── requirements.txt     # Dependencies for the backend
├── frontend
│   ├── index.html           # Main UI for the frontend
│   ├── css
│   │   └── style.css        # Styling for the frontend
│   └── js
│       └── script.js        # Frontend logic
└── .gitignore               # Files to ignore by Git
```

## Setup Instructions

### Backend
1. Navigate to the `backend` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```
   python app.py
   ```

### Frontend
1. Open `index.html` in a web browser to access the quantum circuit builder interface.

## Usage
- Use the drag-and-drop interface to add quantum gates and build circuits.
- Click the "Run Circuit" button to execute the circuit on the backend.
- View the results, including the state vector and measurement probabilities, displayed on the frontend.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.