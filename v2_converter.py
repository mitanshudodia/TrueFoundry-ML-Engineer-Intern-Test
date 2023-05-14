from fastapi import HTTPException

def convert_to_v2_input(hf_pipeline, input_data):
    '''this function converts the normal json input into v2 protocol format'''
    if hf_pipeline == "zero-shot-classification":
        v2_input = {
            "inputs": [
                {
                    'name':"sequences",
                    'shape':[-1],
                    'datatype':"BYTES",
                    'parameters':{"content_type": "str"},
                    'data':input_data.inputs,
                },
                {
                    'name':"candidate_labels",
                    'shape':[-1],
                    'datatype':"BYTES",
                    'parameters':{"content_type": "str"},
                    'data':input_data.candidate_labels,
                },
            ],
            "outputs": [],
        }

    elif hf_pipeline == "object-detection":
            v2_input = {
                "inputs": [
                {
                    'name':"inputs",
                    'shape':[-1],
                    'datatype':"BYTES",
                    'parameters':dict(content_type="pillow_image"),
                    'data': input_data.inputs,
                }
                ],
                "outputs": [],
            }

    elif hf_pipeline == "text-generation":
        v2_input = {
            "inputs": [
                {
                    'name':"text_inputs",
                    'shape':[-1],
                    'datatype':"BYTES",
                    'parameters':{"content_type": "str"},
                    'data':input_data.inputs,
                }
            ],
            "outputs": [],
        }

    elif hf_pipeline == "token-classification":
        v2_input = {
            "inputs": [
                {
                    'name':"inputs",
                    'shape':[-1],
                    'datatype':"BYTES",
                    'parameters':{"content_type": "str"},
                    'data':input_data.inputs,
                }
            ],
            "outputs": [],
        }

    else:
        #if the pipeline is not knows
        raise HTTPException(status_code=400, detail="Unsupported pipeline")

    return v2_input