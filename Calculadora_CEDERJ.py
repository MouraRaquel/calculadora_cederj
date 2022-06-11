from tkinter import*

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
            return None
        else:
            self.nota_ad1 = self.notaAD1.get()
            self.nota_ap1 = self.notaAP1.get()
            self.nota_ad2 = self.notaAD2.get()
            ad1 = int(self.nota_ad1)*2
            ap1 = int(self.nota_ap1)*8
            n1 = ad1+ap1
            ad2 = int(self.nota_ad2)*2
            nota_2 = 1200 - (n1 + ad2)
            self.ap2 = (nota_2/8)/10
            print(self.ap2)
            self.resultado(self.ap2)


    def resultado(self, x):
        if x <= 0:
            self.nota_final["text"] = "Relaxa você já passou nessa disciplina!"

        else:
            self.nota_final['text'] = (f"Você precisa tirar {self.ap2} na AP2 \npara passar nessa disciplina!")

def esc(event):
    calculadora.destroy()

calculadora = Tk()

entradas = Calculator(calculadora)

calculadora.title("Calculadora CEDERJ")

# Coloca o ícone na janela
calculadora.iconbitmap("Calculator.ico")

# Define a geometria da janela
largura_screen = calculadora.winfo_screenwidth()
altura_screen = calculadora.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
calculadora.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

calculadora.bind("<Return>", entradas.calcular)
calculadora.bind("<Escape>", esc)

calculadora.mainloop()