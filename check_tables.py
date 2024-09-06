import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('instance/mydatabase.db')

# Создаем курсор
cursor = conn.cursor()

# Выполняем команду для отображения всех таблиц
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Выводим результат
tables = cursor.fetchall()
print(tables)

# Закрываем соединение
conn.close()
