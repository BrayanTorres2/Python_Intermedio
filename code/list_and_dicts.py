def run():
    my_list=[1,"Hello", True,4.5]
    my_dict={"firstname":"Brayan","lastname":"torres"}
    super_list=[
        {"firstname":"Brayan","lastname":"torres"},
        {"firstname":"Luis","lastname":"Cobo"},
        {"firstname":"Mariana","lastname":"torres"},
        {"firstname":"Carlos","lastname":"torres"},
    ]
    super_dict = {
        "natural_nums": [1,2,3,4,5,6,7,8],
        "intenger_nums": [-1,-2,0,1,2],
        "numeros_flotantes": [1.0,2.0,3.0,5.0,6.0]
    }
    for key,value in super_dict.items():
        print(key,"-",value)
        
if __name__ =="__main__":
    run()