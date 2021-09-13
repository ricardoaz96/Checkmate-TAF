import checklist_Transitions

class checklist_Elements:     
    def read_elements_file(self):
        f = open("01_Web/Resources/03_Elements.txt", "r")
        textFile = str(f.read())
        #print("what")
        #print(textFile)
        return textFile

    def turn_textFile_to_name_xpath_dict(self):
        textFile = checklist_Elements.read_elements_file(self)
        listByLine = textFile.split("\n")
        current_screen = ""
        name_xpath_dict = {}

        for item in listByLine:
            if "#### " in item:
                current_screen= item.replace("#### ", "")
            elif not item.strip():
                continue
            else:
                linebyt = item.split("\t")
                name_xpath_dict[current_screen+"_"+linebyt[0].replace(" ", "")] = linebyt[-1]

        #print(name_xpath_dict)
        return name_xpath_dict

    def get_xpath(self, name):
        name_xpath_dict = checklist_Elements.turn_textFile_to_name_xpath_dict(self)
        #print(name_xpath_dict)
        elementXPATH = name_xpath_dict.get(name, "None")
        
        if elementXPATH == "None":
            raise Exception("'" + name + "' not found in ScreenMapping dictionary")
        return elementXPATH

#print(get_xpath("Screen 1_Go_button"))