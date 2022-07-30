from random import randint

def is_valid_input_num(n):
	if n.isdigit():
		n = int(n)
		return True if 1 <= n <= t else False
	return False

def is_valid_t(t):
	if t.isdigit():
		t = int(t)
		return True if t > 1 else False
	return False

def is_valid_q(q):
	return True if q == "Y" or q == "N" else False

print("Добро пожаловать в числовую угадайку")
q = "Y"

while q == "Y":
	t = input("\nВведите правую границу для случайного выбора числа (>1): ")
	if not is_valid_t(t):
		print("\nЧисло должно быть больше 1.")
		continue
	t = int(t)
	x = randint(1, t)
	s = 0
	while True:
		n = input(f"\nВведите число от 1 до {t}: ")
		if not is_valid_input_num(n):
			print(f"\nА может быть все-таки введем целое число от 1 до {t}?")
			continue
		n = int(n)
		if n == x:
			z = "попытку" if s + 1 == 1 else "попытки"
			print(f"\nВы угадали, поздравляем! Вы использовали {s + 1} {z}.\n")
			break
		elif n > x:
			print("\nВаше число больше загаданного, попробуйте еще разок")
			s += 1
		else:
			print("\nВаше число меньше загаданного, попробуйте еще разок")
			s += 1
	q = input("Хотите ли вы сыграть ещё?(Y/N) ")
	while not is_valid_q(q):
		q = input("\nВведите Y или N: ")

print("\nСпасибо, что играли в числовую угадайку. Ещё увидимся...")