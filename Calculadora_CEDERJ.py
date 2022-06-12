from tkinter import*
from tkinter import messagebox
import tkinter as tk
#root = tk.Tk()

largura = 650
altura = 500


class Calculator(object):
    def __init__(self, i):

        self.font = ('Verdana', '16', 'bold')
        self.fg = "#9a06fe"
        # Frame do Título
        self.frame1 = Frame(i)

        # Frame da Nota da AD1
        self.frame2 = Frame(i)

        # Frame da Nota da AP1
        self.frame3 = Frame(i)

        # Frame da Nota da AD2
        self.frame4 = Frame(i)

        # Frame da Mensagem do valor que falta para passar
        self.frame5 = Frame(i)

        # Frame do botão de confirmar
        self.frame6 = Frame(i)

        # Frame do Label da nota
        self.frame7 = Frame(i)

        # Frame do Canvas
        self.frame8 = Frame(i)

        # Label do título
        self.titulo = Label(self.frame1, font=self.font, text="Calculadora de Notas CEDERJ")

        # Label da AD1
        self.ad1 = Label(self.frame2, font=self.font, text="Nota AD1")

        # Entry da AD1
        self.notaAD1 = Entry(self.frame2, font=self.font)

        # Label da AP1
        self.ap1 = Label(self.frame3, font=self.font, text="Nota AP1")

        # Entry da AP1
        self.notaAP1 = Entry(self.frame3, font=self.font)


        # Label da AD2
        self.ad2 = Label(self.frame4, font=self.font, text="Nota AD2")

        # Entry da AD2
        self.notaAD2 = Entry(self.frame4, font=self.font)

        # Botão de calcular
        self.botao_calcular = Button(self.frame6, font=self.font, text="Calcular", command=self.calcular)
        self.nota_final = Label(self.frame8, font=self.font, text="", fg=self.fg)

        # Empacotamento dos widgets

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame7.pack()
        self.frame8.pack()
        self.titulo.pack()
        self.ad1.pack(side="left")
        self.notaAD1.pack(side="left", pady=15)
        self.ap1.pack(side="left")
        self.notaAP1.pack(side="left", pady=15)
        self.ad2.pack(side="left")
        self.notaAD2.pack(side="left", pady=15)
        self.botao_calcular.pack()
        self.nota_final.pack()


    def calcular(self, *args):
        if self.notaAD1.get() == "" or self.notaAP1.get() == "" or self.notaAD2.get() == "":
            x = messagebox.showerror(title="Atenção", message="Insira todas as notas para realizar o cálculo!")
            return x
        else:
            self.nota_ad1 = float(self.notaAD1.get())
            self.nota_ap1 = float(self.notaAP1.get())
            self.nota_ad2 = float(self.notaAD2.get())

            if self.nota_ad1 > 10 or self.nota_ap1 > 10 or self.nota_ad2 > 10 :

                x = messagebox.showerror(title="Atenção", message="Insira valores válidos! \nNotas entre 0 e 10")
                return x
            
            if self.nota_ap1 == 0:
                self.nota_final['text'] = (f"Uma pena você terá que fazer a AP3!\nDe acordo com critérios da faculdade\n uma prova não pode ter nota 0")
            else: 
                ad1 = self.nota_ad1*0.2
                ap1 = self.nota_ap1*0.8
                n1 = ad1+ap1
                ad2 = self.nota_ad2*0.2
                n2 = (n1 + ad2)/2
                self.ap2 = ((6-n2)*2)/0.8
                print(self.ap2)
                self.resultado(self.ap2)


    def resultado(self, x):
        if x <= 0:
            self.nota_final["text"] = "Relaxa você já passou nessa disciplina! \nMas cuidado você não pode zerar a AP2"

        else:
            self.nota_final['text'] = (f"Você precisa tirar {self.ap2:.1f} na AP2 \npara passar nessa disciplina!")

def esc(event):
    calculadora.destroy()

calculadora = Tk()

entradas = Calculator(calculadora)

calculadora.title("Calculadora CEDERJ")

# Coloca o ícone na janela
calculadora.iconbitmap('C:/Users/piura/Desktop/Calculadora/calculadora_cederj/Imagens/Calculator.ico')

# Define a geometria da janela
largura_screen = calculadora.winfo_screenwidth()
altura_screen = calculadora.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
calculadora.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

calculadora.bind("<Return>", entradas.calcular)
calculadora.bind("<Escape>", esc)

calculadora.mainloop()