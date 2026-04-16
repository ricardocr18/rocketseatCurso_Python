from flask import Flask
from src.main.routes.calculators import cal_router_bp

app = Flask(__name__)
app.register_blueprint(cal_router_bp)