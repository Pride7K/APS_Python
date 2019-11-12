from tkinter import *
from functools import partial
import os
import sys
import Algoritmo_Criptográfico as algoritmo



def aviso(mensagem):

    def voltar():
        aviso_sistema.withdraw()
    
    aviso_sistema = Tk();
    aviso_sistema.geometry("300x250");
    aviso_sistema .title("AVISO")
    aviso_sistema.resizable(False,False);

    lbl_aviso_sistema = Label(aviso_sistema,text=mensagem);
    lbl_aviso_sistema.pack(anchor="center",fill="x",pady=50);
    Button(aviso_sistema,text="Voltar",width=30,command=voltar).pack();
    Label(aviso_sistema,text="",height=3).pack()

    aviso_sistema.mainloop()

def criptografo_sucesso():
    
    criptografado = Tk()
    criptografado.geometry("300x250")
    criptografado.resizable(False,False)
    criptografado.title("Criptografia concluida com sucesso!");
    lbl_sucesso = Label(criptografado,text="Mensagem criptografada com sucesso!!",pady=50)
    lbl_sucesso.pack(anchor="center",fill="x")
    
    btn_voltar = Button(criptografado, text="Voltar para a tela Inicial",padx=5,pady=7)
    btn_voltar.pack()
    btn_voltar["command"] = partial(voltar_tela, criptografado)

    criptografado.mainloop()

################################### Criptografia ##############################################

def janela_criptografia():

    def processo_criptografar():
        
        msg       = str(msg_criptografia.get())
        key       = list(msg_chave.get())

        if msg == "":
            aviso("Digite uma mensagem!!!")
            return
        
        algoritmo.processo_criptografar(msg, key)
        
        janela_criptografia.withdraw();
        criptografo_sucesso()
        


    
    janela_criptografia = Tk()
    estilo_janelas(janela_criptografia)
    janela.withdraw()

    
    lbl1_criptografia = Label(janela_criptografia,text="Insira uma mensagem para criptografar",height = 3);
    lbl1_criptografia.pack(fill="both");
    
    msg_criptografia = Entry(janela_criptografia);
    msg_criptografia["width"] = 30
    msg_criptografia.pack();

    lbl1_chave = Label(janela_criptografia,text="Insira uma mensagem para servir de chave criptografica",height = 3);
    lbl1_chave.pack(fill="both");

    msg_chave = Entry(janela_criptografia);
    msg_chave["width"] = 30
    msg_chave.pack();

    Label(janela_criptografia,text="",height=3).pack()
    
    btn_criptografar = Button(janela_criptografia,text="Criptografar",width = 15,pady=10);
    btn_criptografar["command"] = partial(processo_criptografar);
    btn_criptografar.pack();
    
    btn_voltar = Button(janela_criptografia, text="Voltar para a tela Inicial",padx=5,pady=7)
    btn_voltar.pack(anchor="s", side="left")
    btn_voltar["command"] = partial(voltar_tela, janela_criptografia)

    janela_criptografia.mainloop();




#################################################################################################################








################################### Descriptografia #############################################################


def janela_descriptografia():


    def descriptografo_sucesso(mensagem):
        descriptografado = Tk();
        descriptografado.geometry("300x250");
        descriptografado.title("Descriptografia concluida com sucesso!");
        descriptografado.resizable(False,False);
        janela_descriptografia.withdraw()
        lbl_sucesso = Label(descriptografado,text="Mensagem descriptografada com sucesso!!",pady=50);
        lbl_sucesso.pack(anchor="center",fill="x");

        lbl_mensagem_descriptograda = Label(descriptografado,text=mensagem);
        lbl_mensagem_descriptograda.pack(anchor="center",fill="x");
        Label(descriptografado,text="",height=3).pack()
        btn_voltar = Button(descriptografado, text="Voltar para a tela Inicial",padx=5,pady=7)
        btn_voltar.pack()
        btn_voltar["command"] = partial(voltar_tela, descriptografado);

        descriptografado.mainloop()




    def processo_descriptografar():
        
        msg       = str(msg_descriptografia.get())
        chave_dec = msg_chave_descript.get()

        if msg == "":
            aviso("Digite uma mensagem!!!")
            return
        
        validar_chave = len(chave_dec.split("-")) == 3

        for sub_key in chave_dec.split("-"):
            
            if sub_key.isnumeric():
                if not int(sub_key) > 0:
                    validar_chave = False
                    break
                
            else:
                validar_chave = False
                break
        
        if not validar_chave:
            aviso("Chave Invalida!!!")
            return

        
        msg = algoritmo.processo_descriptografar(msg, chave_dec)
        
        descriptografo_sucesso(msg)
        

    
    janela_descriptografia = Tk()
    estilo_janelas(janela_descriptografia)
    janela.withdraw()

    lbl1_descriptografia = Label(janela_descriptografia,text="Insira uma mensagem para descriptografa-la",height = 3);
    lbl1_descriptografia.pack(fill="both");
    
    msg_descriptografia = Entry(janela_descriptografia);
    msg_descriptografia["width"] = 30
    msg_descriptografia.pack();

    lbl1_chave_descript = Label(janela_descriptografia,text="Insira a chave  descriptográfica",height = 3);
    lbl1_chave_descript.pack(fill="both");

    msg_chave_descript = Entry(janela_descriptografia);
    msg_chave_descript["width"] = 30
    msg_chave_descript.pack();

    Label(janela_descriptografia,text="",height=3).pack()
    
    btn_descriptografar = Button(janela_descriptografia,text="Descriptografar",width = 15,pady=10);
    btn_descriptografar["command"] = partial(processo_descriptografar);
    btn_descriptografar.pack();

    btn_voltar = Button(janela_descriptografia, text="Voltar para a tela Inicial",padx=5,pady=7)
    btn_voltar.pack(anchor="s", side="left")
    btn_voltar["command"] = partial(voltar_tela, janela_descriptografia)

    janela_descriptografia.mainloop();






#################################################################################################################







def sair():
    janela.destroy()


def estilo_janelas(janela_estilo):
    janela_estilo.geometry("350x300")
    janela_estilo.title("Tela de Criptografia")
    return janela_estilo


def voltar_tela(tela):
    tela.withdraw()
    janela.update()
    janela.deiconify()






    
    
janela = Tk()
janela.title("APS Aplicação");
janela.geometry("350x400");

chave_dec = ""

# Criando elementos da janela inicial e definindo funções

lbl_titulo = Label(janela, text="Bem vindo a nossa aplicação", height=3)
lbl_titulo2 = Label(janela, text="Escolha uma das opções abaixo", height=7)
btn_criptografia = Button(janela, text="Criptografia", width=30,padx=5,pady=7)
lbl_espaco = Label(janela,text="",width=30);
btn_descriptografia = Button(janela, text="Descriptografia", width=30,padx=5,pady=7)
lbl_espaco2 = Label(janela,text="",width=30);
btn_sair = Button(janela, text="Sair", width=30,padx=5,pady=7)

btn_criptografia["command"] = janela_criptografia
btn_descriptografia["command"] = janela_descriptografia
btn_sair["command"] = sair
########################################################################

# Posicionando os elementos da janela inicial

lbl_titulo.pack(fill="x")
lbl_titulo2.pack(fill="both")
btn_criptografia.pack()
lbl_espaco.pack(fill="x");
btn_descriptografia.pack()
lbl_espaco2.pack(fill="x");
btn_sair.pack()

########################################################################

janela.mainloop()
