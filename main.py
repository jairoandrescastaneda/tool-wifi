from wifi import Cell

allssid = list(Cell.all('wlp3s0'))

for cell in allssid:
    print(cell.ssid)