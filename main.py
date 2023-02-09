import PySimpleGUI as sg
import random




layout = [
    
    [sg.Output(size = (300,2))],
    [sg.Text()],
    [sg.Text('Raiz :')],
    [sg.Input(size = (10,1), key = "raiz")],
    [sg.Button('Começar'), sg.Button('Enviar')]

    ]


window = sg.Window('Raiz', layout = layout, size = (350,180))



while True :
    event, values = window.read()
    x = random.randint(1,100)

    if event == sg.WIN_CLOSED:
        break

    if event == 'Começar' :
        print('Descubra a raiz de ', x*x )

    while True :

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Começar' :
            print('Descubra a raiz de ', x*x )
        
        if event == 'Enviar' :
            raiz = values['raiz']
            raizn = int(raiz)
            if raizn == x :
                print('Você acertou!')
                break
            else :
                print('Você errou, a resposta era', x)
                break
