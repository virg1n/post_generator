from dotenv import load_dotenv
from PIL import Image, ImageDraw
import requests
from io import BytesIO
import os

load_dotenv()
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY")

)

def question(body):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": body,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return response.choices[0].message.content



def question_for_housing(house):
    answer = ""
    response = client.chat.completions.create(
        messages=[
            {   
                "role":"user",
                "content":f"I want to create an Instagram post about engaging real estate content. Can you write text for this post? make it the most attractive, skip the information that may seem unattractive or that is not given to you. There is information about this house: price: 3395000, area: 3450, bedrooms: 3, bathrooms: 1, stories: 1, mainroad: yes, guestroom: no, basement: yes, hotwaterheating: no, airconditioning: no, parking: 2, prefarea: no, furnishingstatus: unfurnished",
                "role":"assistant",
                "content":"🏡 Dream Home Alert 🌟\n\nStep into your very own paradise with our latest listing! This stunning house is guaranteed to make all your real estate dreams come true! ✨\n\n💰 Price: $3,395,000\n📐 Area: 3,450 sqft\n🛏️ Bedrooms: 3\n🛁 Bathrooms: 1\n📚 Stories: 1\n\n📍 Located right off the main road, this home ensures convenience and easy access with out sacrificing tranquility. \n\n🚗 With its two parking spaces, you'll never have to worry about finding a spot for your vehicles again!\n\n🏠 Boasting a spacious basement, you'll have plenty of room for storage and endless possibilities for customization. \n\n💧 Enjoy the comfort of a hot water heating system throughout the house, delivering warmth during those chilly winter months.\n\n❄️ While there is no air conditioning, the open floor plan and ample windows allow for great airflow, keeping you cool and refreshed all yeaar round. \n\n🛋️ The house comes unfurnished, giving you the opportunity to add your personal touch and create a space that truly reflects your style and personality. \n\n🌳 Alt hough it doesn't have a guestroom, the layout ensures that your family and friends will always feel welcome and comfortable during their stay.\n\n✨ While this property might not be in a preferred area, it offers incredible potential to create the home of your dreams at an amazing value!\n\nSounds like the perfect fit? Don't miss out on this amazing opportunity! DM us for more details or to arrange a showing. ✉️📞\n\n#DreamHome #RealEstateOpportunity #UnfurnishedBeauty #HomeSweetHome",
                "role": "user",
                "content": f"I want to create an Instagram post about engaging real estate content. Can you write text for this post? make it the most attractive, skip the information that may seem unattractive or that is not given to you. There is information about this house: {' '.join(f'{key}: {house[i]},' for i, key in enumerate(['price', 'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 'furnishingstatus']))[:-1]}",
            }
        ],
        model="gpt-3.5-turbo",
    )
    return response.choices[0].message.content



def image1024(body):
    response = client.images.generate(
    model="dall-e-3",
    prompt=body,
    size="1024x1024",
    quality="standard",
    n=1,
    )
    image_url = response.data[0].url
    return image_url


def saveImg1024(prompt, name, directory):
    url = image1024(prompt)
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.save(f'{directory}/{name}.png')
    return url

