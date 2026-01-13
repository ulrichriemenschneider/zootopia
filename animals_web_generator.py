import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
HTML_TEMPLATE = "animals_template.html"
REQUEST_URL = "https://api.api-ninjas.com/v1/animals?name="

def api_request(animal_name):
    """ API-Request for a given animal, returns a json-object """
    url = f"{REQUEST_URL}{animal_name}"
    res = requests.get(url, headers={"X-Api-Key": API_KEY})
    if res.status_code == requests.codes.ok:
        print("Success:", res.status_code)
        return res.json()
    else:
        print("Error:", res.status_code, res.text)
        return None


def get_html():
    """ Loads the html-template and returns it as a string """
    with open(HTML_TEMPLATE, "r") as fileobj:
        return fileobj.read()
    

def save_html(html_string, file_name):
    """ Saves the generated HTML-file """
    with open(file_name, "w") as fileobj:
        fileobj.write(html_string)


def serialize_animal(animal):
    """ Serialize the animal-data and returns a string """
    output = ""
    output += '<ul class="cards">'
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal["name"]}</div>\n'
    output += '<p class="card__text">\n'
    try:
        output += f"<strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n"
    except KeyError:
        pass
    try:
        output += f"<strong>Location:</strong> {animal["locations"][0]}<br/>\n"
    except KeyError:
        pass
    try:
        output += f"<strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n"
    except KeyError:
        pass
    output += '</p>\n'
    output += '</li>\n'
    output += '</ul>\n'
    return output


def get_string(animal_name):
    """ Returns the animal-data as a string """
    animals_data = api_request(animal_name)
    print(f"Number of animals: {len(animals_data)}")
    if animals_data == None:
        return None
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def main():
    animal_name = input("Enter a name of an animal: ")
    animals = get_string(animal_name)
    if animals == None:
        animals = '<h2>Error during API query.</h2>'
    elif len(animals) == 0:
        print("No animals found")
        animals = f'<h2>The animal {animal_name} doesn\'t exist.</h2>'
    html_template = get_html()
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals)
    save_html(html_output, "animals.html")


if __name__ == "__main__":
    main()
