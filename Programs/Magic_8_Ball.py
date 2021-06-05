sentences = [
    "Find Your Peace And Live In It",
    "We Shine Bright So That Others May Shine Brighter",
    "The Simplest Answer Is Usually The Correct One",
    "In This Life You Do Get Second Chances",
    "Find Your Natural Rhythm And Harmonize With It",
    "Glide Joyfully Toward Your Next Challenge In Life",
    "Reading Is Fun-To-Mental",
    "Leadership Needs Compassion To Thrive",
    "Focus On The Team… That’s Leadership",
    "Everyone Plants Seeds… Leaders Make Them Grow",
    "The first step towards failure is trying",
    "The best things in life are actually really expensive",
    "If at first you don’t succeed. Give up and try something else",
    "You can be replaced",
    "It probably will get worse",
    "You’re born, you work, you die",
    "I can but I won’t",
    "Will it be easy? Nope. Worth it? Absolutely not!",
    "Just imagine how terrible it might have been if we’d been at all competent",
    "Accept that you're just a product, not a gift"
]

import random

while True:
    
    userInp = int(input("Start or Stop ( 1 or 0): "))

    if userInp == 1:
        random_sentence = random.randint(1, len(sentences))
        print(f"\n{sentences[random_sentence]}\n")
        continue

    elif userInp == 0:
        break

    else:
        print("\nEnter Correct Value!\n")