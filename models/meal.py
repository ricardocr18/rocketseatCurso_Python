from database import db
from datetime import datetime

class Meal(db.Model):
    __tablename__ = 'meal'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_on_diet = db.Column(db.Boolean, nullable=False, default=True)
    
    # Chave estrangeira para relacionar com o usuário
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Relacionamento (acessa o usuário dono da refeição)
    user = db.relationship('User', backref=db.backref('meals', lazy=True, cascade='all, delete-orphan'))
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date_time": self.date_time.isoformat() if self.date_time else None,
            "is_on_diet": self.is_on_diet,
            "user_id": self.user_id
        }