import json


secret = json.load(open('config.json', 'r', encoding='utf-8'))
django_config = secret['django_config']