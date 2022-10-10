def creating():
    file = 'Phonebook.csv'
    with open(file, 'w') as data:
        data.write(f'Фамилия; Имя; Номер телефона; Описание')