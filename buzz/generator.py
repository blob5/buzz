from __future__ import print_function
import random

fish = ("cod", "salmon", "tilapia", "pollock", "catfish")
styles = ("crispy", "grilled", "blackened", "buttered", "beer-battered")
toppings = ("tartar sauce", "lemon aioli", "pickled onions", "slaw", "melted cheddar")
buns = ("brioche bun", "sesame bun", "potato bun", "pretzel bun", "toasted roll")
finishes = ("with a squeeze of lemon", "with a dash of hot sauce", "with sea salt", "with fresh dill", "with cracked pepper")

def sample(l, n=1):
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result

def generate_buzz():
    phrase = " ".join([
        "A",
        sample(styles),
        sample(fish),
        "fishburger on a",
        sample(buns),
        "topped with",
        sample(toppings),
        sample(finishes),
    ])
    return phrase

if __name__ == "__main__":
    print(generate_buzz())
