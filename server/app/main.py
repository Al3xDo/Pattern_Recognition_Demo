import io
from fastapi import FastAPI, UploadFile,Response, status
import torch
from PIL import Image
import torchvision.transforms as transforms
import logging
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
LOG= logging.getLogger("INFO")
model=None
map_label = {
    0: "bamboo", 1: "banana", 2: "cacao", 3: "cinnamon", 4: "coffeearabica",
    5: "dragonfruit", 6: "durian", 7: "frangipani", 8: "guava", 9: "jackfruit", 10: "lychee",
    11: "mango", 12: "mangosteen", 13: "nilam", 14: "papaya", 15: "passiflora", 16: "sawo", 17: "snakefruit",
    18: "starfruit", 19: "sugarpalm", 20: "suweg", 21: "taro", 22: "vanilla", 23: "waterguava", 24: "whitepepper", 25: "zodia"
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
    print(file.filename)
    image= Image.open(io.BytesIO(image_bytes))
    new_image = image.resize((224, 224))
    transform = transforms.ToTensor()
    tensor = transform(new_image)[None,:,:,:]
    res= torch.argmax(model(tensor))
    return {"label": map_label[res.item()] }