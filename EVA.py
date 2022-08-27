import os
import subprocess

import pyautogui as cm
from tkinter import *
from tkinter import filedialog
from psutil import process_iter

win = Tk()

win.title("EVA")
win.geometry("800x350")
myName = Label(win, justify=LEFT, font=("Comic Sans", 7), text="Fernanda Pachla"
                                                               "\nVersão alfa")
myName.place(x=0, y=0)

link = []  # gambiarra
tempo = [8]

# Instruções:
instrucoes = "Siga as instruções a seguir:" \
             "\n1º- O programa deve " \
             "\n\n1º- O arquivo deve estar em CONFIDENCIAL" \
             "\n2º- Pressione Procurar arquivo e selecione o arquivo desejado" \
             "\n3º- Confira o nome e o diretório do arquivo" \
             "\n4º- Pressione Executar e espere o programa finalizar o processo" \
             "\n5º- O APPCONFIDENCIAL deve estar fechado antes da execução do programa" \
             "\n\n\nEM CASO DE ERRO: pressionar Ctrl+alt+del"

myInstrucoes = Label(win, text=f"{instrucoes}", font=(12), justify=LEFT)
myInstrucoes.place(x=275, y=25)


# Botao de alterar tempo
def pegarNovoTempo():
    t = entry1.get()
    try:
        a = int(t, base=10)
        tempo[0] = a
    except ValueError:
        pass
    mostrarTempo = Label(win, pady=4, text=f"Tempo atual: {tempo[-1]} s")  # mostrar novo tempo
    mostrarTempo.place(x=100, y=200)


mostrarTempo = Label(win, text=f"Tempo atual: {tempo[-1]} s")  # mostrar tempo
mostrarTempo.place(x=100, y=200)

entry1 = Entry(win, width=5)  # pegar novo tempo
entry1.place(x=30, y=200)

button = Button(win, text="Novo tempo", command=pegarNovoTempo, padx=8,
                pady=4,
                height=1,
                width=20, )
button.place(x=30, y=150)


# Botão 1
def selecionarArquivo():
    win.diretorio = filedialog.askopenfilename(initialdir="C:/Users/operador/Desktop/Forno arquivos",
                                               title="Abrir arquivo")
    x = win.diretorio.split("/")
    link.append(x[-1])
    mostrarDiretorio = Label(win, font=("courier"), justify=LEFT,
                             text=str(f"Diretório do arquivo:  {win.diretorio:}"
                                      f"\n\nNome do arquivo:       {x[-1]:}"))
    mostrarDiretorio.place(x=10, y=260)


# Botão 2
def execucaoFinal():
    # Checa se o app está aberto
    APP = "C:/DIRETORIO/APP.exe"

    isRunning = subprocess.check_output('tasklist')
    if not (b'Contemp Connect.exe' in isRunning):
        os.startfile(APP)
        cm.sleep(20)

        def clickAndWait(cordX, cordY, time):  # função de clique e espera (mouse)
            cm.click(cordX, cordY)
            cm.sleep(time)

        def pressAndWait(key, time):  # função de clique e espera (teclado)
            cm.press(f"{key}")
            cm.sleep(time)

        # LOGIN
        clickAndWait(477, 335, 1)
        cm.typewrite("CONFIDENCIAL LOGIN", 0.05)
        cm.press("tab")
        cm.typewrite("CONFIDENCIAL SENHA", 0.05)
        pressAndWait("enter", 3)

        width = cm.size()  # Captura o tamanho da tela
        clickAndWait(504, 402, 1)  # seleciona parte aleatória para entrar no programa
        clickAndWait(634, 44, 1)  # seleciona "CONFIDENCIAL"

        cm.sleep(1)
        for i in range(8):  # Abrindo a aba "CONFIDENCIAL"
            if i == 0:
                clickAndWait(794, 297, 1)  # selecionando o endereço (1)
            elif i > 0:
                clickAndWait(1014, 361, 1)  # baixando a guia
                clickAndWait(794, 297, 1)  # selecionando o endereço (2 a 8)

            pressAndWait("enter", 1)  # Deseja editar o programa: "SIM"
            clickAndWait(68, 114, 1)  # Selecionando a guia "CONFIDENCIAL" do SOFTWARE

            for i in range(7):
                pressAndWait("tab", 0.1)

            pressAndWait("space", 0.1)
            clickAndWait(794, 297, 0.8)  # selecionando parte aleatória
            cm.typewrite("fornoeva", 0.5)  # consertar
            cm.press("enter")
            for i in range(2):
                cm.press("tab")

            cm.write(link[0])  # Escreve no diretório do arquivo
            pressAndWait("enter", 2)
            pressAndWait("enter", 2)  # Deseja sincronizar com o equipamento: "SIM"
            cm.sleep(tempo[0])


getNome = Button(win,
                 text="Nome do arquivo",
                 padx=8,
                 pady=4,
                 height=1,
                 width=20,
                 fg="blue",
                 command=selecionarArquivo)

getNome.place(x=30, y=50)

executarPrograma = Button(win,
                          text="Executar",
                          padx=8,
                          pady=4,
                          height=1,
                          width=20,
                          fg="green",
                          command=execucaoFinal)

executarPrograma.place(x=30, y=100)

win.mainloop()
