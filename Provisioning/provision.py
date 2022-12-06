from datetime import date
import os
import shutil
from aocd import get_data
import requests
import lxml.html

def check_date(date):
    year = date.strftime('%Y')

    if int(date.strftime('%m').lstrip('0')) < 12:
        days_left = (date(int(year), 12, 1) - date).days
        raise Exception('Advent of Code {year} has not started yet, come back in {days} days.'.format(
            year = year,
            days = days_left
        ))
    elif int(date.strftime('%d').lstrip('0')) > 24:
        raise Exception('Advent of Code {year} has finished, come back next year.'.format(
            year = year
        ))

def create_folder(date):
    folder = get_folder(date)
    if not os.path.isdir(folder):
        os.makedirs(folder)
        shutil.copyfile('solution.py.template', folder + '/solution.py')

def get_folder(date):
    return os.path.abspath(''.join((os.getcwd(), '/../', 'Day ' + date.strftime('%d').lstrip('0'))))

def add_input(date):
    year = date.strftime('%Y')
    day = date.strftime('%d').lstrip('0')
    file = get_folder(date) + '/input.txt'
    with open(file, 'w') as f:
        f.write(get_data(day = int(day), year = int(year)))

def add_sample(date):
    url = 'https://adventofcode.com/{year}/day/{day}'.format(
        year = date.strftime('%Y'),
        day = date.strftime('%d').lstrip('0')
    )

    token = open('token').read().strip()
    cookies = {'session': token}
    response = requests.get(url, cookies = cookies)
    xml = lxml.html.fromstring(response.text)
    sample = xml.xpath('//pre/code[not(*)][1]')
    file = get_folder(date) + '/sample.txt'
    with open(file, 'w') as f:
        f.write(sample[0].text)

if __name__ == '__main__':
    try:
        today = date.today()
        check_date(today)

        print('Provisioning Advent of Code {year}, day {day}...'.format(
            year = today.strftime('%Y'),
            day = today.strftime('%d').lstrip('0')
        ))

        create_folder(today)
        add_sample(today)
        add_input(today)

        print('Done!')
    except Exception as e:
        print(e)
