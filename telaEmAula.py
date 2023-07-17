#Criar operações matematicas

from tkinter import * #interface gráfica
from operacoesMatematicas import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Operações Matemáticas")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.valorLabel1 = Label(self.segundoContainer,text="Digite valor 1", font=self.fontePadrao)
        self.valorLabel1.pack(side=LEFT)

        self.valor1 = Entry(self.segundoContainer)
        self.valor1["width"] = 30
        self.valor1["font"] = self.fontePadrao
        self.valor1.pack(side=LEFT)

        self.valorLabel2 = Label(self.terceiroContainer, text="Digite valor 2", font=self.fontePadrao)
        self.valorLabel2.pack(side=LEFT)

        self.valor2 = Entry(self.terceiroContainer)
        self.valor2["width"] = 30
        self.valor2["font"] = self.fontePadrao
        self.valor2.pack(side=LEFT)

        self.valorLabel3 = Label(self.quartoContainer, text="Resultado: ", font=self.fontePadrao)
        self.valorLabel3.pack(side=LEFT)
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.soma = Button(self.quintoContainer)
        self.soma["text"] = "somar"
        self.soma["font"] = ("Calibri", "8")
        self.soma["width"] = 20
        self.soma["command"] = self.somar
        self.soma.pack()

        self.subtrai = Button(self.quintoContainer)
        self.subtrai["text"] = "subtrair"
        self.subtrai["font"] = ("Calibri", "8")
        self.subtrai["width"] = 20
        self.subtrai["command"] = self.subtrair
        self.subtrai.pack()

        self.multiplica = Button(self.quintoContainer)
        self.multiplica["text"] = "multiplicar"
        self.multiplica["font"] = ("Calibri", "8")
        self.multiplica["width"] = 20
        self.multiplica["command"] = self.multiplicar
        self.multiplica.pack()

        self.dividi = Button(self.quintoContainer)
        self.dividi["text"] = "dividir"
        self.dividi["font"] = ("Calibri", "8")
        self.dividi["width"] = 20
        self.dividi["command"] = self.dividir
        self.dividi.pack()

    def somar(self):
            n1 = int(self.valor1.get())
            n2 = int(self.valor2.get())
            self.mensagem["text"] = somar(n1,n2)

    def subtrair(self):
            n1 = int(self.valor1.get())
            n2 = int(self.valor2.get())
            self.mensagem["text"] = subtrair(n1,n2)

    def multiplicar(self):
            n1 = int(self.valor1.get())
            n2 = int(self.valor2.get())
            self.mensagem["text"] = multiplicar(n1,n2)

    def dividir(self):
            n1 = int(self.valor1.get())
            n2 = int(self.valor2.get())
            self.mensagem["text"] = dividir(n1,n2)


root = Tk()
Application(root)
root.mainloop()