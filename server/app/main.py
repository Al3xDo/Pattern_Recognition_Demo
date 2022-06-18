import io
import os
from fastapi import FastAPI, UploadFile,Response, status
import torch
from PIL import Image
import torchvision.transforms as transforms
import logging
from fastapi.middleware.cors import CORSMiddleware
import torchvision.transforms as transforms
from torchvision.transforms import InterpolationMode

from app.wiki_parser import get_result
app = FastAPI()
LOG= logging.getLogger("INFO")
model=None
map_label = {
    0: "bamboo", 1: "banana", 2: "Cocoa_bean", 3: "cinnamon", 4: "coffeearabica",
    5: "Pitaya", 6: "durian", 7: "Plumeria", 8: "guava", 9: "jackfruit", 10: "lychee",
    11: "mango", 12: "mangosteen", 13: "nilam", 14: "papaya", 15: "passiflora", 16: "Manilkara zapota", 17: "Salak",
    18: "Carambola", 19: "Arenga pinnata", 20: "suweg", 21: "taro", 22: "vanilla", 23: "Syzygium samarangense", 24: "Black pepper", 25: "zodia"
}

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def file_is_validated(filename: str) -> bool:
    if filename.split(".")[-1] in ['jpg', 'jpeg', 'png']:
        return True
    return False

def _transform(image):
    transform_stages=[]
    size= int((256 / 224) * 224)
    transform_stages.append(transforms.Resize(size, interpolation=InterpolationMode.BICUBIC))
    transform_stages.append(transforms.CenterCrop(224))
    transform_stages.append(transforms.ToTensor())

    transform_pipline = transforms.Compose(transform_stages)
    tensor = transform_pipline(image)[None,:,:,:]
    return tensor

@app.on_event("startup")
def start_uo():
    """
    Load models
    """
    global model
    model= torch.jit.load('./app/weights/plant_classifier/swin.pt')
    model.eval()
    LOG.info("load model")


@app.post("/")
async def classifer(file: UploadFile, resp: Response):
    """
    Receive file and output the labels
    """
    if not file_is_validated(file.filename):
        resp.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return {"detail": "File type is not allowed"}
    image_bytes = await file.read()
    image= Image.open(io.BytesIO(image_bytes))
    tensor = _transform(image)
    res= torch.argmax(model(tensor))
    label =  map_label[res.item()]
    LOG.info(f'Label {label}')
    data= get_result(label)
    return {"label": label,
            "data": data}