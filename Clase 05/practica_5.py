#####################################################################################################
# IDEA PRINCIPAL: DEFINO UNA CLASE JUEGO A LA CUAL LE ATRIBUYO 2 PARAMETROS, 1 VA A CONDICIONAR AL OTRO
# PARA VER EL PUNTAJE QUE SACASTE EN ESE JUEGO
#####################################################################################################

import random


class juego():
    def __init__(self):
    #####################################################################################################
    # FUNCION INIT PARA ALMACENAR LOS NUMEROS DE LAS VARIABLES RANDOM EN UNA LISTA
    #####################################################################################################    

        self.__list = []

    def num_random(self):
    #####################################################################################################
    # FUNCION PARA GENERAR UN NUMERO RANDOM
    #####################################################################################################

        return random.randint(1,21)

    def push(self):
    #####################################################################################################
    # FUNCION PARA CALLEAR EL NUMERO RANDOM Y AGREGARLO A LA LISTA
    #####################################################################################################

        a = self.num_random()
        print(a)
        self.__list.append(a)
        print(self.__list)

    def funcion_calculadora(self):
    #####################################################################################################
    # FUNCION QUE SE ENCARGA DE SUMAR LOS NUMEROS DE LA LISTA
    #####################################################################################################
        resultado = 0
        for i in self.__list:
            resultado+=i

        return resultado

    def jogo_bonito(self):
    #####################################################################################################
    # FUNCION QUE SE ENCARGA DE VINCULAR TODAS LAS FUNCIONES
    #####################################################################################################

        print('Juego de apuestas:\n\n')
        entrada = input('Que desea hacer:\n\tObtener numero (s)\n\tTerminar apuesta (n)')
        if entrada.lower() == 's':
            self.push()
        
        else:
            return self.ejecutora()
    
        while self.funcion_calculadora()<50:

            entrada = input('Que desea hacer:\n\tObtener numero (s)\n\tTerminar apuesta (n)')
            if entrada.lower() == 's':
                self.push()

            else:
                break

        return self.ejecutora()
    
    def ejecutora(self):
        #####################################################################################################
        # FUCION QUE SE ENCARGA DE DEFINIR LA CANTIDAD DE PUNTOS QUE SACO EN EL JUEGO
        #####################################################################################################
        result=0
        if self.funcion_calculadora()>50:
            return print('Usted sacò 0 puntos su numero supero los 50 puntos')

        if self.funcion_calculadora()==50:
            return print('Felicidades usted saco blackjack')
        else:
            result = self.funcion_calculadora()
            return print(('Usted obtuvo {} puntos').format(result))


if __name__ == '__main__':
    s = juego()
    s.jogo_bonito()