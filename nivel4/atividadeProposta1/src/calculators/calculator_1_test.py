from typing import Dict
from pytest import raises
from .calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest({"number": 1})
    calculator_1 = Calculator1()
    reponse = calculator_1.calculate(mock_request)
    print()
    print("ResponseMater: ", reponse)

    # formato da resposta
    assert "data" in reponse
    assert "Calculator" in reponse["data"]
    assert "result" in reponse["data"]

    # Assertividade da resultado
    assert reponse["data"]["Calculator"] == 1
    assert reponse["data"]["result"] == 14.25

def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": 1})
    calculator_1 = Calculator1()

    with raises(Exception) as excinfo:
        calculator_1.calculate(mock_request)

    assert str(excinfo.value) == "body mal formatado!"