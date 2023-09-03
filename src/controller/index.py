import pandas as pd
import json
import requests
import openai
import os
from dotenv import load_dotenv
load_dotenv()

# Etapa de Extract: Extração de dados do Monday.com utilizando GraphQL
# Nessa etapa foram extraídos dados de um único Board
# Foram coletadas apenas informações importantes para esse projeto, estas informações estão representadas na linha 15 na variável query_to_get 
access_token = os.getenv("ACCESS_TOKEN")
id_board = os.getenv("ID_BOARD")
api_key = os.getenv("API_KEY")

URL_MONDAY = "https://api.monday.com/v2/"
headers = {"Authorization" : access_token}
query_to_get = '{boards(ids:'+id_board+') { name id groups {id title} items {id name column_values { id text }}}}'
data = {'query' : query_to_get}     

# Função responsável por realizar uma coleta de dados no Monday.com
def get_datas_monday():
    response = requests.post(url=URL_MONDAY, json=data, headers=headers)
    values = response.json() if response.status_code == 200 else None
    return values['data']['boards'][0] if values else None

values_monday = get_datas_monday()

# Guarda as informações úteis dentro de uma lista
datas_to_msg = []
for value in values_monday['items']:
    datas_to_msg.append(value)

# Etapa de Transform: Transformar esses dados em algo com OpenAI
def get_people():
    people=[]
    for item in datas_to_msg:
        name, ref, value, message = "","",0,""
        for column in item["column_values"]:
            if column["text"] == "Pendente":
                name = item["name"]
        for column in item["column_values"]:
            if(column["id"] == "texto3"):
                ref = column["text"]
        for column in item["column_values"]:
            if(column["id"] == "n_meros"):
                value = column["text"]
        people.append([name, ref, value, message]) if name != "" and ref != "" and value != 0 else None
    return people

openai.api_key = api_key

def generate_message(person):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system", 
        "content": "Você é um especialista em cobranças."
      },
      {
        "role": "user", 
        "content": f"Cria uma mensagem de cobrança para {person[0]} no valor de {int(person[2])} reais referente a {person[1]} com no máximo 300 caracteres"
      }
    ]
  )
  return completion.choices[0].message.content

people = get_people()
for person in people:
    message = generate_message(person)
    person[3] = message


# Load: PUT desses dados modificados
# Os dados serão salvos em um CSV 
def create_csv():
    arr_name=[]
    arr_values=[]
    arr_refs=[]
    arr_msgs=[]
    for person in people :
        arr_name.append(person[0]) 
        arr_values.append(person[2])
        arr_refs.append(person[1])
        arr_msgs.append(person[3])
    return f'"Nomes": {arr_name}, "Valores": {arr_values}, "Referência": {arr_refs}, "Mensagens": {arr_msgs}'

arr_csv = create_csv()
arr_csv = "{"+arr_csv.replace("'",'"')+"}"
csv_data = json.loads(arr_csv)
df = pd.DataFrame(csv_data)
df.to_csv("CSV_with_messages_to_clients.csv")

create_csv()