def encrypt(text, step, language):
	answer = ""
	if language == "ru":
		lowercase = rus_lowercase
		uppercase = rus_uppercase
	else:
		lowercase = eng_lowercase
		uppercase = eng_uppercase
	for i in text:
		if not i.isalpha():
			answer += i
			continue
		if i.isupper():
			answer += uppercase[(uppercase.find(i) + step) % len(uppercase)]
		else:
			answer += lowercase[(lowercase.find(i) + step) % len(lowercase)]
	return answer

def decrypt(text, step, language):
	answer = ""
	if language == "ru":
		lowercase = rus_lowercase
		uppercase = rus_uppercase
	else:
		lowercase = eng_lowercase
		uppercase = eng_uppercase
	for i in text:
		if not i.isalpha():
			answer += i
			continue
		if i.isupper():
			answer += uppercase[uppercase.find(i) - step]
		else:
			answer += lowercase[lowercase.find(i) - step]
	return answer

again = "Y"

eng_lowercase = 'abcdefghijklmnopqrstuvwxyz'
eng_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lowercase = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_uppercase = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

while again == "Y" or again == "да":
	language = input("What language should we use: english or russion? (ru/ en) ").strip()
	while language != "ru" and language != "en":
		language = input("Type en or ru: ").strip()
	if language == "en":
		direction = input("What should we do: encrypt or decrypt?(e / d) ").strip()
		while direction != "e" and direction != "d":
			direction = input("Type e or d: ").strip()
		step = input("Choose the step: ").strip()
		while not step.isdigit():
			step = input("Type a number: ").strip()
		step = int(step)
		text = input("Which text should we use: ").strip()
		while text.isspace():
			text = input("Type the ok test: ").strip()
		print(encrypt(text, step, language) if direction == "e" else decrypt(text, step, language))
		again = input("Do you want to continue the program? (Y / N): ").strip()
		while again != "Y" and again != "N":
			again = input("Type Y or N: ").strip()
	else:
		direction = input("Что мы должны сделать: шифровать или дешифровать?(ш / д) ").strip()
		while direction != "ш" and direction != "д":
			direction = input("Напиши ш или д: ").strip()
		step = input("Выбери  шаг: ").strip()
		while not step.isdigit():
			step = input("Напиши число: ").strip()
		step = int(step)
		text = input("Какой текст нужно использовать: ").strip()
		while text.isspace():
			text = input("Напиши нормальный текст: ").strip()
		print(encrypt(text, step, language) if direction == "ш" else decrypt(text, step, language))
		again = input("Продожить работу программы?(да / нет): ").strip()
		while again != "да" and again != "нет":
			again = input("Напиши да или нет: ").strip()