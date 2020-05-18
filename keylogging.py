# keylogger using pynput module 


import pynput 
from pynput.keyboard import Key, Listener 

def on_press(key): 
    
 
    
    try: 
        #print('alphanumeric key {0} pressed'.format(type(key.char))) 
        if key.char=='w':
            print('up', end='\r')
        elif key.char=='a':
            print('Left',end='\r')
        elif key.char=='s':
            print('Down',end='\r')
        elif key.char=='d':
            print('right',end='\r')

        
    except AttributeError: 
        print('special key {0} pressed'.format(key)) 
        
            
def on_release(key): 
                    
    if key == Key.esc: 
        # Stop listener 
        return False


with Listener(on_press = on_press, 
            on_release = on_release) as listener: 
                    
    listener.join() 
