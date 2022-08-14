def is_correct_number(num, radix, alphabet):
    for i in num:
        if i not in alphabet:
            return False
    return True


def is_correct_radix(radix):
    if radix.isdigit() and 2 <= int(radix) <= 16:
        return True
    return False

def convert_to_10(num, radix, alphabet):
    ans = 0
    num = num[::-1]
    for i in range(len(num)):
        ans += int(alphabet.index(num[i])) * (radix ** i)
    return ans

def convert_from_10(num, radix, alphabet):
    ans = ""
    while num >= radix:
        ans += alphabet[num % radix]
        num //= radix
    ans += alphabet[num]
    return ans[::-1]

again = "Y"
alphabet_of_systems = "0123456789ABCDEF"

while again.upper() == "Y":
    print("For this calculator max radix is 16")
    num_radix = input("Type number radix: ").strip()
    while not is_correct_radix(num_radix):
        num_radix = input("Type correct radix: ").strip()
    num_radix = int(num_radix)

    num = input("Type number: ").strip().upper()
    while not is_correct_number(num, num_radix, alphabet_of_systems[:num_radix]):
        num = input("Type coorect number: ").strip().upper()

    in_what_radix = input("Type in what radix should I calculate number: ").strip()
    while not is_correct_radix(in_what_radix) and in_what_radix != str(num_radix):
        in_what_radix = input("Type coorect radix: ").strip()
    in_what_radix = int(in_what_radix)

    alphabet_of_system1 = alphabet_of_systems[:num_radix]
    alphabet_of_system2 = alphabet_of_systems[:in_what_radix]

    if in_what_radix == 10:
        print(convert_to_10(num, num_radix, alphabet_of_system1))
    elif num_radix == 10:
        print(convert_from_10(int(num), in_what_radix, alphabet_of_system2))
    else:
        print(convert_from_10(convert_to_10(num, num_radix, alphabet_of_system1), in_what_radix,  alphabet_of_system2))
    again = input("Do you close this program (type Y or N): ").strip().upper()
    while again != "Y" and again != "N":
        again = input("Type Y or N: ").strip().upper()