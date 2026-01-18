def mellizos(estudiantes_sem1, estudiantes_sem2, i):
    resultado = []

    cursos_i_sem1 = estudiantes_sem1[i]
    cursos_i_sem2 = estudiantes_sem2[i]

    for j in range(len(estudiantes_sem1)):
        if j != i:
            comun_sem1 = False
            comun_sem2 = False

            # Revisar semestre 1
            for curso in cursos_i_sem1:
                if curso in estudiantes_sem1[j]:
                    comun_sem1 = True
                    break

            # Revisar semestre 2
            for curso in cursos_i_sem2:
                if curso in estudiantes_sem2[j]:
                    comun_sem2 = True
                    break

            if comun_sem1 and comun_sem2:
                resultado.append(j)

    return resultado
