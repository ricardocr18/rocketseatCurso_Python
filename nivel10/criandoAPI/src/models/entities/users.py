from sqlalchemy import Table, Column, Integer, String
from src.models.settings.metadata import metadata

Users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_name", String, nubllable=True),
    Columm("age", Integer),
    Columm("uf", String)
)