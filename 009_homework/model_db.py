import sqlite3


def connect():
    global conn, cursor
    conn = sqlite3.connect('my_phone_book.db')
    cursor = conn.cursor()


def disconnect():
    conn.commit()
    conn.close()


def all(update, context):
    cursor.execute("select * from persons")
    results = cursor.fetchall()
    update.message.reply_text(''.join([str(element) for element in results]))


def find_abonent(update, context):
    fl = 0
    name = update.message.text
    if name != name.title():
        update.message.reply_text('Введите фамилию с заглавной буквы!')
        name = update.message.text
    elif name == name.title():
        cursor.execute(f"select last_name from persons")
        results = cursor.fetchall()
        for elements in results:
            if name in elements:
                cursor.execute(f"select * from persons where last_name like '%{name}%'")
                result = cursor.fetchall()
                fl = 1
                update.message.reply_text(''.join([str(element) for element in result]))
    if fl == 0:
        update.message.reply_text("Контакт не найден")


def add_abonent(update, context):
    flag = 0
    first_name, last_name, number = update.message.text.split(' ')
    cursor.execute("select * from persons")
    results = cursor.fetchall()
    for el in results:
        if int(number) in el:
            update.message.reply_text("Такой номер уже существует!")
            flag = 1
            break
    if flag != 1:
        cursor.execute(
            f"insert into persons (first_name, last_name, number) "
            f"values ('{first_name}', '{last_name}', {number})")
        update.message.reply_text("Контакт добавлен")
    conn.commit()


def update_info(update, context):
    sername, phone = update.message.text.split(' ')
    cursor.execute(
        f"update persons set number={phone} where last_name='{sername}'"
    )
    update.message.reply_text("Изменения внесены")
    conn.commit()

def delete_abonent(update, context):
    first_name = update.message.text
    cursor.execute(
        f"delete from persons where last_name='{first_name}'"
    )
    update.message.reply_text("Контакт удален")
    conn.commit()
