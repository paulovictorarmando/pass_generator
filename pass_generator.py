import string as s
import random

def generator(_size:int) -> str:
    _size = 10 if _size < 10 else _size
    print(_size)
    _word:list = []
    _key:str = s.ascii_letters + s.digits + s.punctuation
    for i in range(_size):
        _word.append(random.choice(_key))
    _word = ''.join(_word)
    return _word