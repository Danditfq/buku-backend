import psycopg2
#Mesin DB

class Connection:
    def __init__(self):
        self.conn = psycopg2.connect(database="postgres",
                                host="34.128.78.79",
                                user="dandi",
                                password="dandi123",
                                port="5432")
    def getConnection(self):
        return self.conn