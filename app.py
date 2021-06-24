from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import time
import getpass
chromedriver_autoinstaller.install()
import pickle


pequena = True
media = True
grande = True
extrema = False
lista_coletas = [[pequena, media, grande, extrema], [15, 6, 3, 2], ['pequena', 'media', 'grande', 'extrema']]

lanceiro = '100'
espada = '200'
barbaro = '0'
cavalaria_leve = '0'
cavalaria_pesada = '0'
lista_tropas = [[lanceiro, espada, barbaro, cavalaria_leve, cavalaria_pesada], ['lanceiro', 'espada', 'barbaro', 'cavalaria_leve', 'cavalaria_pesada']]
lista_velha_tropas = [lanceiro, espada, barbaro, cavalaria_leve, cavalaria_pesada]
def tempo(browser):
    lista_tempo = []
    for tipo_coleta in lista_coletas[2]:
        if lista_coletas[0][lista_coletas[2].index(tipo_coleta)]==True:      
            time.sleep(3)
            try:
                tempo_string = browser.execute_script("""
                    return document.getElementsByClassName('return-countdown')[%d].innerText        
                """%(lista_coletas[2].index(tipo_coleta)))
                var_hora = int(tempo_string[0:1])
                var_min = int(tempo_string[2:4])
                var_seg = int(tempo_string[5:7])
                conversao = ((var_hora*60)+(var_min)+(var_seg/60))*60
                lista_tempo.append(conversao)
            except:
                lista_tempo.append(1)
        lista_tempo.append(1)
    return max(lista_tempo)

def verificar_tropas(browser, lista):
    time.sleep(3)
    for tropa in lista[1]:
        qtde = browser.execute_script("""
                return document.getElementsByClassName('units-entry-all squad-village-required')[%d].innerText        
            """%(lista[1].index(tropa)))
        #browser.find_element_by_xpath('//a[@class="units-entry-all squad-village-required"][%d]'%(lista[1].index(tropa))).text
            
        qtde = qtde.replace('(','').replace(')','')
        if lista[0][lista[1].index(tropa)] == 'all':
            lista[0][lista[1].index(tropa)] = qtde
        else:
            if int(lista[0][lista[1].index(tropa)]) >int(qtde):
                lista[0][lista[1].index(tropa)] = qtde
            else:
                pass
        print('Tropas p/ coleta:', lista[0][lista[1].index(tropa)])

def startandoColetas(browser):
    dados_coleta = definindoColetas()
    for tipo_coleta in lista_coletas[2]:
        if lista_coletas[0][lista_coletas[2].index(tipo_coleta)]==True:
            i=0
            for tropas in dados_coleta[lista_coletas[2].index(tipo_coleta)]:
                time.sleep(3)
                if tropas!=None:
                    entry = None
                    while entry is None:
                        try:
                            print('contagem inputs: ', i)
                            entry = browser.find_elements_by_tag_name('input')
                            entry[i].clear()
                            entry[i].send_keys(tropas)
                            i+=1
                        except:
                            pass
            try:
                browser.execute_script('''
                    document.getElementsByClassName("btn btn-default free_send_button")[0].click()
                ''')
                pass
            except: 
                pass

def Calculo():
    soma=0
    i=0
    for tipo_coleta in lista_coletas[0]:
        if tipo_coleta == True:
            soma+=lista_coletas[1][i]
        i+=1
    return soma

def definindoColetas():
    total_coletas = Calculo()
    i=0
    lista = []
    for tipo_coleta in lista_coletas[0]:
        globals()[lista_coletas[2][i]] = []
        if tipo_coleta == True:
            for tropas in lista_tropas[0]:
                if tropas!='':
                    globals()[lista_coletas[2][i]].append(int((int(tropas)*lista_coletas[1][i])/total_coletas))
        lista.append(globals()[lista_coletas[2][i]])
        i+=1

    return lista   

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\faria\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
options.add_argument('--profile-directory=Default')
browser = webdriver.Chrome(chrome_options=options)
browser.get('https://www.tribalwars.com.br/')
'''
titulo_coleta = None
while titulo_coleta is None:
    try:
        titulo_coleta = browser.execute_script("""
            return document.getElementsByClassName('title')[0].innerText;
        """)
    except:
        pass
while browser.current_url != 'https://br105.tribalwars.com.br/game.php?village=459&screen=place&mode=scavenge':
    pass

while True:
    menor_tempo = tempo(browser)
    print('Faltam apenas '+str(menor_tempo)+ ' segundos')
    try:
        time.sleep(menor_tempo)
    except:
        pass
    time.sleep(3)
    verificar_tropas(browser, lista_tropas)
    startandoColetas(browser)
    for tropa in lista_tropas[1]:
        lista_tropas[0][lista_tropas[1].index(tropa)] = lista_velha_tropas[lista_tropas[1].index(tropa)]'''

    