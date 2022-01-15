# coding: utf-8
import urllib.request
import json
import requests
import sys
import PySimpleGUI as sg
import windows_content

sg.theme('LightBlue')
version = "v1.1"


url = 'https://api.github.com/repos/TI0360/MC-Server-Installer/releases'
session = requests.Session()
req = session.get(url)
req.close()
res = json.loads(req.text)
latest = res[0]["tag_name"]


def startup():
    if latest != version:
        downloadurl = 'https://github.com/TI0360/MC-Server-Installer/releases/latest/download/MCSI.exe'
        save_name = f'MCSI_{latest}.exe'
        urllib.request.urlretrieve(downloadurl, save_name)

        layout = [[sg.Text("アプリを最新版にアップデートしました。")],
                  [sg.Text(f"{save_name}で起動し直してください。")],
                  [sg.Button('終了', key='exit')]]

        window = sg.Window('アップデート完了', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                sys.exit()

            if event == 'exit':
                sys.exit()

    else:
        windows_content.grand()
