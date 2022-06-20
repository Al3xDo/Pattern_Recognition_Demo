import time
import torch
from PIL import Image
import torchvision.transforms as transforms
from torchvision.transforms import InterpolationMode
import cv2
import keras
def _transform(image):
    transform_stages=[]
    size= int((256 / 224) * 224)
    transform_stages.append(transforms.Resize(size, interpolation=InterpolationMode.BICUBIC))
    transform_stages.append(transforms.CenterCrop(224))
    transform_stages.append(transforms.ToTensor())

    transform_pipline = transforms.Compose(transform_stages)
    tensor = transform_pipline(image)[None,:,:,:]
    return tensor

INFERENCE_TIME= {}


def predict_torch_model(model_name='swin_transformer'):
    image= Image.open("./test_inferencetime/test_image.jpg")
    INFERENCE_TIME[model_name]= [0]*10
    model= torch.jit.load('./test_inferencetime/weights/swin.pt')
    model.eval()
    tensor = _transform(image)
    with torch.no_grad():
        for i in range(10):
            start = time.time()
            torch.argmax(model(tensor))
            INFERENCE_TIME[model_name][i] = time.time() - start

def predict_keras_model( model_name="mobilenet"):
    image= cv2.imread("./test_inferencetime/test_image.jpg")
    img = cv2.resize(image,(224,224))     # resize image to match model's expected sizing
    img = img.reshape(1,224,224,3)
    INFERENCE_TIME[model_name]= [0]*10
    mobilenet=keras.models.load_model(f"./test_inferencetime/weights/{model_name}.keras")
    for i in range(10):
        start = time.time()
        mobilenet.predict(img)
        INFERENCE_TIME[model_name][i] = time.time() - start

predict_keras_model("vgg16")
for k in INFERENCE_TIME.keys():
    print(f'{k} - {sum(INFERENCE_TIME[k]) / 10}')