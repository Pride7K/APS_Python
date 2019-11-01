from tkinter import *
from functools import partial

def janela_criptografia():
    janela_criptografia = Tk();
    estilo_janelas(janela_criptografia)
    janela.destroy();

def janela_descriptografia():
    janela_descriptografia = Tk();
    estilo_janelas(janela_descriptografia)
    janela.destroy();
    
def sair():
    janela.destroy();

def estilo_janelas(janela_estilo):
    janela_estilo.geometry("300x300");
    janela_estilo.title("Tela de Criptografia");
    btn_voltar = Button(janela_estilo,text="Voltar para a tela Inicial");
    btn_voltar.pack(anchor="s",side="left");
    btn_voltar["command"] = partial(voltar_tela,janela_estilo);
    return janela_estilo

def voltar_tela(tela):
    tela.destroy();
    return criar_tela_inicial();

def criar_tela_inicial():
    
    janela = Tk();

    ## Criando elementos da janela inicial e definindo funções

    lbl_titulo = Label(janela,text="Bem vindo a nossa aplicação",height=3);
    lbl_titulo2 = Label(janela,text="Escolha uma das opções abaixo",height=7);
    btn_criptografia = Button(janela,text="Criptografia",width=30);
    btn_descriptografia = Button(janela,text="Descriptografia",width=30);
    btn_sair = Button(janela,text="Sair",width=30);

    btn_criptografia["command"] = janela_criptografia;
    btn_descriptografia["command"] = janela_descriptografia;
    btn_sair["command"] = sair;


    ########################################################################

    ## Posicionando os elementos da janela inicial

    lbl_titulo.pack(fill="x")
    lbl_titulo2.pack(fill="both")
    btn_criptografia.pack();
    btn_descriptografia.pack();
    btn_sair.pack();

    ########################################################################


    janela.mainloop();


criar_tela_inicial()


