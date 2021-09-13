from datetime import date
from robot.libraries.BuiltIn import BuiltIn
import logging

debug_mode = False

class checklist_Logging:     
    def startup_checklist_configuration(self):
        debug_mode = BuiltIn().get_variable_value("${DEBUG_MODE}")
        print("######################")        
        print("TEST RUN CONFIGURATION")
        print("######################")        
        #logging.debug('Watch out!') 
        logging.info('TEST RUN CONFIGURATION:')
        logging.info('PROJECT:' + "Test")
        logging.info('TEST EXECUTION:' + "SQA Checklist")
        logging.info('DEBUG MODE:' + debug_mode)
        logging.info('DATE :' + checklist_Logging.get_current_date(self))
        #logging.warning('Watch out!') 
        #logging.error('Watch out!') 
        #logging.critical('Watch out!')

    def get_current_date(self):
        #print(date)
        return str(date)

    def teardown_checklist(self):
        #TODO: edit html report for personalized content and add data in table
        return False