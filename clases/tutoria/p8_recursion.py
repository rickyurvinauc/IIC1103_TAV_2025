def impariestos_rec(a, dias):
    #ver si es impariesto
    año_impariesto = False
    if a%5 == 0 or a%7==0:
        print("a", a)
        dias_año_impariesto = 390
        año_impariesto = True
    else:
        dias_año_normal = 360
        año_impariesto = False

    if año_impariesto:
        if dias>dias_año_impariesto:
            resto = dias - dias_año_impariesto
            return impariestos_rec(a+1,resto)
        else:
            return a

    elif not año_impariesto:
        if dias>dias_año_normal:
            resto = dias -dias_año_normal
            return impariestos_rec(a+1,resto)
        else:
            return a
        
# Cortesia de Catalina :D 
# a mi no me salio, no me hubiera sacado 7 D: jejeje