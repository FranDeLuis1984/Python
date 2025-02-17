""" EJERCICIO PARA APLICAR LA LLAMADA A LA FUNCIÓN MAIN DESDE OTRA FUNCIÓN SECUNDARIA"""

def main():
    print ("La abadía del crimen es un juego programado por Paco Menéndez y con Juan DelCán a cargo de los gráficos")

    funcion_secundaria()

def funcion_secundaria():
    print ("La abadía del crimen es el mejor juego de la era dorada del software Español")

if __name__ == '__main__': 
    main()