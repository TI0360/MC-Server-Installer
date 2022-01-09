import sys
import os
import windows
#import linux
import PySimpleGUI as sg

sg.theme('LightBlue')

if os.name == 'nt':
    windows.startup()

#elif os.name == 'posix':
    #linux.startup()

else:
    layout = [[sg.Text("サポートされていないOSで実行されたためアプリを終了します。")],
              [sg.Text("サポートOSは同封されているテキストファイルを参照してください。")]]
    window = sg.Window('起動エラー', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            sys.exit()
