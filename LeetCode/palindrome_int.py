def is_palindrome_int(_integer: int) -> bool :

    if _integer == 0:
        return True
    
    if _integer % 10 == 0 or _integer < 0:
        return False

    _num = _integer
    _rev = 0

    while _num > _rev:
        _rev = int(_rev * 10 + _num % 10)
        _num = int(_num / 10)

    return _num == _rev or _num == _rev / 10

print(is_palindrome_int(19))
print(is_palindrome_int(10))
print(is_palindrome_int(0))
print(is_palindrome_int(101))