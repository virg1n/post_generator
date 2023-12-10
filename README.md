# Post Creation Method with GPT & DALL·E3

## Overview

I've implemented a flexible post creation method that used gpt3.5-turbo model and dalle3.

### Implementation

I've written the necessary functions in `Backend/functions.py` to handle post creation using GPT and DALL·E3

### Usage

These function can be executed using the `main.py` script. 
However, you need to download all requirements by using command:
`cd .\Backend\`
`pip install -r requirements.txt`
after all, you can easily start `main.py` script

function `generate_posts()` is main function.
There are 3 args:
1. Number of posts
2. True if you want images and False if you dont
3. path for save images(skip is 2 was False)
### Output Files

In the **EXAMPLE.txt** you can see my examples of postsusing the GPT 3.5-turbo model with dalle3.
 
In this file:

- The first line represents the number of posts.
- Subsequently, you'll find information about a randomly chosen house.
- Then, text of the post
- The image's path and image's URL are also included.

Afterwards, new posts' data is presented.

## Important Warning

I also made an additional method for this assignment. Since I used to create projects using gpt without having tokens, I had to use gpt4free (the free model). This library parses sites such as Bing, YouGPT, GPT4Love, etc. I used Stable diffusion XL to create the images. 

In this assignment, I also implemented this method, you can see its results in `free_EXAMPLE.txt`.
However, in order to try these functions yourself, you need to download the g4f library:


cd Backend
git clone https://github.com/xtekky/gpt4free.git
cd gpt4free
pip install -r requirements.txt
cd ..
python main.py



Also, you need to put `SDXL_MODEL_ID` to .env file. (I wrote it in telegram)

Then, you need run this:
`pip install baseten`
`pip install urllib3==1.26.15 requests-toolbelt==0.10.1`

Change function in the 131 line:
generate_posts -> generate_posts_with_g4f
or just comment 131 line and uncomment 138 line 

# Questions
1. How to mimic the style of successful Instagram posts?
Answer: Using hashtags, emojis and as attractive as possible to tell as if the author of the post is a realtor who wants to sell a house. It is also important that the post does not contain information that is not in the dataset or that does not seem attractive


2. What prompt engineering techniques can improve quality?
Answer: First of all, you need to explain to the model what you want to do and how it can help. It is necessary to explain which data should be used and which should not be used. Next, you need to give all the data about the house that is available. It is also important to show an example that we want to get (in the message history)

3. How to ensure the model doesn't invent extra features?
Answer: show an example that we want to get (in the message history). test the model and write more precisely prompt if needed.
