import pandas as pd
import requests 
import json
import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

df = pd.read_csv('SDW2023_Amanda.csv')

user_ids = df['userID'].tolist()

def get_user_by_id(id):
  response = requests.get(f"{sdw2023_api_url}/users/{id}")
  return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if(user := get_user_by_id(id)) is not None]

# print(json.dumps(users, indent=2))

openai.api_key = api_key

def generate_message(user):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system", 
        "content": "Você é um especialista em markting bancário."
      },
      {
        "role": "user", 
        "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
      }
    ]
  )
  return completion.choices[0].message.content

def update_user(user):
  response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
  return True if response.status_code == 200 else False

for user in users:
  news = generate_message(user)
  print(news)
  user['news'].append({
    "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
    "description": news
  })
  success = update_user(user)
  print(f"User {user['name']} updated? {success}!")