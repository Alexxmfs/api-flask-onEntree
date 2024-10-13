# host = '0.0.0.0'
# port = 5000
# conn_str = 'mysql+mysqlconnector://root:root@localhost/onEntreeDB'


import os

host = '0.0.0.0'
port = 5000

# Use a variável de ambiente DATABASE_URL para se conectar ao banco de dados do Render
conn_str = os.getenv("DATABASE_URL")