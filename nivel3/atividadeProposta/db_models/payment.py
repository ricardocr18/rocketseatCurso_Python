from repository.database import db

class Payment(db.Model):
    # id, value, paid, bank_payment_id, qr_code, expiration_date
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float) # Exemplo 10.50
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.String(200), nullable=True) # UUID tem 36 caracteres
    qr_code = db.Column(db.String(250), nullable=True)
    expiration_date = db.Column(db.DateTime) # Exemplo 2025-01-01 01:01:00


    def to_dict(self):
        return {
            "id": self.id,
            "value": self.value,
            "paid": self.paid,
            "bank_payment_id": self.bank_payment_id,
            "qr_code": self.qr_code,
            "expiration_date": self.expiration_date.isoformat() if self.expiration_date else None
        }
