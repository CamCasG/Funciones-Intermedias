x = [ [5,2,3], [10,8,9] ] 

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]

print(x[1])                                                          #llamo al indíce 1 de la var x 
x[1][0] = 15                                                         # modifico el primer elemento del índice.
print(x[1])                                                          #imprimo para corroborar que el cambio se haya efectuado.
print(estudiantes[0])                                                #llamo al primer indice del diccionario de estudiantes
estudiantes[0]['last_name'] = 'Bryant'                               # modifico el apellido.
print(estudiantes[0])
print(directorio_deportes)
directorio_deportes['fútbol'][0] = 'Andrés'                          # reemplazo Messi x Andrés
print(directorio_deportes)
print(z)                                                             #llamo a la var z
z[0]['y'] = 30                                                       #modifico el número guardado en 'y'
print(z)


estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(call):
    return call                                             

print(iterateDictionary(estudiantes)[0])                            #llamo al primer indice de estudiantes...
print(iterateDictionary(estudiantes)[1])
print(iterateDictionary(estudiantes)[2])
print(iterateDictionary(estudiantes)[3])                           #y así cada índice hasta el último.



# nuevEstudiantes = []
# for name in estudiantes:                                        (1) Para sacar el ejercicio 3 primero pensé en la manera de sacar por separado la información de un diccionario.
#     nuevEstudiantes.append(name.get('first_name'))              (2) se me ocurrió crear una lista nueva que guardara los elementos solicitados con .get
#     print(name.get('first_name'))
# nuev_apellido = []                                              (3) Tuve que crear dos listas nuevas, una para que guardara los nombres y otra los apellidos.
# for apell in estudiantes:                                       (4) Pensé en cómo pasar esta información a una sola función que llamara ambas, por lo que se me ocurrió que un
#     nuev_apellido.append(apell.get('last_name'))                          if & elif sería buena idea.
#     print(apell.get('last_name'))

def iterateDictionary(clave, estudiantes):                         # equivalente a key_name & some_list
    if clave == 'first_name':                                      #si var clave es igual a 'first_name'
        for name in estudiantes:
            print(name.get('first_name'))                          # imprime la información guardada en first_name
    elif clave == 'last_name':                                     # si var clave es igual a 'last_name'
        for name in estudiantes:                                   
            print(name.get('last_name'))                           # imprime la información guardada en last_name

    
iterateDictionary('first_name',estudiantes)
iterateDictionary('last_name',estudiantes)


dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for info in some_dict:
        print(str(len(some_dict[info]))+ " "+ info)             #convertir len(some_dict) que me arrojaría un error de type (ya que me entrega un número entero) a un str 
        for sum in some_dict[info]:                             #va buscando en el diccionario todos los elemeentos dentro de ubicaciones / instructores
            print(sum)                                          #los suma a la salida.

printInfo(dojo)


