import random, string

amount = int(input('Amount of nitro codes to generate: '))
value = 1

while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    print ("[GENERATED] " + code)
    value += 1