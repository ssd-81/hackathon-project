from sqlalchemy import create_engine


db_connection_string = "mysql+pymysql://2euWq46C4YeBhJn.root:zk61D1ljDOqCSyJb@gateway01.ap-southeast-1.prod.aws.tidbcloud.com/host?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "<CA_PATH>",
        }
    }
)



