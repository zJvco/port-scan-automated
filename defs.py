import requests
from path_list import path

def main(win, simpleGUI):
    while True:
        event, values = win.read()

        if event == simpleGUI.WIN_CLOSED or event == "Quit":
            break

        if event == "button1":
            if searchTool(win, values["-INPUT-"]) == False:
                win["-INPUT-"].update("URL INVÁLIDA!")

    win.close()


def searchTool(win, host):
    try:
        for p in path:
            req = requests.get(host + p)
            url = req.url

            if req.status_code == 200:
                print(
                    f"Foi descoberto um diretório: {url} - Status: {req.status_code}")

            win.refresh()
        print("Escaneamento finalizado...")
    except:
        return False