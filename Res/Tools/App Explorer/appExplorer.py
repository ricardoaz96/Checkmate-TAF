import tkinter as tk
import pyautogui
import wx
import os, shutil
import math
from PIL import Image, ImageDraw
from pynput.keyboard import Listener

screen_count = 1
element_count = 1
area_counter_click = 1
temp_pos_area_1_x = None
temp_pos_area_1_y = None
wxinstance = wx.App()

countFocus = 0
focused = True

def delete_files_in_folder():
    folder = 'Res'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def save_screenshot(filename):
    # Need to create an App instance before doing anything
    global wxinstance
    screen = wx.ScreenDC()
    size = screen.GetSize()
    bmp = wx.Bitmap(size[0], size[1])
    mem = wx.MemoryDC(bmp)
    mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
    del mem  # Release bitmap
    bmp.SaveFile('Res/'+ filename +'.png', wx.BITMAP_TYPE_PNG)

def save_screenshot_of_element_by_area(filename, x1, y1, x2, y2):

    # Need to create an App instance before doing anything
    global wxinstance
    screen = wx.ScreenDC()
    size = screen.GetSize()
    bmp = wx.Bitmap(size[0], size[1])
    mem = wx.MemoryDC(bmp)
    mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
    del mem  # Release bitmap
    bmp.SaveFile('Res/'+ filename +'.png', wx.BITMAP_TYPE_PNG)

    with Image.open('Res/'+ filename +'.png') as img:
    
        shape = [(int(x1), int(y1)), (int(x2), int(y2))]
        
        # create rectangle image
        img1 = ImageDraw.Draw(img)  
        img1.rectangle(shape, outline ="red", width = 5)
        #img.show()
        img.save('Res/'+ filename +'.png')

def save_screenshot_of_element_by_point():

    # Need to create an App instance before doing anything
    global wxinstance
    screen = wx.ScreenDC()
    size = screen.GetSize()
    bmp = wx.Bitmap(size[0], size[1])
    mem = wx.MemoryDC(bmp)
    mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
    del mem  # Release bitmap
    bmp.SaveFile('Res/'+ filename +'.png', wx.BITMAP_TYPE_PNG)

    with Image.open('Res/'+ filename +'.png') as img:
    
        shape = [(1, 1), (2, 2)]
        
        # create rectangle image
        img1 = ImageDraw.Draw(img)  
        img1.rectangle(shape, outline ="red", width = 5)
        img.show()

def click_add_screen():
    global buttonAdd, screen_count, entryScreenText
    currentvalue = entryScreenText.get(1.0, tk.END)
    currentvalue = currentvalue + "Screen" + str(screen_count) + " = " + "\n"
    entryScreenText.delete(1.0, tk.END)
    finaltext = currentvalue.lstrip().split("\n")
    finaltext.remove("")

    entryScreenText.insert(1.0, '\n'.join(finaltext))
    entryScreenText.yview_moveto('1.0')

    save_screenshot('Screen'+str(screen_count))

def move(x,y):
    pyautogui.moveTo(x, y)

def move_while_click(x, y):
    pyautogui.dragTo(x, y, button='left') 

    #### PythonScreen

    currentvalue = entryPOIText.get(1.0, tk.END)
    currentvalue = currentvalue + "####" + "Screen" + str(screen_count) + "\n"
    entryPOIText.delete(1.0, tk.END)
    finaltext = currentvalue.lstrip().split("\n")
    finaltext.remove("")

    entryPOIText.insert(1.0, '\n'.join(finaltext))
    entryPOIText.yview_moveto('1.0')


    screen_count = screen_count + 1

start_was_clicked = False 
def start_click():
    global start_was_clicked
    start_was_clicked = True
    window.wm_state('iconic')
    #window.iconify()



# interface creation
window = tk.Tk()

# frame add screen
"""
frame = tk.Frame(window)
frame.rowconfigure(0, minsize=50)
frame.columnconfigure([0], minsize=50)
buttonAdd = tk.Button(frame, text="Start", width=15, height=0, bg="orange", fg="white", command = start_click)
buttonAdd.grid(row=0, column=0)
frame.pack()
"""

