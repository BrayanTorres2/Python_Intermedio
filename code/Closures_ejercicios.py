#hola 3 ->holaholahola
def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Sólo puedes utilizar cadenas"
        return string*n
    return repeater

def divisor(coc):
    assert type(coc) == int, "Sólo puedes utilizar enteros"
    def dividendo(div):
        assert type(div) == int, "Sólo puedes utilizar enteros"
        return div/coc
    return dividendo

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola "))
    div_by_5 = divisor(5)
    print(div_by_5(100))

if __name__=="__main__":
    run()
