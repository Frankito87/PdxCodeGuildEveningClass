import csv

def load_phonebook():
    with open('phonebook.csv', newline='') as csvfile:
        phonebook = csv.reader(csvfile, delimiter=',')

        for row in list(phonebook) [1:]:
            print(', '.join(row))

load_phonebook()


def save_phonebook(dct):
    with open('phonebook.csv', 'w', newline='') as  csvfile:
        phone_writter = csv.writer(csvfile, delimiter=',')
        phone_writter.writerow(['id','name','number'])

        for id, entry in dct.items():
            phone_writter.writerow([id, entry['name'], entry['number']])
