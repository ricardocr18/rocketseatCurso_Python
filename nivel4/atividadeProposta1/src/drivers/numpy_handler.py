# Aqui é uma faixada para o módulo numpy, para que possamos usar a classe NumpyHandler
# sem precisar importar o numpy diretamente em outros arquivos.

import numpy
from typing import List

class NumpyHandler:
    def __init__(self) -> None:
        self._np = numpy

    # desvio padrão
    def standard_derivation(self, numbers: List[float]) -> float:
        return self._np.std(numbers)