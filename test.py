import requests
import base64

#API_URL = 'http://0.0.0.0:8000/zero'
#this is the endpoints of text generatino server hosted as as a service on TrueFoundry
API_URL = 'https://fastapi-intern-mitanshu-8000.demo1.truefoundry.com/zero'

def query():
    
 #input for zero shot classification
#     input_data = {'
# 	inputs': 'Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!',
#       'candidate_labels': ["refund", "legal", "faq"]
# 	}

    #input for token classification and text genetation
    input_data = {
	"inputs": "My name is Sarah Jessica Parker but you can call me Jessica and I am studying computer science engineering in Mumbai",
    }

    #input for object detection
    # input_data = {'inputs': data}

    response = requests.post(API_URL, json=input_data)
    return response

with open('html.png', "rb") as f:
    data = base64.b64encode(f.read()).decode('utf-8')
    
output = query(data)
print(output.json())

