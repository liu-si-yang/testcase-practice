from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "practice 项目启动成功"}
