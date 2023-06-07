import mysql.connector
from mysql.connector import Error


config = {
    "mysql": {
        "host": "192.168.15.95",
        "port": "3306",
        "user": "user48",
        "password": "55907",
        "database": "user48"
    }
}


def connect(db_host, db_port, user_name, user_password, db_name):

    connect_db = None
    try:
        connect_db = mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print('Connection successful')
    except Error as connect_error:
        print(f'Error: {connect_error}')
    return connect_db


conn = connect(config["mysql"]["host"],
               config["mysql"]["port"],
               config["mysql"]["user"],
               config["mysql"]["password"],
               config["mysql"]["database"])

mycursor = conn.cursor()


def user_authorization(login, password):

    mycursor.execute(
        f"SELECT COUNT(*) FROM users WHERE user_name = '{login}' AND user_password = '{password}'")
    result = mycursor.fetchone()
    result = result[0]
    return result


def user_roles(login):
    mycursor.execute(
        f'SELECT user_role FROM users WHERE user_name = "{login}"')
    role = mycursor.fetchone()
    role = role[0]
    return role
