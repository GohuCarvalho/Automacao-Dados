import pyautogui
import time
import pandas as pd

pyautogui.pause = 1.5


link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(5)

pyautogui.hotkey("ctrl", "l")
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(5)


pyautogui.click(x=615, y=413) 
time.sleep(1)

pyautogui.write("hugo@email.com")
pyautogui.press("tab")

pyautogui.write("1234")
pyautogui.press("enter")

time.sleep(5)


tabela = pd.read_csv("produtos.csv")
print(tabela)


for linha in tabela.index:

    pyautogui.scroll(5000)
    time.sleep(0.5)

    pyautogui.click(x=619, y=298)
    time.sleep(1)

    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")

    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs == "nan":
        pyautogui.write("sem observações")
    else:
        pyautogui.write(obs)

    pyautogui.press("enter")
    time.sleep(2)

