# coding: utf-8
import sys
import PySimpleGUI as sg
import linux_download

sg.theme('LightBlue')


def grand():
    layout = [[sg.Text("ビルドするSpigotのバージョンを選択してください。")],
              [sg.Combo(['latest', '1.17.1', '1.16.5', '1.15.2', '1.14.4', '1.13.2', '1.12.2', '1.11.2', '1.10.2', '1.9.4', '1.8.8'], default_value="latest", size=(30, 1), key='version')],
              [sg.Text("使用するJavaを選択してください。※選択しない場合はシステムのデフォルトで規定されているJavaを使用します。")],
              [sg.InputText('ファイルパス', key='-file-'), sg.FilesBrowse('Java読み込み', target='-file-', file_types=(('EXEファイル', '*.exe'),))],
              [sg.Text("※ビルドには時間を要します。")],
              [sg.Button('開始', key='start'), sg.Button('終了', key='exit')]]

    window = sg.Window('バージョン選択', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            sys.exit()

        if event == 'start':
            if "java" not in values['-file-']:
                java = 'java'
                linux_download.spigot(values['version'], java)

            else:
                java = values['-file-']
                linux_download.spigot(values['version'], java)

        if event == 'exit':
            sys.exit()
