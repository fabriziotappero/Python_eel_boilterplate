import eel

eel.init('web')
eel.start('index.html',mode='chrome-app', size=(300, 200), block=False)

# list of Python functions that GUI can use to send stuff
@eel.expose
def talk_to_py(x):
    print('Receiving:', x)

t=0
while True:
    eel.sleep(1)
    eel.talk_to_gui(t) # function defined in index.html
    t += 1