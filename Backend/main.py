from collections import Counter
import csv
import random
import base64
import time
import os
from dotenv import load_dotenv


# If you want to use gpt for free


from functions import question, question_for_housing, saveImg1024
try:
    from functions_for_g4f import generateImage, default_question_for_gpt, g4f_question_for_housing
except:
    pass

load_dotenv()
# If you want to use gpt for free


filename = "Housing.csv"

def get_random_house(csv_file_path):
    with open(csv_file_path, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Convert the CSV reader to a list and skip the header if there is one
        lines = list(csv_reader)[1:]
        
        # Choose a random house from the list
        random_line = random.choice(lines)
        
    return random_line




def generate_posts_with_g4f(number_of_posts, generate_images=False, directory_for_images='imgs'):

    texts_for_posts, path_for_imgs, used_houses, urls = [], [], [], []
    if not os.path.exists(directory_for_images):
        os.makedirs(directory_for_images)
    for i in range(number_of_posts):
        random_house = get_random_house(filename)
        while random_house in used_houses:
            random_house = get_random_house(filename)
        used_houses.append(random_house)
        texts_for_posts.append(g4f_question_for_housing(random_house))

        if generate_images:
            name_for_save_picture = f"{directory_for_images}{time.time()}"
            generateImage(name=name_for_save_picture, prompt=f"generate image of house with following information about this house: {' '.join(f'{key}: {random_house[i]},' for i, key in enumerate(['price', 'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 'furnishingstatus']))[:-1]}", dir=directory_for_images)
            urls.append("sadly, sdxl cannot provide url for image")
            path_for_imgs.append(f"{directory_for_images}/{name_for_save_picture}.jpeg")
    if generate_images:
        combined_list = list(zip(texts_for_posts, path_for_imgs, urls))
        answer = [list(triplet) for triplet in combined_list]
        return answer, used_houses
    else:
        return texts_for_posts, used_houses


def generate_posts(number_of_posts, generate_images=False, directory_for_images='imgs'):
    texts_for_posts, path_for_imgs, used_houses, urls = [], [], [], []
    if not os.path.exists(directory_for_images):
        os.makedirs(directory_for_images)
    for i in range(number_of_posts):
        random_house = get_random_house(filename)
        while random_house in used_houses:
            random_house = get_random_house(filename)
        used_houses.append(random_house)
        texts_for_posts.append(question_for_housing(random_house))
#  prompt for dalle for creating image 
        if generate_images:
            name_for_save_picture = f"{directory_for_images}{time.time()}"
            url = saveImg1024(name=name_for_save_picture, prompt=f"generate of house with following information about this house: {' '.join(f'{key}: {random_house[i]},' for i, key in enumerate(['price', 'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 'furnishingstatus']))[:-1]}", directory=directory_for_images)
            urls.append(url)
        
            path_for_imgs.append(f"{directory_for_images}/{name_for_save_picture}.jpeg")
    if generate_images:
        combined_list = list(zip(texts_for_posts, path_for_imgs, urls))
        answer = [list(triplet) for triplet in combined_list]
        return answer, used_houses
    else:
        return texts_for_posts, used_houses


# array, used_houses = generate_posts(2, True, 'imgs')
# array = [['Sure! Here\'s a captivating Instagram post for your real estate content:\n\n"🏡 Dream Home Alert! 🌟 This stunning 2-story house is a hidden gem in the heart of the city! With a spacious area of 4400 sqft, it offers 3 cozy bedrooms and a luxurious bathroom. The main road accessibility ensures convenience and easy commuting. Imagine the possibilities with this unfurnished canvas, where you can bring your own personal touch and style. Although parking is limited, the charm of this house makes up for it! 💫 Don\'t miss out on this incredible opportunity to make this house your dream home! 💖 #RealEstateGems #DreamHome #CityLiving"\n\nRemember, as GPT-3.5, I can provide creative and attractive text based on the given information. Let me know if there\'s anything else I can assist you with!', 'imgs/imgs1702149103.661759.jpeg'], ["🏠🔑 Your Dream Home Is Here! 🌟 Check Out This Stunning Property!\n\n💰 Price: $4,550,000\n📏 Area: 2,550 sqft\n🛏️ Bedrooms: 3\n🛁 Bathrooms: 1\n🏢 Stories: 2\n\nWelcome to this enchanting home that will truly capt ivate your heart! ✨ With its spacious layout and modern design, it offers the perfect blend of comfort and style.\n\n🛣️ Located on a main road, accessibility is at your doors tep. No need to worry about long commutes or inconvenient travel!\n\n🌞 Step inside and immerse yourself in the warm ambiance, as natural light beautifully enhances every corner of this house. \n\n✨ The elegant furnishing adds a touch of luxury, creating a cozy and inviting atmosphere that you'll love coming home to.\n\n🚗 In terms of parking, you have ample options, ensuring convenience for you and your guests.\n\n🏡 Yes! There's a basement, providing extra storage space and even more potential to personalize this home according to your desires.\n\n💦 While there's no hot water heating system, this home is still an absolute gem. 🌟\n\n❄️ Although there's no central air conditioning, you can eaasily install a cooling system based on your preferences.\n\n🚶\u200d♀️ Set in a preferred area, you'll find local amenities, schools, and parks just a stone's throw away.\n\n 🏠🌳 Don't miss out on this incredible opportunity to create lifelong memories in your dream home. Reach out to us today and let's make it yours!\n\n📲 Contact us: [Insert contact details] \n🌐 Website: [Insert website]\n\n#DreamHome #RealEstateOpportunity #StylishLiving", 'imgs/imgs1702149125.1050735.jpeg']]

# print(used_houses)
# file_path = "EXAMPLE.txt"
def write_posts_to_file(file_path, array, used_houses):
    with open(file_path, 'w', encoding='utf-8') as file:
        k = 0
        for i in array:
            price, area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus = used_houses[k]
            file.write(f"POST NUMBER {k+1}\n\n")
            file.write(f"price={price}\n")
            file.write(f"area={area}\n")
            file.write(f"bedrooms={bedrooms}\n")
            file.write(f"bathrooms={bathrooms}\n")
            file.write(f"stories={stories}\n")
            file.write(f"mainroad={mainroad}\n")
            file.write(f"guestroom={guestroom}\n")
            file.write(f"basement={basement}\n")
            file.write(f"hotwaterheating={hotwaterheating}\n")
            file.write(f"airconditioning={airconditioning}\n")
            file.write(f"parking={parking}\n")
            file.write(f"prefarea={prefarea}\n")
            file.write(f"furnishingstatus={furnishingstatus}\n")
            file.write("Text for this post:\n")
            file.write(i[0])
            file.write("\n")
            file.write("image's path for this post:")
            file.write(i[1])
            file.write("\n")
            file.write("image's url for this post:")
            file.write(i[2])
            file.write("\n")
            file.write("\n")
            file.write("\n")
            file.write("\n")

            k += 1


array, used_houses = generate_posts(1, True, 'imgs_for_test')
# write_posts_to_file("free_EXAMPLE.TXT", array=array, used_houses=used_houses)



# If you want to try g4f:
# array, used_houses = generate_posts_with_g4f(1, True, 'free_imgs_for_test')


print(array, used_houses)