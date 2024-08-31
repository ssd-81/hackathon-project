from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
from sqlalchemy.orm import sessionmaker

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
def get_db_connection():
    Session = sessionmaker(bind=engine)
    return Session()


def load_records_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from patient"))
        result_all = result.all()
        result_dicts = []
        for row in result_all:
            result_dicts.append((dict(row._mapping)))
    return result_dicts