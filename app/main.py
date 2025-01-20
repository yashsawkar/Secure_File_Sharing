# filepath: /Users/yashsawkar/Desktop/secure_file_sharing/app/main.py
from fastapi import FastAPI
from app.routes import client_user, ops_user

app = FastAPI()

app.include_router(client_user.router, prefix="/client-user", tags=["client_user"])
app.include_router(ops_user.router, prefix="/ops-user", tags=["ops_user"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)