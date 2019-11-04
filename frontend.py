from tkinter import *
from functools import partial
import os
import sys
import random


################################### Criptografia ##############################################

def janela_criptografia():

    def complexidade(n_celula): return (n_celula)# + int(chave_dec[4])) * int(chave_dec[0]) 

    dicio_encript = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27,
 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40,
 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52, ' ': 53,
 '-': 54, '_': 55, '+': 56, '=': 57, ')': 58, '(': 59, '*': 60, '%': 61, '#': 62, '@': 63, '!': 64, "'": 65, '[': 66,
 ']': 67, '{': 68, '}': 69, 'ã': 70, 'Ã': 71, 'ô': 72, 'Ô': 73, 'é': 74, 'É': 75, 'á': 76, 'Á': 77, 'à': 78, 'À': 79,
 'ê': 80, 'Ê': 81, 'Ç': 82, 'ç': 83, '&': 84, 'º': 85, '|': 86, ',': 87, '.': 88, ';': 89, ':': 90, 'ó': 91, 'Ó': 92,
 '0': 93, '1': 94, '2': 95, '3': 96, '4': 97, '5': 98, '6': 99, '7': 100, '8': 101, '9': 102, '<': 103, '>': 104,
 '~': 105, '$': 106, '¨': 107, '/': 108, '\\': 109, '"': 110, '?': 111}
    
    def criptografar(msg):
        msg = list(msg)
        n_celula = len(msg)
        
        # Gera um novo valor para célula
        for n in range(0, len(msg)):
            
            msg[n]    = dicio_encript[msg[n]] + complexidade(n_celula)
            msg[n]    = str(msg[n]) + "#"
            n_celula -= 1
            
        return "".join(msg)
        
    def processo_criptografar():
    
        ##chave_dec = "".join(gerar_chave())
        
        msg = str(msg_criptografia.get())

        msg = criptografar(msg);

        lbl1_criptografia["text"] = msg
        
        ##print("Mensagem Criptografada e chave gerada no arquivo!! \n")
        ##print("-------------------------------------------\n\n\n")

            
        ##arquivo = ["Chave de Descriptação: {}\n".format(chave_dec)]

        ##arquivo.extend(["-------------------------------------------\n\n"])
        ##arquivo.extend(["Mensagem Criptografada: \n\n{}".format(msg)])

        ##escrever_arquivo("cifra", arquivo)


    
    janela_criptografia = Tk()
    estilo_janelas(janela_criptografia)
    janela.withdraw()

    
    lbl1_criptografia = Label(janela_criptografia,text="Insira uma mensagem para criptografar",bg="green",height = 3);
    lbl1_criptografia.pack(fill="both");
    
    msg_criptografia = Entry(janela_criptografia);
    msg_criptografia.place(x=70,y=90);
    
    btn_criptografar = Button(janela_criptografia,text="Criptografar",width = 15);
    btn_criptografar["command"] = partial(processo_criptografar);
    btn_criptografar.place(x=70,y=130);
    
    btn_voltar = Button(janela_criptografia, text="Voltar para a tela Inicial",padx=5,pady=7)
    btn_voltar.pack(anchor="s", side="left")
    btn_voltar["command"] = partial(voltar_tela, janela_criptografia)

    janela_criptografia.mainloop();




#################################################################################################################








################################### Descriptografia #############################################################


def janela_descriptografia():

    dicio_decript = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n',
 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: 'A',
 28: 'B', 29: 'C', 30: 'D', 31: 'E', 32: 'F', 33: 'G', 34: 'H', 35: 'I', 36: 'J', 37: 'K', 38: 'L', 39: 'M', 40: 'N',
 41: 'O', 42: 'P', 43: 'Q', 44: 'R', 45: 'S', 46: 'T', 47: 'U', 48: 'V', 49: 'W', 50: 'X', 51: 'Y', 52: 'Z', 53: ' ',
 54: '-', 55: '_', 56: '+', 57: '=', 58: ')', 59: '(', 60: '*', 61: '%', 62: '#', 63: '@', 64: '!', 65: "'", 66: '[',
 67: ']', 68: '{', 69: '}', 70: 'ã', 71: 'Ã', 72: 'ô', 73: 'Ô', 74: 'é', 75: 'É', 76: 'á', 77: 'Á', 78: 'à', 79: 'À',
 80: 'ê', 81: 'Ê', 82: 'Ç', 83: 'ç', 84: '&', 85: 'º', 86: '|', 87: ',', 88: '.', 89: ';', 90: ':', 91: 'ó', 92: 'Ó',
 93: '0', 94: '1', 95: '2', 96: '3', 97: '4', 98: '5', 99: '6', 100: '7', 101: '8', 102: '9', 103: '<', 104: '>',
 105: '~', 106: '$', 107: '¨', 108: '/', 109: '\\', 110: '"', 111: '?'}

    def complexidade(n_celula): return (n_celula)

    def descriptografar(msg):
    
        msg = msg.split("#")
        if "" in msg: msg.remove("")
        n_celula = len(msg)
        
        
        for n in range(0, len(msg)):
            
            msg[n] = int(msg[n]) - complexidade(n_celula) if msg[n].isnumeric() else 0
            
            if msg[n] in dicio_decript: msg[n] = dicio_decript[msg[n]]
            else: msg[n] = "*"
            
            n_celula -= 1
            
        return "".join(msg)

    def processo_descriptografar():
        
        global chave_dec
        
        ##msg = escolha("cls", "Digite a mensagem a ser Descriptografada: ", "cls")
               
        # Recepção da Chave, retomada de chave invalida!
        while len(chave_dec) != 3:
            
            chave_dec = list(escolha("", "\nDigite a chave de Desencriptação: \n\n", ""))
            chave_dec = "".join(chave_dec)
            chave_dec = chave_dec.split("-")
            clean()
        
        msg = descriptografar(msg)
        
        ##print("\nMensagem Descriptografada: \n\n{} \n".format(msg))
        ##print("-------------------------------------------\n\n\n")

    
    janela_descriptografia = Tk()
    estilo_janelas(janela_descriptografia)
    janela.withdraw()

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
