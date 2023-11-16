spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    the_names = []
    for dictionary in spicy_foods:
        the_names.append(dictionary["name"])
    return the_names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [item for item in spicy_foods if item["heat_level"] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        print( f"{item['name']} ({item['cuisine']}) | Heat Level: {item['heat_level'] * '🌶'}" )

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    list = [item for item in spicy_foods if item['cuisine'] == cuisine]
    return list[0]

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    list = []
    for dictionary in spicy_foods:
        list.append(dictionary["heat_level"])
    average = sum(list)/len(list)
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
