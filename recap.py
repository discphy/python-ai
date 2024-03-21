my_name = "discphy"
my_age = 28

print(f"Hello I'm {my_name}, I have {my_age}, years in the earth")


def make_juice(fruit):
    return f"{fruit}+🥤"


def add_ice(juice):
    return f"{juice}+🧊"


def add_suger(iced_juice):
    return f"{iced_juice}+🍬"


juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_suger(cold_juice)

print(perfect_juice)
