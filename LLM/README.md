## Setup
### Python Virtual Environment
Create a new virtual environment (venv):
```ps
python -m venv .venv
```

Use the venv in the current terminal (Windows):
```ps
.venv\Scripts\activate
```

### Installing packages
```ps
pip install -r requirements.txt
```

### Create requirements.txt file
A requirements.txt file has been generated using pipreqs.

Install pipreqs:
```ps
pip install pipreqs
```
Create requirements.txt file:
```ps
pipreqs /path/to/project
```

### local config file
Add a local.config.json file to the root of the LLM folder with the following content:
 - The ENDPOINT and the API_KEY are available at:
  [02242-openai-resource](https://portal.azure.com/#@dtudk.onmicrosoft.com/resource/subscriptions/d775b440-d558-4fd3-b687-5d042b57911a/resourceGroups/02242-program-analysis/providers/Microsoft.CognitiveServices/accounts/02242-openai-resource/cskeys)
  
```json
{
    "AZURE_OPENAI_ENDPOINT": <ENDPOINT>,
    "AZURE_OPENAI_KEY": <API_KEY>,
    "AZURE_OPENAI_DEPLOYMENT_NAME": "gpt-4"
}
```