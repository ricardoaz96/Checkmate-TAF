import requests
import time as t

# global driver related variables

# global test execution variables

class checklist_Server:     

    def authentication(self):
        print("todo: authentication")

    def perform_action(self, action, **params):
        self.get_request_parameters(action)

    def get_request_parameters(self, action):
        f = open( "C:\\Users\\riaze\\Desktop\\SQA Checklist\\Project\\Checklist\\03_Server\\Resources\\Actions\\"+action+".txt", "r")
        file = f.read()
        print(file)

        request_section = file[file.find("Request:"): file.find("Response:")]

        response_section = file[file.find("Response:"):]

    def wait(self, time):
        t.sleep(time)

#checklist_Server().perform_action("divide") 

#url="http://www.dneonline.com/calculator.asmx"
#headers = {'content-type': 'text/xml; charset=utf-8'}
##headers = {'content-type': 'text/xml'}
#body = """<?xml version="1.0" encoding="utf-8"?>
#<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#  <soap:Body>
#    <Divide xmlns="http://tempuri.org/">
#      <intA>5</intA>
#      <intB>5</intB>
#    </Divide>
#  </soap:Body>
#</soap:Envelope>"""
#
#response = requests.post(url,data=body,headers=headers)
#print (response.content)