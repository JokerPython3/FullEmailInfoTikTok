from passkey import main,usernamep
from Email2Username import ks
from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
app = FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
temp = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
async def index(request: Request):
    return temp.TemplateResponse("index.html",{"request":request})
@app.post("/info",response_class=HTMLResponse)
async def info(request: Request, email : str = Form(...)):
    username = ks.Email2UsernameTikTok(email).get_ksj().get("username","")
    data = main.Passkey(email).get_passkey()
    data.update({"username":username})
    return temp.TemplateResponse("info.html",{"request":request,"data":data})
