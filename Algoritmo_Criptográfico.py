import random

##   Obs: o termo "Célula" é usado neste algoritmo para designar cada valor de uma lista
##   (podendo ser uma letra da mensagem original, ou seu valor resultante).

#################################################################################################################

### *** Funções Utlitárias *** ###

#-----------------------------------------------------------------------------------------------------------------
# Lê arquivo de Texto e retorna o conteúdo
    
def ler_arquivo(nome):
    
    nome = nome.replace(".txt", "")
    arquivo  = open(nome + ".txt", 'r')
    conteudo = ""
    
    conteudo = arquivo.readlines()

    arquivo.close()
    return conteudo

#-----------------------------------------------------------------------------------------------------------------
# Escreve um conteúdo em um arquivo de texto

def escrever_arquivo(nome, conteudo):
    
    nome = nome.replace(".txt", "")
    arquivo = open(nome + ".txt", 'w')
    
    arquivo.writelines(conteudo)
    arquivo.close()
    
#-----------------------------------------------------------------------------------------------------------------        

### *** Funções Secundárias *** ###

#-----------------------------------------------------------------------------------------------------------------
# Dicionários contendo os valores que cada celula irá assumir


dicio_encript = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27,
 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40,
 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52, ' ': 53,
 '-': 54, '_': 55, '+': 56, '=': 57, ')': 58, '(': 59, '*': 60, '%': 61, '#': 62, '@': 63, '!': 64, "'": 65, '[': 66,
 ']': 67, '{': 68, '}': 69, 'ã': 70, 'Ã': 71, 'ô': 72, 'Ô': 73, 'é': 74, 'É': 75, 'á': 76, 'Á': 77, 'à': 78, 'À': 79,
 'ê': 80, 'Ê': 81, 'Ç': 82, 'ç': 83, '&': 84, 'º': 85, '|': 86, ',': 87, '.': 88, ';': 89, ':': 90, 'ó': 91, 'Ó': 92,
 '0': 93, '1': 94, '2': 95, '3': 96, '4': 97, '5': 98, '6': 99, '7': 100, '8': 101, '9': 102, '<': 103, '>': 104,
 '~': 105, '$': 106, '¨': 107, '/': 108, '\\': 109, '"': 110, '?': 111}

dicio_decript = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n',
 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: 'A',
 28: 'B', 29: 'C', 30: 'D', 31: 'E', 32: 'F', 33: 'G', 34: 'H', 35: 'I', 36: 'J', 37: 'K', 38: 'L', 39: 'M', 40: 'N',
 41: 'O', 42: 'P', 43: 'Q', 44: 'R', 45: 'S', 46: 'T', 47: 'U', 48: 'V', 49: 'W', 50: 'X', 51: 'Y', 52: 'Z', 53: ' ',
 54: '-', 55: '_', 56: '+', 57: '=', 58: ')', 59: '(', 60: '*', 61: '%', 62: '#', 63: '@', 64: '!', 65: "'", 66: '[',
 67: ']', 68: '{', 69: '}', 70: 'ã', 71: 'Ã', 72: 'ô', 73: 'Ô', 74: 'é', 75: 'É', 76: 'á', 77: 'Á', 78: 'à', 79: 'À',
 80: 'ê', 81: 'Ê', 82: 'Ç', 83: 'ç', 84: '&', 85: 'º', 86: '|', 87: ',', 88: '.', 89: ';', 90: ':', 91: 'ó', 92: 'Ó',
 93: '0', 94: '1', 95: '2', 96: '3', 97: '4', 98: '5', 99: '6', 100: '7', 101: '8', 102: '9', 103: '<', 104: '>',
 105: '~', 106: '$', 107: '¨', 108: '/', 109: '\\', 110: '"', 111: '?'}
    
#-----------------------------------------------------------------------------------------------------------------
#   gera a chave de encriptação, exibi e a retorna

def gerar_chave(key):
        
    #  Geração da Chave:
    
    chave_dec = [random.randint(10000,99999),random.randint(10000,99999),random.randint(10000,99999)]

    if key == []: key = list("Frase Padrão")      
    for x in range(0,len(key)): key[x] = dicio_encript[key[x]]
    
        
    #Algarismo 3---
    posic   = len(key)
    soma    = 0
    
    for numero in key:
        soma  = soma + numero * posic
        posic = posic - 1
    while soma > 99999: soma = soma / random.randint(1,5)
    
    chave_dec[2] = int( (soma + chave_dec[2]) / 2 )
    
    #Algarismo 2---
    soma = soma / 2

    for numero in range(0,3): soma = soma + (random.choice(key))
    while soma > 99999: soma = soma / random.randint(1,5)

    chave_dec[1] = int( (soma + chave_dec[1]) / 2 )

    #Algarismo 1----
    soma = chave_dec[0] + chave_dec[1] + len(key)
    soma = soma / 3
    soma = soma + (random.randint(0,999)+random.randint(0,999)+random.randint(0,999))
    soma = soma / 3
    
    while soma > 99999: soma = soma / random.randint(1,5)
    
    chave_dec[0]   = int( (soma + chave_dec[0]) / 2 )


    # Impressão de Chave
    
    chave_dec.insert(1,"-")
    chave_dec.insert(3,"-")
    for x in chave_dec: chave_dec[chave_dec.index(x)] = str(x)
    
    return chave_dec
