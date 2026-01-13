import data_fetcher


HTML_TEMPLATE = "animals_template.html"


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
    animals_data = data_fetcher.fetch_data(animal_name)
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
