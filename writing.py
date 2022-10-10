from asyncore import write
from phonebook_model import get_abonents as ga

info = ga()

def writing_csv():
    file = 'phone_book.csv'
    with open(file, 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]}; {info[1]}; {info[2]}; {info[3]}')

def writing_txt():
    file = 'phone_book.txt'
    with open(file, 'a', encoding = 'utf-8') as data:
       data.write(f'Фамилия: {info[0]} \n\n Имя: {info[1]} \n\nНомер телефона: {info[2]} \n\nОписание: {info[3]}')
