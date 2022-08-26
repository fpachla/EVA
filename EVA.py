import os
import pyautogui as cm
from tkinter import *
from tkinter import filedialog
from psutil import process_iter


win = Tk()

win.title("EVA")
win.geometry("800x350")
myName = Label(win, text="Fernanda Pachla", font=("Comic Sans", 7))
myName.place(x=0, y=0)


link = []

#Instruções:
instrucoes = "Siga as instruções a seguir:" \
            "\n1º- O programa deve " \
            "\n\n1º- O arquivo deve estar em CONFIDENCIAL" \
            "\n2º- Pressione Procurar arquivo e selecione o arquivo desejado" \
            "\n3º- Confira o nome e o diretório do arquivo" \
            "\n4º- Pressione Executar e espere o programa finalizar o processo" \
            "\n\n\nEM CASO DE ERRO: pressionar Ctrl+alt+del"

myInstrucoes = Label(win, text=f"{instrucoes}",font=(12), justify=LEFT)
myInstrucoes.place(x=275, y=25)

#Botão 1
def selecionarArquivo():
    win.diretorio = filedialog.askopenfilename(initialdir="/", title="Abrir arquivo" )
    x = win.diretorio.split("/")
    link.append(x[-1])
    mostrarDiretorio = Label(win, font=("courier"), justify= LEFT,
                             text=str(f"Diretório do arquivo:  {win.diretorio:}" \
                                    f"\n\nNome do arquivo:       {x[-1]:}"))
    mostrarDiretorio.place(x=10, y=230)

#Botão 2
def execucaoFinal():
    # Checa se o app está aberto
    app = "C:APPConfidencial.exe"
    if "APPConfidencial.exe" in (app.name() for app in process_iter()) == True:
        os.close(app)
    os.startfile(app)  # Inicialização do programa
    cm.sleep(18)


    def clickAndWait(cordX, cordY, time):  #função de clique e espera (mouse)
        cm.click(cordX, cordY)
        cm.sleep(time)

    def pressAndWait(key, time): #função de clique e espera (teclado)
        cm.press(f"{key}")
        cm.sleep(time)


    # LOGIN
    clickAndWait(477, 335, 1)
    cm.write("CONFIDENCIAL - login")
    pressAndWait("tab", 1)
    cm.write("CONFIDENCIAL - senha")
    pressAndWait("enter", 1)
    cm.sleep(1)

    width = cm.size()  # Captura o tamanho da tela
    clickAndWait(504, 402, 0.5)  # seleciona parte aleatória para entrar no programa (Gerencie os arquivos)
    clickAndWait(634, 44, 0.5)  # seleciona "PROGRAMA"

    cm.sleep(1)
    for i in range(8):  # Abrindo a aba "PROGRAMA nos próximos queimadores"
        if i == 0:
            clickAndWait(794, 297, 0.5)  # selecionando o endereço (1)
        elif i > 0:
            clickAndWait(1014, 361, 0.5)  # baixando a guia
            clickAndWait(794, 297 , 0.5)  # selecionando o endereço (2 a 8)

        pressAndWait("enter", 1)  # Deseja editar o programa: "SIM"
        clickAndWait(68, 114, 1)  # Selecionando a guia "ABRIR" do SOFTWARE

        for i in range(7):
            pressAndWait("tab", 0.1)

        cm.keyDown
        cm.sleep(0.2)
        pressAndWait("space", 0.1)
        clickAndWait(794, 297, 0.1)  # selecionando parte aleatória
        cm.typewrite("forno", 0.1) #consertar
        cm.press("enter")
        for i in range(2):
            cm.press("tab")
        cm.write(link[0])  # Escreve no diretório do arquivo
        pressAndWait("enter", 1)
        pressAndWait("enter", 1)  # Deseja sincronizar com o equipamento: "SIM"
        cm.sleep(6)


getNome = Button(win,
                 text="Nome do arquivo",
                 padx=8,
                 pady=4,
                 height= 1,
                 width= 20,
                 fg="blue",
                 command=selecionarArquivo)

getNome.place(x=30, y=75)

executarPrograma = Button(win,
                          text="Executar",
                          padx=8,
                          pady=4,
                          height= 1,
                          width= 20,
                          fg="green",
                          command=execucaoFinal)

executarPrograma.place(x=30, y= 125)

win.mainloop()
