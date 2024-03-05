import pyautogui
import time

pyautogui.PAUSE=0.5
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")



link="https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=805, y=882)
pyautogui.write("tukado2@gmail.com")
pyautogui.press("tab")
pyautogui.write("meuovo")
pyautogui.click(x=1402, y=1301)
import pandas
dados=pandas.read_csv("produtos.csv")

for linha in dados.index:
    
    pyautogui.click(x=893, y=593)
    pyautogui.write(dados.loc[linha,"codigo"])
    pyautogui.press("tab")

    pyautogui.write(dados.loc[linha,"marca"])
    pyautogui.press("tab")

    pyautogui.write(dados.loc[linha,"tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(dados.loc[linha,"categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(dados.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(dados.loc[linha,"custo"]))
    pyautogui.press("tab")
    
    if pandas.isna(dados.loc[linha,"obs"]) == True:
        pyautogui.write("Sem informacoes")
        pyautogui.press("tab")
        pyautogui.press("enter")
    else:
        pyautogui.write(dados.loc[linha,"obs"])
        pyautogui.press("tab")
        pyautogui.press("enter")
    pyautogui.scroll(99999)



