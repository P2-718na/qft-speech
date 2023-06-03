from qutip import *
from qutip.qip.circuit_latex import _latex_compile
N = 3
qc = QubitCircuit(N)

qc.add_gate("CNOT", targets=[0], controls=[2])

latex_code = qc.latex_code()
print(latex_code)

compiled_latex = _latex_compile(latex_code)
print(compiled_latex)

from IPython.display import Image
Image(compiled_latex, embed=True)
