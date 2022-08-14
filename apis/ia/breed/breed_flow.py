from utils.utils import jsonify
from skimage.metrics import structural_similarity as compare_ssim
import cv2
import urllib.request
import numpy as np
import io
import PIL.Image as Image
import pandas as pd
import json
import requests

class BreedFlow:

    def __call__(self, request):

        # Flujo de IA
        path_pet_img = 'apis/ia/img/pet_client.jpg'
        image_client = request.files["pet_image"]
        image_client.save(path_pet_img)
        image = cv2.imread(path_pet_img)
        image = image / 255.0

        image = image.astype(np.float32)
        image = np.expand_dims(image, axis=0)

        labels_path = "apis/ia/csv/labels.csv"
        labels_df = pd.read_csv(labels_path)
        breed = labels_df["breed"].unique()
        id2breed = {i: name for i, name in enumerate(breed)}

        #start_time = time.time()

        url = "https://petsbreed7app.herokuapp.com/v1/models/petsbreed7:predict"
        #url = "http://localhost:8501/v1/models/petsbreed7:predict"

        data = json.dumps({"signature_name":"serving_default","instances":image.tolist()})
        headers = {"content-type":"application/json"}
        response = requests.post(url, data=data, headers=headers)
        prediction = json.loads(response.text)

        breed_estimation = prediction["predictions"][0]
        label_idx = np.argmax(breed_estimation)
        breed_name = id2breed[label_idx]

        #print(prediction["predictions"][0])
        print(breed_name)


        return jsonify({"raza":format(breed_name)})

