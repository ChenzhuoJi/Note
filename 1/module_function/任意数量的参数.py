def ingredients_for_sandwich(*ingredients):
    print(f"\nThe ingrediens for sandwich:")
    for ingredient in ingredients:
        print(f"-{ingredient}")
        

ingredients_for_sandwich('sausage','bread slice','butter','lettuce')
