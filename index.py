import PySimpleGUI as sg
import os


sg.theme("DarkAmber")

def_file = 'javal.txt'
def_inter = 'execute.py'

replaces = {"->": "print", 
            "<-": "input",
            "(se)": "if",
            "(entao_se)": "elif",
            "(senao)": "else"}

layout = [
    [sg.Text("Javal V2", font=("Arial", 22, 'bold'))],
    [sg.Text("Selecione o arquivo .txt:")],
    [sg.InputText(def_file, key='txt', disabled=False,text_color="black", background_color="white"), sg.Button("Selecionar!", button_color="red")],
    [sg.InputText(def_inter, key='py', disabled=False,text_color="black", background_color="white"), sg.Button("Selecionar!", button_color="red")],
    [sg.Multiline(key='text', default_text=open("javal.txt").read(), size=(50, 30), auto_refresh=True, text_color="white", selected_text_color=("black"),
                  background_color=("#2b2b33"))],
    [sg.Button("Salvar", key='btn'), sg.Button("Executar!", key="exec")]
]

window = sg.Window("Javal", layout=layout)

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break
    
    if event == 'btn':
       with open("javal.txt", "w", encoding="utf-8") as file2:
          file2.write(value['text'])
       
       with open("execute.py", 'w', encoding="utf-8") as file:
           content = value['text']
           for old, new in replaces.items():
            content = content.replace(old, new) 
           file.write(content)
        
    if event == 'exec':
        try:
            os.system("start cmd /k py execute.py")
            os.system('cls')
        except SyntaxError:
           sg.popup_error_with_traceback("Erro na execução :(", "Corrija essa parada ai...")
        
        #exec(open("execute.py").read())

    if event == 'test':
       print(value['file-txt'],'\n',value['file-python'])


window.close()
