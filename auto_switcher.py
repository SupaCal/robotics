# VEX IQ Python-Project
import sys
import vexiq
import timer


timer = timer.Timer()
selectedSlot = 1;
timer.start()
SELECTED="◈ "
UNSELECTED="o "

def up():
    global selectedSlot
    if selectedSlot > 1:
        
        selectedSlot = selectedSlot - 1
        writePrograms()
def down():
    global selectedSlot
    if selectedSlot < len(programs):
        
        selectedSlot = selectedSlot + 1
        writePrograms()


def buttonPress():
    timer.reset()
    timer.start()
    
def isReady():
    if timer.elapsed_time() > 0.5:
        return True
    else:
        return False
def prog1():
    
    vexiq.sound_note(1)
def prog2():
    vexiq.sound_note(10)
programs = ({"name": "Program 1", "execp": prog1, "slot": 1}, {"name": "Program 2", "execp": prog2, "slot": 2})
def check():
    print("check", selectedSlot)
    programs[selectedSlot - 1]["execp"]()
    
def writePrograms():
    print("write", selectedSlot)
    for x in programs:
        if x["slot"] == selectedSlot:
            
            vexiq.lcd_write(SELECTED, x["slot"], 1)
            vexiq.lcd_write(x["name"], x["slot"], 3)
        else:
            vexiq.lcd_write(UNSELECTED, x["slot"], 1)
            vexiq.lcd_write(x["name"], x["slot"], 3)
writePrograms()
while True:
    if vexiq.is_down_button_pressed() == True and isReady() == True:
        buttonPress()
        down()
    if vexiq.is_up_button_pressed() == True and isReady() == True:
        buttonPress()
        up()
    if vexiq.is_check_button_pressed() == True and isReady() == True:
        buttonPress()
        check()
