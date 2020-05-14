import sqlite3

def main():
    conn = sqlite3.connect("db.sqlite3") # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    '''
    # Создание таблицы
    cursor.execute("""CREATE TABLE test
                      (t1 number, t2 number, t3 number)
                   """)
    '''
    arr1 = ['Товары для детей', 'Товары для дома', 'Товары для офиса', 'Товары для дачи', 'Товары для сада', 'Товары для огорода', 'Товары для самых маленьких', 'Товары для всей семьи', 'Женская одежда', 'Мужская одежда', 'Детсткая одежда', 'Аксессуары', 'Разное', 'Разнообразное', 'Совсем разное', 'Игрушки', 'Мебель', 'Техника', 'Канцелярия', 'Товары для школы', 'Товары для офиса', 'Товары для всей семьи']

    for i in range(3, 50):
        s = str(i) + ", " + str(i) + ", 2"
        s = """INSERT INTO auth_user
            VALUES (""" + s + """)"""
        # Вставляем данные в таблицу
        cursor.execute(s)
        # Сохраняем изменения
        conn.commit()

if __name__ == "__main__":
    main()



'''
#добавление стран - доставщиков в бд
pip install pycountry
python manage.py oscar_populate_countries
'''