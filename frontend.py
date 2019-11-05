from tkinter import *
from functools import partial
import os
import sys
import random

def criptografo_sucesso():
    criptografado = Tk();
    criptografado.geometry("300x250");
    criptografado.resizable(False,False);
    
    lbl_sucesso = Label(criptografado,text="Mensagem criptografada com sucesso!!",pady=50);
    lbl_sucesso.pack(anchor="center",fill="x");
    
    btn_voltar = Button(criptografado, text="Voltar para a tela Inicial",padx=5,pady=7)
    btn_voltar.pack()
    btn_voltar["command"] = partial(voltar_tela, criptografado);

    criptografado.mainloop();

    


################################### Criptografia ##############################################

def janela_criptografia():

    

    def escrever_arquivo(nome, conteudo):
        
        nome = nome.replace(".txt", "")
        arquivo = open(nome + ".txt", 'w')
        
        arquivo.writelines(conteudo)
        arquivo.close()

    def gerar_chave():     
        #  Geração da Chave:
        key = list(msg_chave.get())
        
        chave_dec = [random.randint(0,999),random.randint(0,999),random.randint(0,999)]

        if key == []: key = list("Frase Padrão")      
        for x in range(0,len(key)): key[x] = dicio_encript[key[x]]
        
            
        #Algarismo 3---
        posic   = len(key)
        soma    = 0
        
        for numero in key:
            soma  = soma + numero * posic
            posic = posic - 1
        while soma > 900: soma = soma / random.randint(1,5)
        
        chave_dec[2] = int( (soma + chave_dec[2]) / 2 )
        
        #Algarismo 2---
        soma = soma / 2

        for numero in range(0,3): soma = soma + (random.choice(key))
        while soma > 900: soma = soma / random.randint(1,5)

        chave_dec[1] = int( (soma + chave_dec[1]) / 2 )

        #Algarismo 1----
        soma = chave_dec[0] + chave_dec[1] + len(key)
        soma = soma / 3
        soma = soma + (random.randint(0,999)+random.randint(0,999)+random.randint(0,999))
        soma = soma / 3
        
        while soma > 900: soma = soma / random.randint(1,5)
        
        chave_dec[0]   = int( (soma + chave_dec[0]) / 2 )


        # Impressão de Chave
        
        chave_dec.insert(1,"-")
        chave_dec.insert(3,"-")
        for x in chave_dec: chave_dec[chave_dec.index(x)] = str(x)
            
       
        return chave_dec

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
        chave_dec = "".join(gerar_chave())
        msg = criptografar(msg);


            
        arquivo = ["Chave de Descriptação: {}\n".format(chave_dec)]

        arquivo.extend(["-------------------------------------------\n\n"])
        arquivo.extend(["Mensagem Criptografada: \n\n{}".format(msg)])

        escrever_arquivo("cifra", arquivo)

        janela_criptografia.withdraw();

        criptografo_sucesso();
        


    
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
        descriptografado.resizable(False,False);
        
        lbl_sucesso = Label(descriptografado,text="Mensagem descriptografada com sucesso!!",pady=50);
        lbl_sucesso.pack(anchor="center",fill="x");

        lbl_mensagem_descriptograda = Label(descriptografado,text=mensagem);
        lbl_mensagem_descriptograda.pack(anchor="center",fill="x");
        Label(janela_criptografia,text="",height=3).pack()
        btn_voltar = Button(descriptografado, text="Voltar para a tela Inicial",padx=5,pady=7)
        btn_voltar.pack()
        btn_voltar["command"] = partial(voltar_tela, descriptografado);

        descriptografado.mainloop();

        

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
        
        msg = str(msg_descriptografia.get())
               
        # Recepção da Chave, retomada de chave invalida!
        while len(chave_dec) != 3:
            
            chave_dec = list(msg_chave_descript.get())
            chave_dec = "".join(chave_dec)
            chave_dec = chave_dec.split("-")
            
        
        msg = descriptografar(msg)

        descriptografo_sucesso(msg)
        
        ##print("\nMensagem Descriptografada: \n\n{} \n".format(msg))
        ##print("-------------------------------------------\n\n\n")

    
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
