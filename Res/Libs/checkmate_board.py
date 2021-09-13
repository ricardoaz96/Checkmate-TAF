import pyautogui
import time
import wx
from PIL import Image
import logging
import numpy as np
import cv2
import winsound

# global driver related variables
current_driver = None
current_driver_index = -1
driver_list = []
screenshot_index = 1
wxinstance = wx.App()

# global test execution variables
turbo_mode = True

class checkmate_board: 

    def click(self, element):
        res, type = checkmate_board().get_element_identifier(element)
        if type == 'poi':
            x, y = res.split(',')
            pyautogui.click(int(x), int(y))
        if type == 'aoi':
            p1, p2 = res.split(';')
            p1x1, p1x2 = p1.split(',')
            p2x1, p2x2 = p2.split(',')
            intp1x1, intp1x2, intp2x1, intp2x2 = int(p1x1), int(p1x2), int(p2x1), int(p2x2)
            pyautogui.click(int((intp1x1+intp2x1)/2), int((intp1x2+intp2x2)/2))
        if type == 'xoi':
            #TODO
            #x, y = res.split(',')
            #pyautogui.click(int(x), int(y))
            #pyautogui.click(310,58)
            #pyautogui.press('backspace')
            #pyautogui.write('Hello world!')    
            #pyautogui.press('enter')
            #checkmate_board().wait_for_stability()
            #pyautogui.click(310,58)
            #pyautogui.press('backspace')
            #pyautogui.write('banana')    
            #pyautogui.press('enter')
            #checkmate_board().wait_for_stability()
            print("xoi not available at this moment")
        checkmate_board().wait_for_stability()

    def check(self, element):

        logging.info('Saving screenshot "temp 1"')
        checkmate_board().save_screenshot("temp1")
        large_image = cv2.imread('Res\\temp1.png')

        logging.info('Loading screenshot "element"')
        small_image = cv2.imread('C:\\Users\\riaze\\OneDrive\\Documentos\\CheckMate-QASI\\Example\\Res\\' + element + '.png')
        
        status = checkmate_board().check_if_image_contains_subimage(large_image, small_image)
        print(status)

    def write(self, text):
        pyautogui.write(text)  

    def press_key(self, key):
        if key == 'Enter':
            pyautogui.press('enter')
        elif key == 'Backspace':
            pyautogui.press('backspace')


    def wait_for_stability(self):

        max_cycles =0
        
        count_identical = 1

        while(count_identical!=3 or max_cycles == 20):
            
            logging.info('Saving screenshot "temp 1"')
            checkmate_board().save_screenshot("temp1")
            logging.info('Saving screenshot "temp 2"')
            checkmate_board().save_screenshot("temp2")

            im1 = Image.open('Res/temp1.png')
            im2 = Image.open('Res/temp2.png')

            logging.info('comparing screenshots...')
            if list(im1.getdata()) == list(im2.getdata()):
                count_identical = count_identical+1
                logging.info('identical')
            else:
                count_identical =0
                logging.info('different')


            max_cycles = max_cycles +1

        if (max_cycles==50):
            logging.error('Max cycles reached')
    
    def save_screenshot(self, filename):
        # Need to create an App instance before doing anything
        global wxinstance
        screen = wx.ScreenDC()
        size = screen.GetSize()
        bmp = wx.Bitmap(size[0], size[1])
        mem = wx.MemoryDC(bmp)
        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
        del mem  # Release bitmap
        bmp.SaveFile('Res/'+ filename +'.png', wx.BITMAP_TYPE_PNG)

    def get_element_identifier(self, element_name, oi_type=''):
        dir = "C:\\Users\\riaze\\OneDrive\\Documentos\\CheckMate-QASI\\01_Web\\Resources\\03_Elements.txt"
        textFile = checkmate_board().read_elements_file(dir)

        element_identifier_list = checkmate_board().get_element_identifier_list(textFile)
        #print (element_identifier_list)

        poi_available, aoi_available, xoi_available = False, False, False

        for dict in element_identifier_list:
            if dict['name']==element_name:
                #print(dict['name'])
                #print(dict['poi'])
                #print(dict['aoi'])
                #print(dict['xoi'])

                if oi_type=='':
                    if dict['aoi'] != None:
                        oi_type = 'aoi'
                    if dict['xoi'] != None:
                        oi_type = 'xoi'
                    if dict['poi'] != None:
                        oi_type = 'poi'

                if dict[oi_type] == None:
                    raise TypeError("'" + oi_type + "' is not defined for element '" + element_name + "'")
                else:
                    return dict[oi_type] , oi_type

            else:
                continue
        
        raise TypeError("'" + element_name + "' not found in elements file '" + dir + "'")

    def get_element_identifier_list(self, textfile):
        element_list = []

        element = {
        "name": None,
        "poi": None,
        "aoi": None,
        "xoi": None
        }

        textByLine = textfile.split("\n")

        for line in textByLine:
            if "#### " in line:
                continue
            elif not line.strip():
                continue
            else:
                linebyt = line.split("\t")
                
                element["name"] = linebyt[0]
                for cell in linebyt:
                    if ',' in cell and not ';' in cell and not '//' in cell :
                        element["poi"] = cell
                    elif ',' in cell and ';' in cell and not '//' in cell :
                        element["aoi"] = cell
                    elif '//' in cell :
                        element["xoi"] = cell

                #print("element_list" + str(element_list))
                element_list.append(element.copy())
                #print("element_list" + str(element_list))
                element["poi"] = None
                element["aoi"] = None
                element["xoi"] = None


        #print("final element_list" + str(element_list))
        return element_list


    def read_elements_file(self, filedir):
        f = open(filedir, "r")
        textFile = str(f.read())
        #print("what")
        #print(textFile)
        return textFile

    def get_element_coordinates(self):
        return '159,1066' , 'poi'

    def convert_txt_to_dict(self, txtfile):

        listByLine = txtfile.split("\n")
        element_list = []

        element = {
        "name": None,
        "poi": None,
        "aoi": None,
        "xoi": None
        }


        for item in listByLine:
            if "#### " in item:
                continue
            elif not item.strip():
                continue
            else:
                linebyt = item.split("\t")
                for item in linebyt:
                    print("cenas")


        #print(name_xpath_dict)
        return name_xpath_dict

    def check_if_image_contains_subimage(self, image, subimage):
        im = np.atleast_3d(image)
        tpl = np.atleast_3d(subimage)
        H, W, D = im.shape[:3]
        h, w = tpl.shape[:2]

        # Integral image and template sum per channel
        sat = im.cumsum(1).cumsum(0)
        tplsum = np.array([tpl[:, :, i].sum() for i in range(D)])

        # Calculate lookup table for all the possible windows
        iA, iB, iC, iD = sat[:-h, :-w], sat[:-h, w:], sat[h:, :-w], sat[h:, w:] 
        lookup = iD - iB - iC + iA
        # Possible matches
        possible_match = np.where(np.logical_and.reduce([lookup[..., i] == tplsum[i] for i in range(D)]))

        # Find exact match
        for y, x in zip(*possible_match):
            eleme = im[y+1:y+h+1, x+1:x+w+1]
            if np.all(eleme == tpl):
                return True

        raise TypeError("Element not visible in current screen")


