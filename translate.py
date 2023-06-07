def translate(phrase):
    translation = ""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letter in phrase:
        if letter in vowels:
            translation = translation + "g"
        else:
            translation = translation + letter
    
    return translation

print(translate(input("Enter a phrase: ")))