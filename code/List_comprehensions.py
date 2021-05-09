def run():
    #lista=[]
    #for i in range(1,101):
    #    if(i%3!=0):
    #        lista.append(i**2)
    lista=[i**2 for i in range(1,101) if i%3 !=0]
    #[element for elemento in irable if condicion]
    lista2=[i for i in range(1,9999) if(i%4==0 and (i%6==0 and i%9==0)) ]

    print(lista)

if __name__ =="__main__":
    run()