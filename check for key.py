import keyboard, mouse, time
start=time.time()
while True:
    try:
        if keyboard.is_pressed('c'):
            mouse.click('left')
            #time.sleep(0.0001)
        
        if keyboard.is_pressed('v'):
            mouse.click('right')
            #time.sleep(0.0001)
    except:
        pass
