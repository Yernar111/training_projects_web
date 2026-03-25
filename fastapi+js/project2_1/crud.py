# Работа с базой данных
def create_user(cur, user):
    query = "insert into users(name, password) values(%s, %s) returning *" # Получить измененную/вставленную строку полностью
    cur.execute(query, (user.name, user.password))
    return cur.fetchone() # Получение первой строки результата выполнения SQL запроса

def get_users(cur):
    query = "select * from users" # При select не требуется returning *
    cur.execute(query)
    return cur.fetchall()

def get_user(cur, name: str):
    query = "select * from users where name = %s"
    cur.execute(query, (name,)) # Требуется запятая для гарантии что это кортеж
    return cur.fetchone()
