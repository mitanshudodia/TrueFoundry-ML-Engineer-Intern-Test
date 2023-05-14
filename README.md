# TrueFoundry-ML-Engineer-Intern-Test
This program is a service that acts as a  bridge between hugging face models deployed on TrueFoundry platform and the users using it, this program converts the user input into the v2 inference protocol format and call the TrueFoundry API and fetches and gives the result
## Getting Started
This are the instruction to set up the program and run it in your local machine
## Requirements
* Python 3.9 or above
* pip package installer
## Installation Guide
1. Clone the repository:

```
git clone https://github.com/mitanshudodia/TrueFoundry-ML-Engineer-Intern-Test.git
```
2. Create a virtual environment, activate it and navigate to TrueFoundry-ML-Engineer-Intern-Test:

```
cd TrueFoundry-ML-Engineer-Intern-Test
```
3. Install all the dependencies:

```
pip install -r requirements.txt
```
## Run the Service
```
python main.py --hf_pipeline <pipeline_name> --model_deployed_url <model_url>
```

Here you have to replace the pipeline name with the hugging face pipeline name for that particular model and the mode_url with the endpoints of your TrueFoundry deployed model
    
For Example running the server for the object-detection pipeline use this:

```
python main.py --hf_pipeline object-detection --model_deployed_url https://test-object-detect-intern-mitanshu-ws.tfy-ctl-euwe1-devtest.devtest.truefoundry.tech
```

Once the server is up and running for use you can send POST requests to http://localhost:8000/model_name to make predictions, here model_name is your model name available on TrueFoundry platform. The request body should follow the input format specified in the Hugging Face documentation for the respective pipeline.

## Example
For example running the model for Token Classification then using the image for object detection you have to follows these steps
1. Run the program with the pipeline name and your model endpoints

```
python main.py --hf_pipeline token-classification --model_deployed_url https://zero-intern-mitanshu.demo1.truefoundry.com
```
2. Code for making the request

```
import requests
import base64

#here instead of zero there will be your model name from TrueFoundry
API_URL = 'http://0.0.0.0:8000/zero'

def query():
    input_data = {
	"inputs": "My name is Sarah Jessica Parker but you can call me Jessica, I am a computer engineering student from mumbai",
    }
    response = requests.post(API_URL, json=input_data)
    return response

output = query()
print(output.json())
```
### output
```
["[{"entity": "B-Therapeutic_procedure", "score": 0.3455923795700073, "index": 17, "word": "computer", "start": 78, "end": 86}, {"entity": "I-Therapeutic_procedure", "score": 0.34528684616088867, "index": 18, "word": "science", "start": 87, "end": 94}, {"entity": "I-History", "score": 0.27888694405555725, "index": 19, "word": "engineering", "start": 95, "end": 106}, {"entity": "B-Nonbiological_location", "score": 0.9757474064826965, "index": 21, "word": "mumbai", "start": 110, "end": 116}]"]
```

## Example 2
For example running the model for Zero Shot Classification then using the image for object detection you have to follows these steps
1. Run the program with the pipeline name and your model endpoints

```
 python main.py --hf_pipeline zero-shot-classification --model_deployed_url https://zero-intern-mitanshu.demo1.truefoundry.com
 ```
2. Code for making the request

```
import requests
import base64

API_URL = 'http://0.0.0.0:8000/zero'

def query():
 
    input_data = {'inputs': 'Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!',
                  'candidate_labels': ["refund", "legal", "faq"]}
    response = requests.post(API_URL, json=input_data)
    return response
    
output = query()
print(output.json())

```
### output
```
{"sequence": "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!", "labels": ["refund", "faq", "legal"], "scores": [0.937849760055542, 0.04914167523384094, 0.013008514419198036]}
```

## Example 3
For example running the model for object detection then using the image for object detection you have to follows these steps
1. Run the program with the pipeline name and your model endpoints

```
python main.py --hf_pipeline object-detection --model_deployed_url https://test-object-detect-intern-mitanshu-ws.tfy-ctl-euwe1-devtest.devtest.truefoundry.tech
```
2. Code for making the request

```
import requests
import base64

API_URL = 'http://0.0.0.0:8000/test-object-detect'

def query(data):
    input_data = {'inputs': data}
    response = requests.post(API_URL, json=input_data)
    return response

with open('html.png', "rb") as f:
    data = base64.b64encode(f.read()).decode('utf-8')
    
output = query(data)
print(output.json())
```
### output
```
["[{"score": 0.9528601169586182, "label": "table", "box": {"xmin": 33, "ymin": 46, "xmax": 187, "ymax": 214}}]"]
```