#-----------------------------------------------------------------------------------------------------------------
# converte a msg original na criptografada

def criptografar(msg, chave):
    
    chave = chave.split("-")
    chave = [int(ch) for ch in chave]
    
    msg       = list(msg)
    posicao   = len(msg)
    somatoria = 0
    
    msg.reverse()
    
    # Gera um novo valor para célula--
    
    for n in range(0, len(msg)):
            
        msg[n]     = dicio_encript.get(msg[n])
        msg[n]     = msg[n] if msg[n] is not None else 0
        somatoria += msg[n]
        msg[n]     = ( ( msg[n] * posicao * chave[0] ) + chave[1] ) * chave[2] + somatoria - msg[n]
        posicao   -= 1
    
    msg.reverse()
    somatoria = 0
    
    for n in range(0, len(msg)):
            
        somatoria += msg[n]
        msg[n]    += somatoria - msg[n]
        msg[n]     = converter_base(msg[n])
        msg[n]     = msg[n].replace("'", "£")
    
    #--
    
    return "¬".join(msg)
        
#-----------------------------------------------------------------------------------------------------------------
# converte a msg criptografada na original novamente
    
def descriptografar(msg, chave):
    
    chave = chave.split("-")
    chave = [int(ch) for ch in chave]
    
    msg       = msg.split("¬")
    posicao   = len(msg)
    somatoria = 0
    
    for n in range(0, len(msg)):
            
        msg[n]     = converter_base_decimal(msg[n])
        msg[n]    -= somatoria
        somatoria += msg[n]
        
    somatoria = 0
    msg.reverse()
    
    for n in range(0, len(msg)):
            
        msg[n]     = (msg[n] - (chave[1] * chave[2] + somatoria)) / (posicao * chave[0] * chave[2])
        somatoria += msg[n]
        msg[n]     = dicio_decript.get(msg[n])
        msg[n]     = msg[n] if msg[n] is not None else "*"
        posicao   -= 1
            
    msg.reverse()
    return "".join(msg)
    
#-----------------------------------------------------------------------------------------------------------------
# Converte um número em base decimal para um número com base 112
    
def converter_base(num):

    result = []
    while num > 111:
            
        valor = str(dicio_decript.get(num % 112))
        valor = valor if valor != 'None' else '¢'
        result.insert(0, valor)
        num = num // 112
    
    result.insert(0, str(dicio_decript[num]))
    return "".join(result)

#-----------------------------------------------------------------------------------------------------------------
# Converte um número em base 112 para decimal

def converter_base_decimal(num):

    num     = list(num)
    casas   = len(num)
    result  = 0

    num.reverse()
    
    for x in range(0, casas):
    
        if   num[x] == '¢': num[x] = '0'
        elif num[x] == '£': num[x] = '65'
        else:
            for value in dicio_decript:
                if dicio_decript[value] == num[x]: num[x] = value
                
        result += int(num[x])*112**x
        
    return result
    
#-----------------------------------------------------------------------------------------------------------------
 
### *** Funções Principais *** ###

#-----------------------------------------------------------------------------------------------------------------

def processo_criptografar(msg, key):
        
    chave_dec = "".join(gerar_chave(key))
    msg       = criptografar(msg, chave_dec)
    arquivo   = ["Chave de Descriptação: {}\n".format(chave_dec)]

    arquivo.extend(["-------------------------------------------\n\n"])
    arquivo.extend(["Mensagem Criptografada: \n\n'{}'".format(msg)])

    escrever_arquivo("cifra", arquivo)

#-----------------------------------------------------------------------------------------------------------------        
        
def processo_descriptografar(msg, chave_dec):
    
    msg_original = msg
    msg          = msg.replace("'", "")
    msg          = descriptografar(msg, chave_dec)
    arquivo      = ["Chave de Descriptação: {}\n".format(chave_dec)]
    
    arquivo.extend(["-------------------------------------------\n\n"])
    arquivo.extend(["Mensagem Criptografada: \n\n{}".format(msg_original)])
    arquivo.extend(["\n\n-------------------------------------------\n\n"])
    arquivo.extend(["Mensagem Descriptografada: \n\n{}".format(msg)])
    
    escrever_arquivo("cifra", arquivo)
    
    return msg
#-----------------------------------------------------------------------------------------------------------------
 
### *** Fim - Funções *** ###

#################################################################################################################

