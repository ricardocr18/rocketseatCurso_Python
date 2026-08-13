from sqlite3 import Connection


class UserRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_user(self, username: str, password: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO users (username, password, balance) 
            VALUES (?, ?, ?);
            ''', (username, password, 0)
        )
        self.__conn.commit()