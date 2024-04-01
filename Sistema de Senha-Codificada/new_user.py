listaU = []
listaS = []
resposta = "s"



def novato(var1, var2):
    pw = ""

#        U = (input("novo usuario: "))
#        P = (input("nova senha: "))

    for i in var2:
        pw += str(ord(i))

    listaU.append(var1)
    listaS.append(pw)

#        resposta = input("Continuar? N/S")
        


#    teste = input("Insira um usuario que está procurando: ")

#    if teste in listaU:
#        seila = listaU.index(teste)
#        jeje = listaS[seila]
#        print("Conta existente! posicão ~ ", seila, "\nA senha desse usuario é: ",jeje)