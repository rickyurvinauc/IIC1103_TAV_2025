def tareas_sobre_k(t,k):
   if len(t) == 0:
      return []
   estudiante = t[0]
   notas = estudiante[2]
   promedio = sum(notas)/len(notas)
   if promedio > k:
      return [estudiante[0]] + tareas_sobre_k(t[1:],k)
   else:
      return tareas_sobre_k(t[1:],k)