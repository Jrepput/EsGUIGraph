import PySimpleGUI as sg

i = 0

f = open("test.txt", "r")

BAR_WIDTH = 25
BAR_SPACING = 20
EDGE_OFFSET = 0
GRAPH_SIZE = (550,500)
DATA_SIZE = (500,300)

graph = sg.Graph(GRAPH_SIZE, (150,0), DATA_SIZE, background_color='black',)

layout = [[graph],
          [sg.Button('OK')]]

window = sg.Window('Grafico', layout)



while True:
    before_value = 0
    event, values = window.Read()
    graph.Erase()
    if event is None:
        break

    for x in f:
      n = int(x)

      graph.DrawLine(((i-1) * BAR_SPACING + EDGE_OFFSET+ BAR_WIDTH/2 ,  before_value)  ,  (i * BAR_SPACING + EDGE_OFFSET+ BAR_WIDTH/2 , n ),color='green', width=1 )
   
      graph.DrawText(text=n, color="green", location=(i*BAR_SPACING+EDGE_OFFSET+2, n)) 

      graph.DrawPoint((i * BAR_SPACING + EDGE_OFFSET+ BAR_WIDTH/2 ,n), size=5 ,color='green',)
      before_value = n
      i+=1
        
window.Close()