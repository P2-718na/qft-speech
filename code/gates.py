from qiskit import QuantumCircuit, converters
from math import pi


def c_7mod15_gate(power):

    U = QuantumCircuit(4)
    # https://quantumcomputing.stackexchange.com/questions/15280/how-does-this-represent-modular-multiplication

    for _ in range(power):
      U.x(range(4))
      U.swap(1, 2)
      U.swap(2, 3)
      U.swap(0, 3)

    U = U.to_gate()
    U.name = "%i^%i mod 15" % (7, power)
    c_U = U.control() ##.control(t)
    return c_U


# blatantly stole qft circuit generator from this:
# https://learn.qiskit.org/course/ch-algorithms/quantum-fourier-transform


def qft_rotations(circuit, n):
    """Performs qft on the first n qubits in circuit (without swaps)"""
    if n == 0:
        return circuit
    n -= 1
    circuit.h(n)
    for qubit in range(n):
        circuit.cp(pi/2**(n-qubit), qubit, n)
    # At the end of our function, we call the same function again on
    # the next qubits (we reduced n by one earlier in the function)
    qft_rotations(circuit, n)


def swap_registers(circuit, n):
    for qubit in range(n//2):
        circuit.swap(qubit, n-qubit-1)
    return circuit


def qft(circuit, n):
    """QFT on the first n qubits in circuit"""
    qft_rotations(circuit, n)
    swap_registers(circuit, n)
    return circuit


def qft_gate(n):
  qc = QuantumCircuit(n)
  qc.name = "QFT"
  qft(qc, n)
  gate = converters.circuit_to_gate(qc)

  return gate


def inverse_qft_gate(n):
  return qft_gate(n).inverse()
