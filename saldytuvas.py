product_list = []
recipe_list = []

def add_product():
    product_name = input("Įveskite produkto pavadinimą: ")
    product_mass = float(input("Įveskite produkto masę gramais: "))
    product_list.append((product_name, product_mass))
    print(f"{product_name} ({product_mass}g) pridėtas į produktų sąrašą.\n")

def remove_product():
    product_name = input("Įveskite produkto pavadinimą, kurį norite pašalinti: ")
    for product in product_list:
        if product[0] == product_name:
            product_list.remove(product)
            print(f"{product_name} pašalintas iš produktų sąrašo.\n")
            return
    print(f"{product_name} nerastas produktų sąraše.\n")

def display_products():
    if not product_list:
        print("Produktų sąrašas tuščias.\n")
    else:
        print("Produktų sąrašas:")
        for product in product_list:
            print(f"{product[0]} ({product[1]}g)")
        print()

def total_product_mass():
    total_mass = sum([product[1] for product in product_list])
    print(f"Iš viso produktų masė šaldytuve yra {total_mass}g.\n")

def add_recipe():
    recipe_name = input("Įveskite recepto pavadinimą: ")
    recipe_ingredients = []
    while True:
        ingredient_name = input("Įveskite ingrediento pavadinimą (arba 'baigta', jei baigėte pridėti ingredientus): ")
        if ingredient_name == "baigta":
            break
        for product in product_list:
            if product[0] == ingredient_name:
                ingredient_mass = float(input(f"Įveskite {ingredient_name} masę gramais: "))
                recipe_ingredients.append((ingredient_name, ingredient_mass))
                break
        else:
            print(f"{ingredient_name} nerastas produktų sąraše. Prašome jį pridėti.")
    recipe_list.append((recipe_name, recipe_ingredients))
    print(f"{recipe_name} pridėtas į receptų sąrašą.\n")

def remove_recipe():
    recipe_name = input("Įveskite recepto pavadinimą, kurį norite pašalinti: ")
    for recipe in recipe_list:
        if recipe[0] == recipe_name:
            recipe_list.remove(recipe)
            print(f"{recipe_name} pašalintas iš receptų sąrašo.\n")
            return
    print(f"{recipe_name} nerastas receptų sąraše.\n")

def display_recipes():
    if not recipe_list:
        print("Receptų sąrašas tuščias.\n")
    else:
        print("Receptų sąrašas:")
        for recipe in recipe_list:
            print(recipe[0] + ":")
            for ingredient in recipe[1]:
                print(f"{ingredient[0]} ({ingredient[1]}g)")
            print()
        print()

while True:
    print("Virtuvės valdymas\n")
    print("1. Pridėti produktą")
    print("2. Pašalinti produktą")
    print("3. Rodyti produktus")
    print("4. Viso produkto masė")
    print("5. Pridėti receptą")
    print("6. Pašalinti receptą")
    print("7. Rodyti receptus")
    print("8. Išeiti")

    choice = input("Įveskite pasirinkimą (1-8): ")
    print()

    if choice == "1":
        add_product()
    elif choice == "2":
        remove_product()
    elif choice == "3":
        display_products()
    elif choice == "4":
        total_product_mass()
    elif choice == "5":
        add_recipe()
    elif choice == "6":
        remove_recipe()
    elif choice == "7":
        display_recipes()
    elif choice == "8":
        print("Viso gero!")
        break
    else:
        print("Neteisingas pasirinkimas. Bandykite dar kartą.\n")
#main