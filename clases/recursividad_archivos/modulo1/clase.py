contador=1
punto_T=0
punto_O=0
gane_yo=0
no_gane=0
juego=1
while gane_yo<6 and no_gane<6:
   print("Empezando game", contador)
   while abs(punto_O-punto_T)!=2:
   game=input()
   if game=="T":
      punto_T+=1
   elif game=="O":
      punto_O+=1
   print("Puntaje:", punto_T, "- Puntaje oponente:", punto_O)
   if punto_O-punto_T==2:
      if punto_O>punto_T:
         no_gane+=1
      else:
         gane_yo+=1
         
      print("Puntaje:",punto_T, "- Puntaje oponente:", punto_O)
      contador+=1

if gane_yo==6:
    print("Ganaste este game!")
else:
    print("Tu oponente gano este game...")
print("Games:",gane_yo,"- Games oponente:", no_gane)