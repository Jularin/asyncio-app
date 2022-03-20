from celery import Celery

from time import sleep

from utils import rearrange

app = Celery('celery', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')


@app.task
def reverse_string(string: str):
    sleep(2)
    return string[::-1]


@app.task
def string_permutation(string: str):
    sleep(5)
    l_str = list(string)
    if len(l_str) % 2 == 0:
        return rearrange(l_str, len(l_str))
    else:
        return rearrange(l_str, len(l_str) - 1)


@app.task
def char_multiple(string: str):
    sleep(7)
    result = "".join([char * i for i, char in enumerate(string, 1)])
    return result
