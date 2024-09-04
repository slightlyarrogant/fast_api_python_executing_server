from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio

app = FastAPI()

class CodeInput(BaseModel):
    code: str

@app.post("/execute")
async def execute_code(code_input: CodeInput):
    try:
        # Create a new global namespace for execution
        namespace = {}
        
        # Execute the code asynchronously
        await asyncio.get_event_loop().run_in_executor(
            None, exec, code_input.code, namespace
        )
        
        # Check if 'result' is in the namespace
        if 'result' not in namespace:
            raise ValueError("The code didn't define a 'result' variable.")
        
        return {"result": namespace['result']}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)