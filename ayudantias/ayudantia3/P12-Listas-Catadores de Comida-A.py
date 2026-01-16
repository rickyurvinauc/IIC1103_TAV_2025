
def mas_delicioso(cursos, estudiantes):
    #inicializar variables para almacenar el curso mas delicioso y el maximo de aprobaciones
    curso_mas_deli = ""
    max_aprobaciones = -1
    #recorrer cada curso en la lista de cursos
    for curso in cursos:
        #inicializar contador de aprobaciones para el curso actual
        contador = 0
        #recorrer cada estudiante en la lista de estudiantes
        #en realidad esa lista tiene los cursos aprobados por cada estudiante
        for e in estudiantes:
            #si el curso aprobado por el estudiante es igual al curso actual
            if curso in e:
                contador += 1
        #verificar si el contador de aprobaciones del curso actual es mayor que el maximo registrado
        if contador > max_aprobaciones:
            #actualizo el curso mas delicioso y el maximo de aprobaciones
            max_aprobaciones = contador
            curso_mas_deli = curso
    return [curso_mas_deli, max_aprobaciones]

#######################

def mas_delicioso(cursos, estudiantes):
    #string vacio 
    delicioso = ""
    # recorrer todos los cursos que aprobaron los estudiantes
    for e in estudiantes:
        # concatenar los cursos aprobados por cada estudiante
        delicioso += e
    
    # inicializar el curso mas delicioso con el primer curso de la lista
    curso_mas_deli = cursos[0]
    # contar aprobaciones del curso inicial
    aprobaciones = delicioso.count(curso_mas_deli)

    #recorriendo la lista de cursos
    for c in cursos:
        #contar cuantas veces aparece el curso en la cadena delicioso
        conteo = delicioso.count(c)
        # revisar cuantas aprobaciones tiene el curso c
        if conteo > aprobaciones:
            # si es que sus aprobacion es mayor que la del curso inicial, lo reemplazo
            curso_mas_deli = c
            aprobaciones = conteo
    return [curso_mas_deli, aprobaciones]

#######################

def mas_delicioso(cursos, estudiantes):
    # crear una lista para contar las aprobaciones de cada curso
    # una lista con puros 0s del mismo tamaño que la lista de cursos
    conteos = [0] * len(cursos)

    # recorrer cada estudiante en la lista de estudiantes
    for e in estudiantes:
        # recorrer cada curso y su indice en la lista de cursos
        for i in range(len(cursos)):
            # si el curso esta en la lista de cursos aprobados por el estudiante
            if cursos[i] in e:
                # sumo 1 en su respectivo indice en la lista de conteos
                conteos[i] += 1

    # inicializar variables para encontrar el curso con mas aprobaciones
    max_aprobaciones = conteos[0]
    indice_max = 0

    # verificar si algun curso tiene mas aprobaciones que el maximo actual
    for i in range(len(conteos)):
        if conteos[i] > max_aprobaciones:
            max_aprobaciones = conteos[i]
            indice_max = i

    return [cursos[indice_max], max_aprobaciones]
