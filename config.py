# host = '0.0.0.0'
# port = 5000
# conn_str = 'mysql+mysqlconnector://root:root@localhost/onEntreeDB'


import os

# Use a variável de ambiente HOST
host = os.getenv("HOST", "0.0.0.0")

# Use a variável de ambiente PORT
port = int(os.getenv("PORT", 5001))

# Use a variável de ambiente DATABASE_URL para se conectar ao banco de dados
conn_str = os.getenv("DATABASE_URL")