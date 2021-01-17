# Importar pacotes necessarios
from time import sleep
from whatsapp_api import WhatsApp
import pandas as pd


# Inicializar o whatsapp
wp = WhatsApp()

# Esperar que enter seja pressionado
input("Pressione enter apos escanear o QR Code")

# Lista de nomes ou nomeros de telefone a serem pesquisados
# IMPORTANTE: O nome deve ser nao ambiguo pois ele retornara o primeiro resultado
df = pd.read_excel(r'C:\Users\marco\Documents\Cursos Udemy\Python - boot Whatsapp\whatsapp_api-master\Contatos_marcos.xlsx', sheet_name='familia')

df.head()
df['Nome']

type(df['Nome'])

list(df['Nome'])

nomes_palavras_chaves = list(df['Nome'])

lista_mensagens = list(df['Mensagem'])

# Loop para mandar mensagens para as pessoas da lista
for nome_pesquisar, mensagem in zip(nomes_palavras_chaves, lista_mensagens):
      
    # Pesquisar pelo contato e esperar um pouco
    wp.search_contact(nome_pesquisar)
    sleep(2)
      
    # Enviar mensagem
    wp.send_message(mensagem)

# Esperar 10 segundos e fechar
sleep(10)
wp.driver.close()