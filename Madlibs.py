# This is a simple Madlibs game in Python
name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
number = input("Enter a number: ")

madlib = (
    f"\nOne {adjective} morning, {name} went to {place} with a {noun}.\n"
    f"There, {name} met {number} {animal}s who wanted to {verb}.\n"
    f"So everyone {verb}ed {adverb} until the sun went down.\n"
    f"Computer Programming is {adjective}!"
)
print(madlib)
