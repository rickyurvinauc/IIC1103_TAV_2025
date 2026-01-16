def super_estudiantes(estudiantes, indicados):
    #lista vacia para guardar los indices de los super estudiantes
    super_est = []

    # recorrer la lista de estudiantes por indice
    for i in range(len(estudiantes)):
        # verificar si el estudiante cumple con ser super estudiante
        cumple_super = True
        for curso in indicados:
            # si algun curso del string de cursos indicados no esta en los cursos aprobados del estudiante
            if curso not in estudiantes[i]:
                # el estudiante no cumple con ser super estudiante
                cumple_super = False
        # si el estudiante cumple con ser super estudiante, agregar su indice a la lista
        if cumple_super == True:
            #lo tengo que guardar por indice
            super_est.append(i)

    return super_est

##########################

def super_estudiantes(estudiantes, indicados):
    # inicializar la lista vacia de super estudiantes
    super_est = []
    # variable para llevar el indice del estudiante
    i = 0
    # recorrer la lista de estudiantes
    for estudiante in estudiantes:
        #asumo que cumple 
        cumple = True
        # revisar si el estudiante tiene todos los cursos indicados
        for curso in indicados:
            #si encuentro uno que falta
            if curso not in estudiante:
                #en ese caso estudiante no cumple
                cumple = False
                break
        if cumple == True:
            #guardo el indice del estudiante que cumple
            super_est.append(i)
        #incremento el indice
        i += 1
    #retornar la lista con los indices de los super estudiantes
    return super_est
