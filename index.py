import PySimpleGUI as sg

replaces = {"->": "print", 
            "<-": "input",
            "se": "if",
            "entao_": "el",
            "casoContrario": "else"}

layout = [
    [sg.Text("Javal V1", font=("Arial", 22, 'bold'))],
    [sg.Multiline(key='text', default_text=open("javal.txt").read(), size=(50, 30))],
    [sg.Button("Salvar", key='btn'), sg.Button("Executar!", key="exec")]
]

window = sg.Window("Javal", layout=layout)

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break
    
    if event == 'btn':
       with open("javal.txt", "w") as file2:
          file2.write(value['text'])
       
       with open("execute.py", 'w') as file:
           content = value['text']
           for old, new in replaces.items():
            content = content.replace(old, new) 
           file.write(content)
        
    if event == 'exec':
        exec(open("execute.py").read())




window.close()
