import PySimpleGUI as sg
import os
import time

logo = b"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" 

sg.theme("DarkAmber")

def_file = 'javal'
def_inter = f'{def_file}.py'

replaces = {#Principais:
            "->": "print", 
            "<-": "input",
            "[se]": "if",
            "[entao_se]": "elif",
            "[senao]": "else",
            "[sempre]": "while True",
            "[enquanto]": "while",
            #Condição
            "[menor]": "<",
            "[maior]": ">",
            "[igual]": "==",
            "[diferente]": "!="}

layout = [
    [sg.Text("Javal V2", font=("Arial", 22, 'bold'))],
    [sg.Text("Selecione o arquivo:")],
    [sg.InputText(def_file, key='txt', disabled=False,text_color="black", background_color="white", expand_x=50), sg.Button("Selecionar!", button_color="red", font=("Arial", 10, "bold"))],
    [sg.Multiline(key='text', default_text="Selecione um arquivo para começar!", size=(80, 25), auto_refresh=True, text_color="white",
                  background_color=("#2b2b33"), font=("Arial", 12, ""))],
    [sg.Button("Salvar", key='btn'), sg.Button("Executar!", key="exec")]
]

window = sg.Window("Javal", layout=layout, icon=logo)

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break
    
    if event == 'btn':
       with open(f"{def_file}.txt", "w", encoding="utf-8") as file2:
          file2.write(value['text'])
       
       with open(f"{def_file}.py", 'w', encoding="utf-8") as file:
           content = value['text']
           for old, new in replaces.items():
            content = content.replace(old, new) 
           file.write(content)
        
    if event == 'exec':
        try:
            os.system(f"start cmd /k py {def_file}.py")
            os.system('cls')
        except SyntaxError:
           sg.popup_error_with_traceback("Erro na execução :(", "Corrija essa parada ai...")
        
        #exec(open("execute.py").read())

    if event == "Selecionar!" and value['txt']!='':
        def_file = str(value['txt'])
        window['Selecionar!'].update(button_color='green')

        try:
            with open(f"{def_file}.txt", 'r'):
                pass  # Se abrir o arquivo com sucesso, significa que ele existe
            file_exists = True
        except FileNotFoundError:
            file_exists = False

        if file_exists == False:
            window['text'].update(value="Criando arquivos, aguarde!!")
            time.sleep(2)
            with open(f"{def_file}.txt", 'w') as file:
              file.write("")
              with open(f"{def_file}.py", 'w') as fyp:
                 fyp.write("")
            window['text'].update(value="Arquivos criados, finalizando configurações...")
            time.sleep(3)
            window['text'].update(value=open(f"{def_file}.txt").read())
        else:
            window['text'].update(value="Arquivo encontrado! Carregando código...")
            time.sleep(5)
            window['text'].update(value=open(f"{def_file}.txt").read())
           

window.close()