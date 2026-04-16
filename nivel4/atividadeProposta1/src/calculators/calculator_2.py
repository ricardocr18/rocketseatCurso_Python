from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.numpy_handler import NumpyHandler

class Calculator2:
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        print("Impressão do body:", body)
        input_data = self.__validate_body(body)
        print("Impressão do input_data:", input_data)
        calculated_number = self.__process_data(input_data)

        format_response = self.__format_response(calculated_number)
        return format_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("body mal formatado!")

        input_data = body["numbers"]
        return input_data
    
    def __process_data(self, input_data: List[float]) -> float:
        # Aqui é onde a mágica acontece! Vamos usar a classe NumpyHandler para calcular o desvio padrão dos números processados.
        numpy_handler = NumpyHandler()
        first_proces_result = [(num * 11) ** 0.95 for num in input_data]
        print()
        print("Impressão do first_proces_result:", first_proces_result)
        result = numpy_handler.standard_derivation(first_proces_result) # aqui estamos usando a classe NumpyHandler para calcular o desvio padrão dos números processados.
        print ("Impressão do result:", result)
        return 1/result
    
    def __format_response(self, calculated_number: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": float(round(calculated_number, 2))
            }           
        }