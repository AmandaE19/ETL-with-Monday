# import os
import pandas as pd
import json
# from dotenv import load_dotenv
# load_dotenv()

people = [["amanda","botaão",123,"mensagem 0"],["amanda","bala",314,"mensagem 1"],["ana","bota",131,"mensagem 2"],["angela","bota",232,"mensagem 3"]]
# people_str = str(people).replace("[[",""person':[").replace("]]","]")
# print(people_str)


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
df.to_csv("teste3.csv")
