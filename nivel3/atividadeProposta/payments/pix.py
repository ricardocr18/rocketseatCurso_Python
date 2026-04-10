import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    # Vamos gerar os dados financeiros aqui nesse código, onde estamos simulando a criação do pagamento na instituição financeira, onde o banco vai gerar um ID para o pagamento e um hash, que é o código que vai ser usado para gerar o QR code
    # O base_dir é o caminho em branco aqui, mais lá no arquivo de Teste Unitário "test_pix.py" para passar o caminho correto.
    def create_payments(self, base_dir=""):

        bank_payment_id = str(uuid.uuid4())  # Gerar um ID único para o pagamento "poderia ser do proprio Banco"
        hash_payment = f'hash_payment_{bank_payment_id}'  # Gerar um hash para o pagamento "poderia ser do proprio Banco"

        img = qrcode.make(hash_payment)  # Gerar o QR code a partir do hash do pagamento
        img.save(f'{base_dir}static/img/qr_code_payment_{bank_payment_id}.png')  # Salvar o QR code como uma imagem PNG
        
        # criar pagamento na instituição financeira
        return{"bank_payment_id": bank_payment_id,
                "qr_code_path": f"qr_code_payment_{bank_payment_id}",
                }