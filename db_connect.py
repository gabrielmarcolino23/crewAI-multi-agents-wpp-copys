import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# Configurar as informações de conexão
config = {
    'user': os.getenv('DB_ZOPPY_USER'),
    'password': os.getenv('DB_ZOPPY_PASSWORD'),
    'host': os.getenv('DB_READER_HOST'),
    'database': os.getenv('DB_SCHEMA'),
    
}

# Criar a conexão
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("""select mt.parameters, mt.text, c.name from api.MessageTemplates mt
                        join api.MessageTemplateGroups mtg on mt.messageTemplateGroupId=mtg.id
                        join api.Companies c on c.id = mt.companyId
                        where mtg.type='whatsapp'
                        and c.name like '%{companyName}%';""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
    print("Conexão bem-sucedida!")
except mysql.connector.Error as err:
    print(f"Erro ao conectar ao banco de dados: {err}")