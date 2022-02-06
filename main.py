import eel

eel.init('web')

@eel.expose
def js_says(x):
    print('Js says',x)

eel.start('index.html',mode='chrome-app', size=(300, 200), block=False)  # Start

t=0
while True:
    eel.sleep(1)
    eel.py_says(t)
    t += 1
