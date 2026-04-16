from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1

cal_router_bp = Blueprint('calculators', __name__)

@cal_router_bp.route('/calculator/1', methods=['POST'])
def calculator_1():
    calc = Calculator1()
    print("Request: ", request.json) # aqui é só para mostrar o que chegou no request, não é necessário para o funcionamento do código
    response = calc.calculate(request)
    print("Response: ", response) # aqui é só para mostrar o que vai ser enviado no response, não é necessário para o funcionamento do código
    return jsonify(response), 200
