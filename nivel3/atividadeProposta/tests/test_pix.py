# nesse arquivo vamos fazer o Teste Unitário do arquivo /payments/pix.py, onde vamos testar a função create_payments.
from unittest import result

import sys
sys.path.append('../')

import pytest
import os
from payments.pix import Pix

def test_pix_create_payments():
    pix_instance = Pix()

    # create a pagament via pix
    payment_info = pix_instance.create_payments(base_dir="../")

    # aqui estamos verificando se o pagamento criado via pix tem o campo bank_payment_id e qr_code_path,
    # onde esses campos são retornados pela função create_payments, caso contrário o teste vai falhar.
    assert "bank_payment_id" in payment_info
    assert "qr_code_path" in payment_info
    
    # aqui estamos verificando se o arquivo do qr code foi criado no caminho correto, onde o nome do arquivo do
    # qr code é "qr_code_payment_{bank_payment_id}.png", caso contrário o teste vai falhar.
    qr_code_path = payment_info["qr_code_path"]
    assert os.path.isfile(f'../static/img/{qr_code_path}.png')