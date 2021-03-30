"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

import hashlib
from uuid import uuid4

salt = uuid4().hex
cached_adr = {}


def url_into_cache(url):
    if cached_adr.get(url) != None:
        print("Already into cache")
    else:
        hash_adr_res = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
        cached_adr[url] = hash_adr_res
        print('Adress {} was inserted into cache: {}'.format(url,cached_adr[url]))



url_into_cache("www.ya.ru")
url_into_cache("www.google.com")
url_into_cache("www.ya.ru")
url_into_cache("www.vk.com")
url_into_cache("www.microsoft.com")
