class cifradoVigenere():

    def __init__(self, alfabeto, mensaje, clave):

        __alfabeto = []
        __mensaje = ""
        __clave = ""
        __matriz = []

        self.setalfabeto(alfabeto)
        self.llenarMatriz(self.getalfabeto())
        self.setmensaje(mensaje)
        self.setclave(clave)

        self.setmensaje(self.filtradoMsgOriginal(self.getmensaje()))

    def setalfabeto(self, alfabeto):
        self.__alfabeto = alfabeto

    def getalfabeto(self):
        return self.__alfabeto

    def setmensaje(self, mensaje):
        self.__mensaje = mensaje

    def getmensaje(self):
        return self.__mensaje

    def setmatriz(self, matriz):
        self.__matriz = matriz

    def getmatriz(self):
        return self.__matriz

    def setclave(self, clave):
        self.__clave = clave

    def getclave(self):
        return self.__clave

    def llenarMatriz(self, alfabeto):
        matriz = []
        for i in range(0, len(alfabeto)):
            matriz.append([])
            for j in range(0, len(alfabeto)):
                if j+i < len(alfabeto):
                    matriz[i].append(alfabeto[j+i])
                else:
                    for k in range(0, i):
                        matriz[i].append(alfabeto[k])

        self.setmatriz(matriz)

    def filtradoMsgOriginal(self, msg):
        msg = msg.lower()
        msg = msg.replace(" ", "")
        # al alfabeto no contempla los acentos
        msg = msg.replace("á", "a")
        msg = msg.replace("é", "e")
        msg = msg.replace("í", "i")
        msg = msg.replace("ó", "o")
        msg = msg.replace("ú", "u")

        return msg

    def lista_palabra_clave(self, clave):
        # numero de veces que vamos a repetir la palabra clave pe: v e r d e v e r d e
        # la cantidad a abarcar es 27 que es la longitud del alfabeto esp
        no_repeticiones = (len(self.getmensaje())/len(clave))+0.5
        no_repeticiones = round(no_repeticiones)
        lista_palabra_clave = no_repeticiones*clave

        return list(lista_palabra_clave)

    def cifrarletra(self, pos_letra_clave, pos_letra_texto):
        letra_cifrada = self.getmatriz()[pos_letra_clave][pos_letra_texto]
        return letra_cifrada

    def mensajeCifrado(self):

        # la condicion nos sirve para evitar elementos que no se encuentren en el alfabeto por ejemplo \n , . : ; etc
        texto_cifrado = []
        lista_palabra_clave = self.lista_palabra_clave(self.getclave())
        alfabeto = self.getalfabeto()

        for i in range(0, len(self.getmensaje())):

            if self.getmensaje()[i] in alfabeto:
                pos_letra_clave = alfabeto.index(lista_palabra_clave[i])
                pos_letra_texto = alfabeto.index(self.getmensaje()[i])
                letra_cifrada = self.cifrarletra(
                    pos_letra_clave, pos_letra_texto)
                texto_cifrado.append(letra_cifrada)
            else:
                texto_cifrado.append(" ")

        texto_cifrado = "".join(texto_cifrado)
        return texto_cifrado


ruta = r"./manual.txt"
archivo = open(ruta, "r", encoding="utf8")
msg = archivo.read()
palabra_clave = "verde"
alfabeto_esp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
m = cifradoVigenere(alfabeto_esp, msg, palabra_clave)
