from collections import Counter
import csv
import random
import base64
import time
import os
from dotenv import load_dotenv


import baseten
# If you want to use gpt for free
import gpt4free.g4f as g4f


used_houses = []
load_dotenv()
# If you want to use gpt for free
g4f.debug.logging = True
g4f.check_version = False



def generateImage(name, dir, prompt="dog", w=1024, h=1024, negative_prompt="letters"):
    try:
        model = baseten.deployed_model_version_id(os.environ.get("SDXL_MODEL_ID"))

        request = {
            "prompt": prompt,
            "use_refiner": False,
            "steps":20,
            "negative_prompt":"letters, many images",
            "width":w, 
            "height":h,
        }

        response = model.predict(request)

        img=base64.b64decode(response["data"])

        img_file = open(f'{dir}/{name}.jpeg', 'wb')
        img_file.write(img)
        img_file.close()
    except:
        return False


def default_question_for_gpt(body):
    try:
        answer = ""
        response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {
                    "role": "user",
                    "content": body,
                }
            ],
            stream=True,
        )


        for message in response:
            answer += message
        return answer
    except:
        return False


def g4f_question_for_housing(house):
    try:
        answer = ""
        response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {
                    "role": "user",
                    "content": f"I want to create an Instagram post about engaging real estate content. Can you write text for this post? make it the most attractive, skip the information that may seem unattractive or that is not given to you. There is information about this house: {' '.join(f'{key}: {house[i]},' for i, key in enumerate(['price', 'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 'furnishingstatus']))[:-1]}",
                }
            ],
            stream=True,
        # provider=g4f.Provider.GptGo
        )


        for message in response:
            answer += message
        return answer
    except:
        return False


def get_random_house(csv_file_path):
    try:
        with open(csv_file_path, 'r') as file:
            # Create a CSV reader object
            csv_reader = csv.reader(file)
            
            # Convert the CSV reader to a list and skip the header if there is one
            lines = list(csv_reader)[1:]
            
            # Choose a random house from the list
            random_line = random.choice(lines)
            
        return random_line
    except:
        return False


