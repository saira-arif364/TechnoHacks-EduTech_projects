# 1 Task Solved

import random
alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits='1234567890'
special_char='&@*%'
all_char=alphabets + digits + special_char
passsword_len=12
password=" ".join(random.sample(all_char,passsword_len))
print(password)
