def palindrome(string):
    try:
        palindrome = string == string [::-1]
    except TypeError:
        print(f"No puedes utilizar números, {string} es un número. ")        
    else:
        if palindrome == True:
            print(f"'{string}' es un palíndromo!")
        elif palindrome == False:
            print(f"'{string}' no es un palíndromo.")
def divisors(num):
    try:
        if num < 0:
            raise ValueError("No se aceptan números negativos")
    except ValueError as ve:
        return ve
    return [i for i in range(1, num + 1) if num % i == 0]

def run():

    num = int(input('Ingresa un número: '))
    print(divisors(num))
    print(palindrome("ana"))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()

