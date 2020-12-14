###########################################Mapa meu###########################################################
mp = """l-----------------l\nloooooooolooooooool\nloo------looloolool\nloooooooooooloolool\nloo---------loo---l\nloooooloooooloooool\n---loo---loo---lool\nloooooooooooooolool\nl-----------------l"""
mp = mp[:77]+"p"+mp[78:]
mp_b = mp[:len(mp)-38]+"a"+mp[len(mp)-37:]
s,s_b = mp, mp_b

###############################Troque os símbolos ASCII!#########Alt + ???################•,◘,├,░,▓,○,■##################
import re          

parede = '▓'                #Não usar . + , o * / |
muro = '▓'                  #  
caminho = '░'               #
coisa = '■'                 #
port = '◘'                  #

########################################Movimentaçao###################################################

lab = s.replace('l',parede).replace('-',muro).replace('o',caminho).replace('p',port)
boneco = s_b.replace('a',coisa).replace('l',parede).replace('-',muro).replace('o',caminho).replace('p',port)
lab_jj = lab.replace('\n','jj').replace('a',coisa).replace('l',parede).replace('-',muro).replace('o',caminho).replace('p',port)
boneco_jj = boneco.replace('\n','jj').replace('a',coisa).replace('l',parede).replace('-',muro).replace('o',caminho).replace('p',port)

mold = "a+o".replace('a',coisa).replace('o',caminho)
mold2 = "o+a".replace('a',coisa).replace('o',caminho)
mold_cima = "o....................a".replace('a',coisa).replace('o',caminho)  #19+2+1
mold_baixo = "a....................o".replace('a',coisa).replace('o',caminho)  #12+2


portal_d = "ap".replace('a',coisa).replace('p',port)
portal_c = "p....................a".replace('a',coisa).replace('p',port)
portal_b = "a....................p".replace('a',coisa).replace('p',port)


def anda_d():
    # global porque é modificado
    global lab, boneco, boneco_jj, resultado
    resultado = re.search(mold,boneco_jj)
    if resultado != None:
        k = resultado.span()[0]
        boneco_jj = lab_jj[:k+1]+ coisa + lab_jj[k+2:]
        boneco = boneco_jj.replace('jj','\n')
        resultado = re.search(mold,boneco_jj)
        return(boneco)
    else:
        return("num ta vendo isso na direita?")

def anda_e():
    global lab, boneco, boneco_jj, resultado2
    resultado2 = re.search(mold2,boneco_jj)
    if resultado2 != None:
        k = resultado2.span()[1]
        boneco_jj = lab_jj[:k-2]+ coisa + lab_jj[k-1:]
        boneco = boneco_jj.replace('jj','\n')
        resultado2 = re.search(mold2,boneco_jj)
        return(boneco)
    else:
        return("num ta vendo isso na esquerda")

def anda_c():
    global lab, boneco, boneco_jj, resultado3
    resultado3 = re.search(mold_cima,boneco_jj)
    if resultado3 != None:
        k = resultado3.span()[0]
        boneco_jj = lab_jj[:k]+ coisa +lab_jj[k+1:]
        boneco = boneco_jj.replace('jj','\n')
        resultado3 = re.search(mold_cima,boneco_jj)
        return(boneco)
    else:
        return("num ta vendo isso em cima?")

def anda_b():
    global lab, boneco, boneco_jj, resultado4
    resultado4 = re.search(mold_baixo,boneco_jj)
    if resultado4 != None:
        k = resultado4.span()[1]
        boneco_jj = lab_jj[:k-1]+coisa+lab_jj[k:]
        boneco = boneco_jj.replace('jj','\n')
        resultado4 = re.search(mold_baixo,boneco_jj)
        return(boneco)
    else:
        return("num ta vendo isso em cima?")

def portal():
    resultport_d = re.search(portal_d,boneco_jj)
    resultport_c = re.search(portal_c,boneco_jj)
    resultport_b = re.search(portal_b,boneco_jj)
    if (resultport_d or resultport_c or resultport_b) != None:
        return(True)
    else:
        return(False)



def fechado():
    rfechado = re.search(coisa,boneco_jj)
    kk = rfechado.span()[0]
    sa = '\n'+boneco_jj[kk-1:kk+2]+'\n'
    sc = boneco_jj[kk-1-(19+2):kk+2-(19+2)]
    sb = boneco_jj[kk-1+(19+2):kk+2+(19+2)]
    return(sc+sa+sb)

#########################################Interface Gráfica######################################################
import PySimpleGUI as sg

# Define o conteúdo da janela

esboco = [[sg.Text("Controle",font='Calibri')],
          [sg.Button('   '), sg.Button('▲'), sg.Button('   ')],
          [sg.Button('◄'), sg.Button('   '), sg.Button('►')],
          [sg.Button('   '), sg.Button('▼'), sg.Button('   ')],
          [sg.Text('Sábio quadrado, onde está o seu colega?!',font='Calibri',size=(20,2))],
          #Para jogar com mapa aberto ----->boneco no lugar de fechado()
          #[sg.Text('{}'.format(boneco),size=(45,10),font='Calibri 14', key='-MAPA-')], 
          [sg.Text('{}'.format(fechado()),size=(6,3),pad=(40,0),font='Calibri 14', key='-MAPA-')],#pad=(20,0) 'Helvetica 11'
          [sg.Text('',size=(20,3),font='Calibri', key='-FINALIZACAO-')],
          [sg.Button('Tá chegando ajuda!'), sg.Button('Sair')]]


# Cria a janela
janela = sg.Window('Labiritítulo', esboco)

c = 0
while True:
    
    evento, valores = janela.read()
    if evento == "►":
        anda_d()
    if evento == "◄":
        anda_e()
    if evento == "▲":
        anda_c()
    if evento == "▼":
        anda_b()
    if evento == 'Tá chegando ajuda!':        
        janela['-FINALIZACAO-'].update('{}'.format("Soco{}rro!!".format(c*"o")))
        c = c + 1
    # Verificar se a janela foi fechada ou ver se o usuário deseja Sair 
    if evento == sg.WINDOW_CLOSED or evento == 'Sair':
        break
    # Resulta uma mensagem na janela
    janela['-MAPA-'].update('{}'.format(fechado()))
    if  portal() == True:
        janela['-FINALIZACAO-'].update('{}'.format("Muito obrigado por me encontrar ☺☺☺!!!"))

# Conclui removendo a janela da tela
janela.close()
