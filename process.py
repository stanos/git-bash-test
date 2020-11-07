import PySimpleGUI as gui
import json
with open("pereference.dll", 'r') as f:
    data = json.loads(f.read())
    print(data["valid_username"])
with open("valid_username.dll", 'r') as g:
    data1 = json.loads(g.read())
info = data1
gui.theme(data["background_color"])
layout = [
    [gui.Text(data["text_1"])],
    [gui.Text(data["text_2"]), gui.InputText()],
    [gui.Button(data["button_text_1"]), gui.Button(data["button_text_2"])]]
window = gui.Window('username', layout)
pairs = data.items()
while True:
    event, values1 = window.read()
    if event == gui.WIN_CLOSED or event == data["button_text_2"]: # if user closes window or clicks cancel
        print("program closed!")
        break
    print('You entered ', values1[0])
    if values1[0] in data1:
        layout4 = [
            [gui.Text('searching for username...')],
            [gui.ProgressBar(100, orientation='h', size=(20, 20), key='progressbar')],
            [gui.Cancel()]
        ]
        window4 = gui.Window('loading...', layout4)
        progress_bar = window4['progressbar']
        for i in range(100):
            event, values = window4.read(timeout=10)
            if event == 'Cancel'  or event == gui.WIN_CLOSED:
                break
            progress_bar.UpdateBar(i + 1)
        val = values1[0] 
        layout2 = [
            [gui.Text(data["text_3"])],
            [gui.Text(data["text_4"]), gui.InputText()],
            [gui.Button(data["button_text_3"]), gui.Button(data["button_text_4"])]]
        window2 = gui.Window('password', layout2)
        while True:
            event, values = window2.read()
            if event == gui.WIN_CLOSED or event == data["button_text_4"]: # if user closes window or clicks cancel
                print("program closed!")
                break
            window2.close()
            window.close()
            print('You entered ', values[0])
            for keyval in data1:
                if values[0] == info[values1[0]]:
                    layout5 = [
                    [gui.Text('loading...')],
                    [gui.ProgressBar(200, orientation='h', size=(20, 20), key='progressbar1')],
                    [gui.Cancel()]
                    ]
                    window5 = gui.Window('loading...', layout5)
                    progress_bar = window5['progressbar1']
                    for i in range(200):
                        event, values = window5.read(timeout=10)
                        if event == 'Cancel'  or event == gui.WIN_CLOSED:
                            break
                        progress_bar.UpdateBar(i + 1)
                    print("log in succes")
                    layout3 = [
                    [gui.CBox('check me!!!', key='_check_', enable_events=True)],
                    [gui.Button("ok")],
                    [gui.Menu([['&File', ['&Open', '&Save', '&Exit',]],['&Edit', ['&Paste', ['&Special', '&ormal',], '&Undo'],],['&Help', '&About...'],['theme', ['&green', '&yellow', '&blue']]])],
                    [gui.Combo(['choise1', 'choise2'], enable_events=True, key="com")],
                    [gui.Slider(range=(0,500),
                    default_value=0,
                    size=(20,15),
                    orientation='horizontal',
                    font=('Helvetica', 12),
                    enable_events=True,
                    key="slide")]
                    ]
                    window3 = gui.Window('check', layout=layout3, resizable=True).finalize()
                    window3.Maximize()
                    while True:
                        event, values = window3.read()
                        check = window3.FindElement('_check_').get()
                        com = window3.FindElement('com').get()
                        if check == True:
                            print(com) 
                        elif com == "choise1":
                            print("hoi")  
                        elif com == "choise2":
                            print("hallo")       
                        if event == 'Exit':
                            window3.close()
                        elif event == "Open":
                            gui.FileBrowse('Browse')
                        elif event == "slide":
                            print(values['slide'])
                        elif event == 'green':
                            layout4 = [
                            [gui.CBox('check me!!!', key='_check_', enable_events=True)],
                            [gui.Button("ok")],
                            [gui.Menu([['&File', ['&Open', '&Save', '&Exit',]],['&Edit', ['&Paste', ['&Special', '&ormal',], '&Undo'],],['&Help', '&About...'],['theme', ['&green', '&yellow', '&blue']]])],
                            [gui.Combo(['choise1', 'choise2'], enable_events=True, key="com")],
                            [gui.Slider(range=(0,500),
                            default_value=0,
                            size=(20,15),
                            orientation='horizontal',
                            font=('Helvetica', 12))]
                            ]
                            window3.close()
                            gui.theme('green')
                            window3 = gui.Window('check', layout=layout4, resizable=True).finalize()
                            window3.Maximize() 
                            print("theme changed to green")                           
                        elif event == 'yellow':
                            layout5 = [
                            [gui.CBox('check me!!!', key='_check_', enable_events=True)],
                            [gui.Button("ok")],
                            [gui.Menu([['&File', ['&Open', '&Save', '&Exit',]],['&Edit', ['&Paste', ['&Special', '&ormal',], '&Undo'],],['&Help', '&About...'],['theme', ['&green', '&yellow', '&blue']]])],
                            [gui.Combo(['choise1', 'choise2'], enable_events=True, key="com")],
                            [gui.Slider(range=(0,500),
                            default_value=0,
                            size=(20,15),
                            orientation='horizontal',
                            font=('Helvetica', 12))]
                            ]
                            window3.close()
                            gui.theme("lightyellow")
                            window3 = gui.Window('check', layout=layout5, resizable=True).finalize()
                            window3.Maximize()
                            print("theme changed to lightyellow")
                        elif event == 'blue':
                            layout6 = [
                            [gui.CBox('check me!!!', key='_check_', enable_events=True)],
                            [gui.Button("ok")],
                            [gui.Menu([['&File', ['&Open', '&Save', '&Exit',]],['&Edit', ['&Paste', ['&Special', '&ormal',], '&Undo'],],['&Help', '&About...'],['theme', ['&green', '&yellow', '&blue']]])],
                            [gui.Combo(['choise1', 'choise2'], enable_events=True, key="com")],
                            [gui.Slider(range=(0,500),
                            default_value=0,
                            size=(20,15),
                            orientation='horizontal',
                            font=('Helvetica', 12))]
                            ]
                            window3.close()
                            gui.theme("BlueMono")
                            window3 = gui.Window('check', layout=layout6, resizable=True).finalize()
                            window3.Maximize()
                            print("theme changed to BlueMono")
                        if event == gui.WIN_CLOSED or event == "ok": # if user closes window or clicks cancel
                            print("program closed!")
                            break
                    window3.close()
                    window2.close()
                    window.close()
                    print("done")
                    break
                else:
                    print("ERROR: invalid password")
                    gui.popup("ERROR: invalid password", text_color="red", keep_on_top=True)
                    break
    else:
        print("ERROR: invalid username")
        gui.popup("ERROR: invalid username", text_color="red", keep_on_top=True)
        break
window.close()