from ctypes.wintypes import DWORD
import pyautogui as pg
import pyperclip as pc
import time



def text_to_historic() :
    pg.hotkey('ctrl', 'c')
    texto = pc.paste()
    caminho = input("assunto: ")
    obj = open('safe.txt','a')
    obj.write(f"\n {caminho} \n {texto}")
    obj.close()
    print(texto)
    
def code_teste() :
    pg.hotkey('ctrl', 'c')
    texto = pc.paste()
    caminho = input("assunto: ")
    obj = open('teste.py','a')
    obj.write(f"\n {caminho} \n {texto}")
    obj.close()
    print("Saved code.")

def run_teste() :
    caminho = ""
    pg.hotkey('ctrl', 'c')
    texto = pc.paste()
    obj = open('run.py','w')
    obj.write(texto)
    obj.close()
    print("Running code...")
    pg.press('win')
    time.sleep(3)
    pg.write('anaconda')
    time.sleep(1)
    pg.press('enter')
    time.sleep(7)
    pg.write(f'cd {caminho}')
    time.sleep(1)
    pg.press('enter')
    time.sleep(1)
    pg.write('python run.py')
    time.sleep(1)
    pg.press('enter')

def position() :
    x, y = pg.position()
    obj = open('position.txt','a')
    #obj.write("x = "+str(x)+" y = "+str(y))
    obj.write(f"x = {x} y = {y} \n ")
    obj.close()
    position_ = f"{x}, {y}"
    print("Position ok", position_)


