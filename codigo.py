import pyautogui
import pandas
import time
# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> pressionar uma tecla
# pyautogui.write() -> rescrever algo
# pyautogui.hotkey -> combinação de teclas de atalho
# pyautogui.PAUSE = segundos
# pyautogui.position -> posição cartesiana do mouse 
# pyautogui.scroll ->

pyautogui.PAUSE= 0.5

pyautogui.press('win')
pyautogui.write('google')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

pyautogui.sleep(3)
pyautogui.click(x=868, y=483)
pyautogui.write('gabriellourenco@hotmMOLO000251ail.com')
pyautogui.press('tab')
pyautogui.write('teste123')
pyautogui.press('enter')

pyautogui.sleep(3)


tabela= pandas.read_csv("produtos.csv")
for linha in tabela.index:
    pyautogui.click(x=709, y=322)
    codigo= tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    pyautogui.press('tab')
    marca= tabela.loc[linha,"marca"]
    pyautogui.write(marca)
    pyautogui.press('tab')
    tipo= tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)
    pyautogui.press('tab')
    categoria= str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    preco_unitario= str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')
    custo= str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press('tab')
    obs= str(tabela.loc[linha,"obs"])
    pyautogui.write(obs)
    pyautogui.click(x=924, y=635 ,clicks=2, interval=0.8, button='left')


    pyautogui.scroll(10000)

pyautogui.FailSafeException