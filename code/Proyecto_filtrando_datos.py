DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def run():
    """ los nombres de los programadores que utilizan python como lenguaje dominate """
    all_python_devs = [worker["name"]for worker in DATA if worker['language'] == 'python']#comprension de listas
    all_python_devs1 = list(filter(lambda worker: worker['language'] == 'python', DATA))#utilizando filter
    all_python_devs2 = list(map(lambda worker: worker['name'], all_python_devs1))#Utilizando map
    #print(all_python_devs2)
    """Nombre de todos los trabajadores que trabajan en Platzi"""
    all_platzy_workers = [worker['name']for worker in DATA if worker['organization'] == 'Platzi']#compresion de listas
    all_platzy_workers = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))#utilizando filter
    all_platzy_workers = list(map(lambda worker: worker['name'], all_platzy_workers))#Utilizando map
    #print(all_platzy_workers)
    """El nombre de las personas que sean mayores de edad nuestro diccionario DATA"""
    adults = list(filter(lambda worker: worker['age'] >= 18, DATA))#Usando Filter
    adults = list(map(lambda worker: worker['name'], adults))#usando map
    adults = [worker['name'] for worker in DATA if worker['age'] >= 18]#comprension de listas
    #print(adults)
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))#con map
    old_people1 = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]# con comprension de listas
    for worker in old_people:
        print(worker)
    print(old_people)    
if __name__ =="__main__":
    run()