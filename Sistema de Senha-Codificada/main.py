from tkinter import *
import customtkinter
from tkinter.ttk import Button
from new_user import listaS
from new_user import listaU
from new_user import novato


capacete = 0
# Variável de controle para rastrear se a mensagem já foi exibida


def criptografica(passw):
    code=""
    for i in passw:
        code += str(ord(i))

    passw = code
    return passw

#    ka.configure(texto="{cod}")
#    print(" ". join(togra))
def gerenciar(userData, passData):
    X = userData
    Y = passData

    novato(X, Y)
    
    print(listaU)
    print(listaS)


def clique():
    value = email.get()
    passw = senha.get()

    cod = criptografica(passw)

    if value not in listaU:
        error.configure(text="Algo deu errado, tente novamente.", )
        print("erro aqui")

    else:
        posicao = listaU.index(value)
        jeje = listaS[posicao]
        if cod == jeje:
            error.configure(text="Logado com sucesso!")
            print("sucess")
            ka.configure(text=cod)

            win = Toplevel()
            win.geometry('500x500')

            janela.withdraw() # THIS HIDE THE WINDOW


            img = PhotoImage(file="image/bem.png")
            sub = img.subsample(10, 10)
            label1 = Label(win, image=sub)
            label1.image = sub
            label1.grid(row=10)

            Button(win, text='OK', command=lambda: [win.destroy(), voltar()]).grid(row = 5, columnspan = 2)
        else:
            error.configure(text="Senha incorreta")
            print("erro")

def novaConta():
    newC = Toplevel()

    newC.geometry('720x480')

    janela.withdraw() # THIS HIDE THE WINDOW

    texto = customtkinter.CTkLabel(janela, text="Novo Usuario")
    texto.pack(padx=30, pady=50)

    nu = customtkinter.CTkEntry(newC, placeholder_text="Novo usuario")
    nu.pack(padx=10, pady=0)

    ns = customtkinter.CTkEntry(newC, placeholder_text="Sua senha", show="*")
    ns.pack(padx=10, pady=10)

#    img = PhotoImage(file="image/bem.png")
#    sub = img.subsample(5, 5)
#    label1 = Label(newC, image=sub)
#    label1.image = sub
#    label1.grid(row=6)

    c = customtkinter.CTkButton(newC, text="Criar", command=lambda: [gerenciar(nu.get(), ns.get()),voltar(), newC.destroy()])
    c.pack(padx=10, pady=10)

def voltar():
    janela.deiconify()

janela = customtkinter.CTk()
janela.geometry("720x480")

texto = customtkinter.CTkLabel(janela, text="Fazer login")
texto.pack(padx=30, pady=50)

email = customtkinter.CTkEntry(janela, placeholder_text="Seu Email")
email.pack(padx=10, pady=0)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)

nova = customtkinter.CTkButton(janela, text="Criar conta", command=novaConta)
nova.pack(padx=10, pady=10)

error = customtkinter.CTkLabel(janela, text="")
error.pack(padx=30, pady=10)

ka = customtkinter.CTkLabel(janela)
ka.pack(padx=30, pady=10)


janela.mainloop()








