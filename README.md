# FastAPI Code Executor

This project is a FastAPI server that accepts Python code via POST requests and returns the value of the `result` variable defined in the submitted code.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Setup Instructions

1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the project directory:
   ```
   cd /home/bogdan/Desktop/fastapi_server
   ```

3. Create a virtual environment:
   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   - On Linux or macOS:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Server

1. Make sure you're in the project directory and your virtual environment is activated.

2. Start the FastAPI server:
   ```
   python code_executor.py
   ```

3. The server will start running on `http://0.0.0.0:8000`.

## Using the API

You can send POST requests to `http://0.0.0.0:8000/execute` with JSON payloads containing Python code.

### Example using curl:

```bash
curl -X POST "http://0.0.0.0:8000/execute" \
     -H "Content-Type: application/json" \
     -d '{"code": "result = 2 + 2"}'
```

This should return:

```json
{"result": 4}
```

### Example using Python requests:

```python
import requests

url = "http://0.0.0.0:8000/execute"
payload = {"code": "result = 2 + 2"}
response = requests.post(url, json=payload)
print(response.json())
```

## API Documentation

You can access the interactive API documentation by opening `http://0.0.0.0:8000/docs` in your web browser.

## Security Notice

This server executes arbitrary Python code, which can pose significant security risks. It is intended for demonstration and development purposes only. Do not use this in a production environment or expose it to untrusted inputs without implementing proper security measures.