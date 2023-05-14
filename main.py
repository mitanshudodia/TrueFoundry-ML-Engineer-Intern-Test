from fastapi import FastAPI, HTTPException
import argparse
import uvicorn
from v2_converter import convert_to_v2_input
import requests
from pydantic import BaseModel

app = FastAPI()

parser = argparse.ArgumentParser()
parser.add_argument("--hf_pipeline", type=str, help="Hugging Face pipeline name")
parser.add_argument("--model_deployed_url", type=str, help="URL of the deployed model")
args = parser.parse_args()
pipeline_name = args.hf_pipeline
model_deployed_url = args.model_deployed_url

class Input(BaseModel):
    inputs: str
    candidate_labels: list = None

@app.post("/{model_name}")
async def read_item(model_name, input_data:Input):
    '''This function converts the input in v2 protocol format and make request to TrueFoundry model and returns the response'''
    err_msg = None
    try:
        if not pipeline_name:
            err_msg = 'pipeline name not found'
            raise

        if not model_deployed_url:
            err_msg = 'model url not found'
            raise
        
        #this line converts the input to v2 format
        body = convert_to_v2_input(pipeline_name, input_data)
        url = model_deployed_url + f'/v2/models/{model_name}/infer'
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        response = requests.post(url, json=body, headers=headers)

        try:
            output = response.json()['outputs'][0]['data']
            return output
        
        except:
            return response.json()
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error while fetching data and the error is {err_msg}. Exception is {e}')


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)