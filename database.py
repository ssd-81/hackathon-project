from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

db_connection_string = os.getenv('DB_CONNECTION_STRING')

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "<CA_PATH>",
        }
    }
)

def load_records_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from p"))
        result_all = result.all()
        result_dicts = []
        for row in result_all:
            result_dicts.append(dict(dict(row._mapping)))
    return result_dicts

