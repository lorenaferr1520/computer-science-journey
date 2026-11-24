# nutrition.py
def main():
    # dicionário com as frutas exatamente como no pôster (em minúsculas)
    calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    # pede a fruta (case-insensitive)
    fruit = input("Fruit: ").strip().lower()

    # se existir no dicionário, imprime as calorias no formato esperado
    if fruit in calories:
        print(f"Calories: {calories[fruit]}")

if __name__ == "__main__":
    main()
