from fastapi import FastAPI,HTTPException
import uvicorn
from meowchatterbot import *

app = FastAPI()

@app.get("/chatterbot")
def conversation(user_name:str,query:str):
     try:
        return {"response":"hello"}
     except Exception as e:
      #   send_email("sandeepnamjoshi95@gmail.com","bczhvhftvbilcjqt","pallavi@noborderz.com","Not getting response","There is some issue in an api")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    