x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15  


estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
estudiantes[0]['last_name'] = 'Bryant'  



directorio_deportes = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol': ['Messi', 'Ronaldo', 'Rooney']
}
directorio_deportes['fútbol'][0] = 'Andrés'  



z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30  


print(x)
print(estudiantes)
print(directorio_deportes)
print(z)


estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(some_list):
    for dictionary in some_list:
        for key, value in dictionary.items():
            print(key, "-", value)
iterateDictionary(estudiantes)



def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])
iterateDictionary2('first_name', estudiantes)
print()  
iterateDictionary2('last_name', estudiantes)



dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(len(value), key.upper())
        for item in value:
            print(item)
        print()
printInfo(dojo)
