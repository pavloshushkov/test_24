import requests

url = 'https://www.magetic.com/c/test?api=1&name=pavlo_shushkov'
games_store = {}

separator = ';'
response_block_list = ['Error 501', ]


def update_store(value: str):
    if value:
        store = games_store.get(value, 0)
        games_store.update({value: store + 1})


def request(url_path: str):
    r = requests.get(url_path)
    content = r.content.decode("utf-8")
    if r.status_code != 200 or any(x for x in response_block_list if content.find(x) != -1):
        return False, ''
    return True, content.split(separator)


def start():
    status, values = request(url_path=url)
    if status:
        for v in values:
            update_store(v)


def runner(number_repeats=2):
    while number_repeats >= max(games_store.values()) if games_store else True:
        start()
    print(games_store)


runner(number_repeats=10)
