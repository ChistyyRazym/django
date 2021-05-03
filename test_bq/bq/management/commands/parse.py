import requests
import os
import sqlite3
import re

from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('link', nargs='+', type=str, help='link')

    def handle(self, *args, **kwargs):
        links = kwargs['link']

        if not 'file.log' in os.listdir():
            x = requests.get(links[0])
            with open('file.log', 'wb') as f:
                    f.write(x.content)
                    f.close()

        with open('file.log', 'r') as f:
            for i in f.read().split('\n'):
                string = re.findall(r'(\d+.\d+.\d+.\d+) (\w+|\-) (\w+|\-) \[(.+)\] '
                                         r'\"(.+)\" (\d+) (\d+) \"(.*)\" \"(.*)\"', i)
                ip = string[0][0] if string else ''
                date = string[0][3] if string else ''
                method = string[0][4].split(' ')[0] if string else ''
                url = string[0][4].split(' ')[1] if string else ''
                status_code = string[0][5] if string else ''
                size = string[0][6] if string else ''
                conn = sqlite3.connect('db.sqlite3')
                cur = conn.cursor()
                sql = """INSERT INTO bq_test_1(ip, date, method, url, status_code, response_size) 
                       VALUES(?, ?, ?, ?, ?, ?);"""
                cur.execute(sql, (ip, date, method, url, status_code, size))
                conn.commit()

