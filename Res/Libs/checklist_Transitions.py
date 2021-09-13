import robot
from robot.libraries.BuiltIn import BuiltIn
import logging as log

class checklist_Transitions:

    #global variable
    reversed_list = []
    current_from_screen = "landingScreen"
    temp_current_from_screen = "landingScreen"

    # Go
    # Purpose: Transition between system screens according to 'ScreenMapping.txt'.
    # Arguments: from_screen; to_screen;
    # Args Meaning: screen to start transition from; screen where system ends;
    # Example 1: Go    from LandingScreen    to SettingsScreen
    # Example 2: Go    to SettingsScreen

    def go(self, from_or_to_screen="", to_screen=""):
        temp_current_from_screen=to_screen

        # input data validations
        if "from " in from_or_to_screen:
            from_screen = from_or_to_screen.replace("from ", "")
            if "to " in to_screen:
                to_screen = to_screen.replace("to ", "")
            else:
                raise Exception("[Not Defined] Please define a \"to\" screen")
        elif "to " in from_or_to_screen:
            to_screen = from_or_to_screen.replace("to ", "")
            from_screen = checklist_Transitions.current_from_screen
        elif from_or_to_screen == "":
            raise Exception("[Not Defined] Please define a \"to\" screen")

        # getting initial screen to end screen branch
        checklist_Transitions.startup(self, from_screen, to_screen)
        screen_to_screen_branch = checklist_Transitions.get_final_branch(from_screen, to_screen)
        transitions_list = checklist_Transitions.get_to_keyword(self, screen_to_screen_branch)

        # run transitions from 'from' screen to 'to' screen
        for transition in transitions_list:
            suiteName = BuiltIn().get_variable_value("${SUITE NAME}")
            dir = suiteName.split(".")
            platformdir = dir[1].replace(" ", "_")
            BuiltIn().import_resource('${EXECDIR}' + "//" + platformdir + "//Resources//02_TransitionKws.robot")
            BuiltIn().run_keyword(transition)

        # set last screen as current from screen
        last_screen = transition.split(" to ")
        checklist_Transitions.current_from_screen = last_screen[1]

    def startup(self, from_screen, to_screen):

        # read ScreenMapping.txt for specific platform folder
        suiteName = BuiltIn().get_variable_value("${SUITE NAME}")
        dir = suiteName.split(".")
        platform = dir[1].replace(" ", "_")
        execDir = BuiltIn().get_variable_value("${EXECDIR}")

        # read file to string
        f = open( execDir + "\\" +platform+"\\Resources\\04_ScreenMapping.txt", "r")
        file = f.read()

        # generate list_screens and list_level with screens and their level (max=0)
        file_lines = file.split("\n")
        list_screens = []
        list_level = []
        for line in file_lines:
            level = line.count("\t")
            list_screens.append(str(line.replace("\t", "")))
            list_level.append(str(level))

        #verify screens existence
        if from_screen not in list_screens and to_screen not in list_screens:
            raise Exception("[Not Defined] \"from\" (\"" + from_screen + "\") and \"to\" (\"" + to_screen + "\") Screens not defined in Screen Mapping file (" + execDir + "\\" +platform+"\\03_Elements\\ScreenMapping.txt" + ")")
        if from_screen not in list_screens:
            raise Exception("[Not Defined] \"from\" Screen \""+from_screen+"\" not defined in Screen Mapping file (" + execDir + "\\" +platform+"\\03_Elements\\ScreenMapping.txt" + ")")
        if to_screen not in list_screens:
            raise Exception("[Not Defined] \"to\" Screen \""+to_screen+"\" not defined in Screen Mapping file (" + execDir + "\\" +platform+"\\03_Elements\\ScreenMapping.txt" + ")")

        # get lowest level in min_level
        min_level = 0
        for index in range(len(list_screens) - 1, 0, -1):
            if int(list_level[index]) > int(min_level):
                min_level = list_level[index]

        # get absolut tree list for each screen
        absolute_tree_list = []
        for index in range(len(list_screens) - 1, -1, -1):
            current_level = list_level[index]
            current_tree = list_screens[index] + "|"
            while (int(current_level) != 0):
                for index2 in range(index, -1, -1):
                    if (int(list_level[index2]) == int(current_level) - 1):
                        current_level = str(int(current_level) - 1)
                        current_tree = current_tree + list_screens[index2] + "|"

            absolute_tree_list.append(current_tree)


        # get absolute_tree_list (reversed)
        global reversed_list
        reversed_list = []
        for item in absolute_tree_list:
            current_list = item.split("|")
            current_list.remove("")
            current_list.reverse()
            reversed_list.append("|".join(current_list))

        reversed_list.reverse()


    def get_final_branch(fromScreen, toScreen):
        #print("fromScreen")
        #print(fromScreen)
        #print("toScreen")
        #print(toScreen)
        global reversed_list
        final_branch=""
        for item in reversed_list:
            if item.endswith(fromScreen):
                ##print("from Branch:")
                ##print(item)
                fromScreenBranch = item
            if item.endswith(toScreen):
                ##print("to Branch:")
                ##print(item)
                toScreenBranch = item

        fromBranchInToBranch = fromScreenBranch in toScreenBranch
        toBranchInFromBranch = toScreenBranch in fromScreenBranch

        if fromBranchInToBranch and not toBranchInFromBranch:
            # Same Branch From Higher To Lower Level
            #print("Same Branch From Higher To Lower Level")
            #print(toScreenBranch[toScreenBranch.find(fromScreen):])
            final_branch = toScreenBranch[toScreenBranch.find(fromScreen):]

        elif not fromBranchInToBranch and toBranchInFromBranch:
            # Same Branch From Lower To Higher Level
            #print("Same Branch From Lower To Higher Level")
            temporary = fromScreenBranch[fromScreenBranch.find(toScreen):].split("|")
            temporary.reverse()
            finalbranch = "|".join(temporary)
            #print(finalbranch)
            final_branch = finalbranch

        elif not fromBranchInToBranch and not toBranchInFromBranch:
            # Different Branches
            #print("Different Branches")
            temporaryfrom = fromScreenBranch.split("|")
            temporaryfrom.reverse()
            temporaryfrombranch = "|".join(temporaryfrom)
            temporaryto = toScreenBranch
            #print(temporaryfrombranch)
            #print(temporaryto)

            #print("branches with accessWithin Level: landingScreen|#accessWithinLevel")
            branchesWithAccessWithinLevel = []
            for item in reversed_list:
                if item.endswith("#accessWithinLevel"):
                    screen = item.split("|")[-2]
                    if(screen in temporaryfrombranch.split("|") and screen in temporaryto.split("|")):
                        branchesWithAccessWithinLevel.append(screen)

            final_branch= temporaryfrombranch
            #print(temporaryfrombranch)
            #print(temporaryto)

            for item2 in temporaryto.split("|"):
                if item2 not in temporaryfrombranch.split("|"):
                    final_branch = final_branch + "|" + item2

            #remove screen with access
            for screen in branchesWithAccessWithinLevel:
                if (screen in final_branch.split("|")):
                    temp = final_branch.split("|")
                    temp.remove(screen)
                    final_branch = "|".join(temp)


            #print(final_branch)


        return final_branch

    def get_to_keyword(self, final_branch):
        tokeywords = []
        for index in range (len(final_branch.split("|"))):
            if index != (len(final_branch.split("|"))-1):
                tokeywords.append(final_branch.split("|")[index] + " to " + final_branch.split("|")[index+1])
        #print("tokeywords")
        #print(tokeywords)
        return tokeywords

    def get_skeleton(self):
        global list_screens
        global min_level, list_level
        #print("SKELETON: all screens")
        all_transitions = []

        all_children_list = []
        #get transitions with access within level
        for index in range(0, len(list_screens)):
            if list_screens[index] == "#accessWithinLevel":
                father_level = list_level[index-1]
                children_list = []
                for index2 in range(index, len(list_screens)):
                    if int(list_level[index2])==int(father_level)+1 and list_screens[index2] != "#accessWithinLevel":
                        children_list.append(list_screens[index2])
                    if int(list_level[index2])==int(father_level) or index2 == len(list_screens)-1:
                        all_children_list.append(children_list)
                        break
        #print("all_children_list")
        #print(all_children_list)

        for index in range(0, len(list_screens)):
            if list_screens[index] != "#accessWithinLevel":
                #print("screen: " + list_screens[index] + " [" + list_level[index] + "]")
                temp_transitions = get_to_keyword(get_final_branch("landingScreen", list_screens[index]))
                #print("temp_transitions:")
                #print(temp_transitions)
                for item in temp_transitions:
                    if not item in all_transitions:
                        all_transitions.append(item)
                        reversed_item_list = item.split(" to ")
                        all_transitions.append(reversed_item_list[1] + " to " +  reversed_item_list[0])

        # add access within level transitions to all_transitions

        for item in all_children_list:
            for screen in item:
                for screen2 in item:
                    if screen != screen2:
                        transition = screen + " to " + screen2
                        if not transition in all_transitions:
                            all_transitions.append(transition)


        all_transitions_sorted = []
        for index in range(0, len(list_screens)):
            if list_screens[index] != "#accessWithinLevel":
                for item in all_transitions:
                        if list_screens[index] in item.split(" to "):
                            if not item in all_transitions_sorted:
                                all_transitions_sorted.append(item)

        #sorted transitions by level
        #all_transitions_sorted = []
        #for indexOfScreen in range (0, int(min_level)):
        #    print(indexOfScreen)
        #    for index in range(0, len(list_screens)):
        #        print(list_screens[index])
        #        print(list_level[index])
        #        if list_screens[index] != "#accessWithinLevel":
        #            if str(indexOfScreen) == list_level[index]:
        #                for item in all_transitions:
        #                    if list_screens[index] in item.split(" to "):
        #                        if not item in all_transitions_sorted:
        #                            all_transitions_sorted.append(item)

        #print("all_transitions:")
        #print(all_transitions)

        #print("all_transitions sorted:")
        #print(all_transitions_sorted)
        return all_transitions_sorted

    def get_skeleton_file(self):
        # get all transitions skeleton
        # fromScreen to toScreen

        skeleton = get_skeleton()

        with open("Output.txt", "w") as text_file:
            txt_file = ""
            for index in range(0, len(skeleton)):
                if index != len(skeleton) - 1:
                    txt_file = txt_file + skeleton[index] + "\n" + "Log    Going from " + skeleton[index] + "\n\n"
                else:
                    txt_file = txt_file + skeleton[index] + "\n" + "Log    Going from " + skeleton[index] + "\n"
            text_file.write(txt_file)
    
    def get_current_screen(self):
        return self.temp_current_from_screen

    def set_current_screen(self, screen):
        checklist_Transitions.current_from_screen = screen
        checklist_Transitions.temp_current_from_screen = screen