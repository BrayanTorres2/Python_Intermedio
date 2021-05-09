def dict_compre():
    dict_cubo = {num: num**3 for num in range(1, 101) if num % 3  != 0}

    print(dict_cubo)


def challenge_root():
    raiz = 1/2
    dict_root = {num: num**raiz for num in range(1, 1001)}

    print(dict_root)


if __name__ == "__main__":
    dict_compre()
    challenge_root()