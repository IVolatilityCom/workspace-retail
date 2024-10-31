import json
import os
from dotenv import load_dotenv
from tinydb import TinyDB,Query


# Путь к базе данных
db_path = '/Users/manbetov/Documents/Flashpost/flashpostVariable.db'

with open(db_path, "r") as jsonFile:
    data = json.load(jsonFile)
old_json = json.dumps(data)

print('Before Modifying:', old_json)
ivol_api_key = os.getenv('ivolApiKey')
print("Значение ivolApiKey:", ivol_api_key)
if not 'data' in data['collections'][0]['data'][0] or len(data['collections'][0]['data'][0]['data']) == 0:
    data['collections'][0]['data'][0]['data'].append({'isChecked':True, 'key':'ivolApiKey', 'value':ivol_api_key, 'type':'global'})
else:
    data['collections'][0]['data'][0]['data'][0]['value']=ivol_api_key

modified_json = json.dumps(data)
print('After Modifying:', modified_json)

with open(db_path, "w") as jsonFile:
    json.dump(data, jsonFile)


# Вывод структуры базы данных для проверки
print("Структура базы данных:")
with open(db_path) as db_file:
    db_content = json.load(db_file)
    print(json.dumps(db_content, indent=4))