def find_image(im, tpl):
    im = np.atleast_3d(im)
    tpl = np.atleast_3d(tpl)
    H, W, D = im.shape[:3]
    h, w = tpl.shape[:2]

    # Integral image and template sum per channel
    sat = im.cumsum(1).cumsum(0)
    tplsum = np.array([tpl[:, :, i].sum() for i in range(D)])

    # Calculate lookup table for all the possible windows
    iA, iB, iC, iD = sat[:-h, :-w], sat[:-h, w:], sat[h:, :-w], sat[h:, w:] 
    lookup = iD - iB - iC + iA
    # Possible matches
    possible_match = np.where(np.logical_and.reduce([lookup[..., i] == tplsum[i] for i in range(D)]))

    # Find exact match
    for y, x in zip(*possible_match):
        eleme = im[y+1:y+h+1, x+1:x+w+1]
        if np.all(eleme == tpl):
            return (y+1, x+1)

    raise Exception("Image not found")

def find_image_at_coordinates(im, tpl, x, y):
    find_image(im, tpl)

def play_sound():
    winsound.Beep(700, 2000)


#small_image = cv2.imread('C:\\Users\\riaze\\OneDrive\\Documentos\\CheckMate-QASI\\Example\\Res\\Screen1_crop.png')
#large_image = cv2.imread('C:\\Users\\riaze\\OneDrive\\Documentos\\CheckMate-QASI\\Example\\Res\\Screen1.png')

#print(find_image(large_image, small_image))
#print(find_image_at_coordinates(large_image, small_image, 144,282))

#txtfile = read_elements_file()
#convert_txt_to_dict(txtfile)

#print(checkmate_board().get_element_identifier('ChromeIcon'))
#print(checkmate_board().get_element_identifier('ex1'))
#print(checkmate_board().get_element_identifier('ex2'))
#print(checkmate_board().get_element_identifier('extuti'))
#checkmate_board().wait_for_stability()