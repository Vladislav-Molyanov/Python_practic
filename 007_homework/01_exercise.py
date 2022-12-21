'''Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.'''

print('МЕНЮ.\n'
'1. Создание справочника.\n'
'2. Экспорт данных в справочник.\n'
'3. Импорт данных из справочника.\n'
'4. Вывод справочника.\n'
'0. Выход из программы.')
phonebook = {'full_name': [], 'phone': [], 'date_of_birth': []}
key = ''
while key != '0':
    key = input('Выберите пункт меню: ')
    match key:
        case '1':
            name = input('Введите ФИО: ')
            phone = input('Введите номер телефона: ')
            date = input('Введите дату рождения: ')
            phonebook['full_name'].append(name)
            phonebook['phone'].append(phone)
            phonebook['date_of_birth'].append(date)
        case '2':
            file = input('Введите файл, куда необходимо сохранить данные: ')
            with open(file, 'w', encoding='cp1251') as f:
                f.write('№;ФИО;Номер телефона;Дата рождения\n')
                i = 1
            for fio, ph, dob in zip(phonebook['full_name'], phonebook['phone'], phonebook['date_of_birth']):
                f.write(f'{i};{fio};{ph};{dob}\n')
                i += 1
        case '3':
            file = input('Введите файл, откуда необходимо считать данные: ')
            with open(file, 'r', encoding='cp1251') as f:
                for line in f.readlines():
                    if line[:-1] == '№;ФИО;Номер телефона;Дата рождения':
                        continue
                    else:
                        data = line[:-1].split(';')
                        phonebook['full_name'].append(data[1])
                        phonebook['phone'].append(data[2])
                        phonebook['date_of_birth'].append(data[3])
        case '4':
            print('Данные справочника.')
            i = 1
            for fio, ph, dob in zip(phonebook['full_name'], phonebook['phone'], phonebook['date_of_birth']):
                print(f'{i}. ФИО: {fio}. Телефон: {ph}. Дата рождения: {dob}')
            i += 1
        case '0':
            print('Завершение работы программы.')
        case _:
            print('Введен неверный пункт меню! Выберите пункт меню 0-4.')