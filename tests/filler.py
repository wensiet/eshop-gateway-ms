import datetime
import json
import random
import requests


def get_random_text_from_github(url):
    response = requests.get(url)
    if response.status_code == 200:
        text = response.text
        data = json.loads(text)
        return random.choice(data['fruits'])
    else:
        return "Default Text"


def get_random_description(url):
    response = requests.get(url)
    if response.status_code == 200:
        text = response.text
        text = text.split("\n")
        word = None
        while word is None or len(word) <= 3:
            word = random.choice(text)
        return word
    else:
        return "Default Title"


def generate_product_info():
    titles_url = ("https://raw.githubusercontent.com/first20hours/"
                  "google-10000-english/master/google-10000-english-usa-no-swears-medium.txt")
    descriptions_url = "https://raw.githubusercontent.com/dariusk/corpora/master/data/foods/fruits.json"

    title = get_random_text_from_github(descriptions_url)
    description = get_random_description(titles_url)
    price = round(random.uniform(1.0, 50.0), 2)
    quantity = random.randint(1, 100)

    product_info = {
        "title": title.strip(),
        "description": description.strip(),
        "price": price,
        "quantity": quantity
    }

    return product_info


def save_to_json(product_info, filename):
    with open(filename, 'w') as json_file:
        json.dump(product_info, json_file, indent=2)


if __name__ == "__main__":
    total = []
    while True:
        start = datetime.datetime.now()
        product_info = generate_product_info()
        end = datetime.datetime.now()
        print(f"Generated product info in {end - start}")
        start = datetime.datetime.now()
        request = requests.post("http://localhost/api/v1/product", json=product_info)
        end = datetime.datetime.now()
        print(f"Sent request to my API in {end - start}")
        total.append(end - start)
        print(f"Average my API response time: {sum(total, datetime.timedelta()) / len(total)}")
        if request.status_code != 200:
            print(request)
