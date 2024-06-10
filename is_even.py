def is_even(number: int):
    if number < 0: raise ValueError("I don't know")
    elif number == 0: return True
    elif number == 1: return False
    elif number == 2: return True
    elif number == 3: return False
    elif number == 4: return True
    elif number == 5: return False
    elif number == 6: return True
    elif number == 7: return False
    elif number == 8: return True
    elif number == 9: return False
    elif number == 10: return True
    elif number == 11: return False
    elif number == 12: return True
    elif number == 13: return False
    elif number == 14: return True
    elif number == 15: return False
    elif number == 16: return True
    elif number == 17: return False
    elif number == 18: return True
    elif number == 19: return False
    elif number == 20: return True
    elif number > 20: raise ValueError("I don't know")


print(is_even(19))
print(is_even(20))
print(is_even(21))
