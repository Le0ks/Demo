# здесь не предусмотрена защита от дурака
from string import *
from random import choice

def generate_passwords(length, chars):
	password = ""
	for _ in range(length):
		password += choice(chars)
	return password

chars = ""
n = int(input('Введите количество паролей для генерации: '))
length = int(input('Введите длину пароля: '))
add_digit = input('Включить цифры? (Y / N) ').strip()
add_lowercase = input('Включить прописные буквы? (Y / N) ').strip()
add_uppercase = input('Включить строчные буквы? (Y / N) ').strip()
add_punctuation = input('Включить символы, такие как !#$%&*+-=?@^_? (Y / N) ').strip()
remove_badsymbols = input('Исключить символы il1Lo0O? (Y / N) ').strip()

if add_digit.upper() == 'Y':
    chars += digits
if add_lowercase.upper() == 'Y':
    chars += ascii_lowercase
if add_uppercase.upper() == 'Y':
    chars += ascii_uppercase
if add_punctuation.upper() == 'Y':
    chars += '!#$%&*+-=?@^_'
if remove_badsymbols.upper() == 'Y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

for _ in range(n):
	print(generate_passwords(length, chars))