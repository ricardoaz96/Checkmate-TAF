import time as t

# global driver related variables

# global test execution variables

class checklist_Utils:     

    def set_variable_up(self, variable, *items_to_be_replaced):
        for item in items_to_be_replaced:
            variable= variable.replace(item, "")
        return variable

    def wait(self, time):
        t.sleep(time)

print(checklist_Utils().set_variable_up("for 'Test'", "for ", "'"))