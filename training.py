import json

# JSON строка
json_string = '''
{
  "имя": "Анна",
  "возраст": 25,
  "город": "Москва",
  "знания": ["Python", "JavaScript", "SQL"]
}
'''

# Чтение JSON и преобразование в объект Python
data = json.loads(json_string)
print(data["имя"])
print(data["возраст"])