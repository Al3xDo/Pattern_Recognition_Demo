from fastapi import FastAPI
import torch
from PIL import Image
import torchvision.transforms as transforms

app = FastAPI()
model=None
map_label = {0: "bamboo", 1: "banana", 2: "cacao", 3: "cinnamon", 4: "coffeearabica",\
    5: "dragonfruit", 6: "durian", 7: "frangipani", 8: "guava", 9: "jackfruit", 10: "lychee",
    11: "mango", 12: "mangosteen", 13: "nilam", 14: "papaya", 15: "passiflora", 16: "sawo", 17: "snakefruit",\
    18: "starfruit", 19: "sugarpalm", 20: "suweg", 21: "taro", 22: "vanilla", 23: "waterguava", 24: "whitepepper", 25: "zodia"}    
@app.on_event("startup")
def start_uo():
    """
    Load models
    """
    global model
    model= torch.jit.load('./app/weights/plant_classifier/swin.pt')
    model.eval()

@app.get("/")
async def root():
    image = Image.open('./app/13.jpg')
    new_image = image.resize((224, 224))
    transform = transforms.ToTensor()
    tensor = transform(new_image)[None,:,:,:]
    res= torch.argmax(model(tensor))
    return map_label[res.item()]