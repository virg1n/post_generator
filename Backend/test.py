
house = ['3395000', '3450', '3', '1', '1', 'yes', 'no', 'yes', 'no', 'no', '2', 'no', 'unfurnished']

print(f"I want to create an Instagram post about engaging real estate content. Can you write text for this post? make it the most attractive, skip the information that may seem unattractive or that is not given to you. There is information about this house: {' '.join(f'{key}: {house[i]},' for i, key in enumerate(['price', 'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 'furnishingstatus']))[:-1]}")