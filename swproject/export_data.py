import os
import sys
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swproject.settings')
django.setup()

# Теперь импортируем Django команды
from django.core.management import call_command
from io import StringIO

# Создаем дамп в памяти
output = StringIO()
call_command('dumpdata', 
             '--natural-foreign', 
             '--natural-primary', 
             '-e', 'contenttypes', 
             '-e', 'auth.Permission',
             stdout=output)

# Сохраняем с явной кодировкой UTF-8
with open('starwars_data.json', 'w', encoding='utf-8') as f:
    f.write(output.getvalue())

print("Данные экспортированы в starwars_data.json")