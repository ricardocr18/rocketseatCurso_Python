from .calculator_2 import Calculator2
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.drivers_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, number: List[float]) -> float:
        return 3 # aqui estamos retornando um valor fixo para o desvio padrão, para que possamos testar a lógica do cálculo sem depender do resultado real do desvio padrão.

def test_calculate_integration():
    mock_request = MockRequest({
        "numbers": [2.12, 4.62, 1.32]
        })
    
    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    format_response = calculator_2.calculate(mock_request)

    print()
    print(format_response)

    assert isinstance(format_response, dict)
    assert format_response == {
        "data": {
            "Calculator": 2,
            "result": 0.08
            }
        }
    
def test_calculate():
    mock_request = MockRequest({
        "numbers": [2.12, 4.62, 1.32]
        })
    
    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)
    format_response = calculator_2.calculate(mock_request)    

    assert isinstance(format_response, dict)
    assert format_response == {
        "data": {
            "Calculator": 2,
            "result": 0.33
            }
        }