# frame for screens and pois
frame3 = tk.Frame(window)
frame3.rowconfigure(0, minsize=200)
frame3.columnconfigure([0], minsize=200)
entryScreenText = tk.Text(frame3, width=50, height=10, font=("Helvetica", 8))
entryScreenText.grid(row=0, column=0)
frame3.pack()

# frame for screens and pois
frame3 = tk.Frame(window)
frame3.rowconfigure(0, minsize=200)
frame3.columnconfigure([0], minsize=200)
entryPOIText = tk.Text(frame3, width=50, height=10, font=("Helvetica", 8))
entryPOIText.grid(row=0, column=0)
frame3.pack()

# Export frame
frame = tk.Frame(window)
frame.rowconfigure(0, minsize=50)
frame.columnconfigure([0], minsize=50)
button = tk.Button(frame, text="Export", width=15, height=0, bg="blue", fg="white")
button.grid(row=0, column=0)
frame.pack()

# controls labels
w = tk.Label(window, text="\n add screen: + \n poi: * \n aoi: ª\n")
w.pack()

def key_control_q(e=None):
    global element_count
    print(pyautogui.position())
    currentvalue = entryPOIText.get(1.0, tk.END)
    currentvalue = currentvalue + "ex" + str(element_count) + "\t\t\t" + str(pyautogui.position().x) + "," + str(pyautogui.position().y) + "\n"
    entryPOIText.delete(1.0, tk.END)
    finaltext = currentvalue.lstrip().split("\n")
    finaltext.remove("")

    entryPOIText.insert(1.0, '\n'.join(finaltext))
    entryPOIText.yview_moveto('1.0')

    element_count = element_count + 1


def key_control_w(e=None):
    global area_counter_click, temp_pos_area_1_x, temp_pos_area_1_y, element_count

    if (area_counter_click==1):
        temp_pos_area_1_x = pyautogui.position().x
        temp_pos_area_1_y = pyautogui.position().y
        print("waiting for click of area 2...")
        area_counter_click = 2
    elif (area_counter_click==2):
        #print(pyautogui.position())
        currentvalue = entryPOIText.get(1.0, tk.END)
        currentvalue = currentvalue + "ex" + str(element_count) + "\t\t\t" + str(temp_pos_area_1_x) + "," + str(temp_pos_area_1_y) + ";" + str(pyautogui.position().x) + "," + str(pyautogui.position().y) + "\n"
        entryPOIText.delete(1.0, tk.END)
        finaltext = currentvalue.lstrip().split("\n")
        finaltext.remove("")
        entryPOIText.insert(1.0, '\n'.join(finaltext))
        entryPOIText.yview_moveto('1.0')
        save_screenshot_of_element_by_area("ex" + str(element_count), str(temp_pos_area_1_x), str(temp_pos_area_1_y), str(pyautogui.position().x), str(pyautogui.position().y))
        area_counter_click = 1
        element_count = element_count + 1
        


def on_press(key):
    #print("PRESSED", key)
    if (str(key) == "'+'"):
        print("+")
        click_add_screen()
    if (str(key) == "'*'"):
        print("*")
        key_control_q()
    if (str(key) == "'ª'"):
        print("ª")
        key_control_w()

listener = Listener(on_press=on_press)

start = False
stop = False 
def key_control_p(e=None):
    global start, listener, stop
    #listener.start()
    start = True
    
    


started = False

def handle_focus_in(event):
    if event.widget == window:
        global started
        if (not started):
            listener.start()
            started = True



#def handle_focus_out(event):
#    if event.widget == window:
#        print("I have gained defocus")
#        global start_was_clicked, started
#        
#        if (not start_was_clicked):
#            print('not clicked')
#            return
#        else: 
#            if not started:
#                listener.start()
#                listener.join()
#                started = True
#            else:
#                if (not listener.is_alive()):
#                    listener.run()
            
    
# bind control + c and control + a 
#window.bind('<Control-q>', key_control_q)
#window.bind('<Control-w>', key_control_w)

#window.bind('<Control-p>', key_control_p)
window.bind("<FocusIn>", handle_focus_in)
#window.bind("<FocusOut>", handle_focus_out)

delete_files_in_folder()

#waiting for events
window.mainloop()