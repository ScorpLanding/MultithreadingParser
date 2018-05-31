#Created by ScorpDEv

from bs4 import BeautifulSoup
import requests
import os
import threading

class ParseTh(threading.Thread):
    def __init__(self, url, name):
        threading.Thread.__init__(self)
        self.url = url
        self.name = name

    def run(self):
        handler = requests.get(self.url).content
        soup = BeautifulSoup(handler, 'html.parser')
        with open(self.name +'.txt', 'a') as f:
            f.write(str(soup))
            f.close()
        be = '%s закончил парсинг %s' % (self.name, self.url)
        print(be)

def main(list_urls):
    for item, url in enumerate(list_urls[:-1]):
        name = 'Поток %s' % (item+1)
        thread = ParseTh(url, name)
        thread.start()

if __name__ == '__main__':
    file_url = input('Ссылка на файл:  ')
    list_urls = []
    if os.path.exists(file_url) == True:
        with open(file_url) as urls:
            listaf = urls.readlines()
            for a in range(len(listaf)):
                list_urls.append(listaf[a][:-1])

    main(list_urls)
