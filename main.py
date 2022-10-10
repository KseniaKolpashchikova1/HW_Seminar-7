from logging.config import valid_ident
from os.path import exists
from creating import creating
from writing import writing_csv
from writing import writing_txt

path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_csv()
writing_txt ()