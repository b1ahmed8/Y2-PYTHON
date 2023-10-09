teams = ["Ferrari","Williams","Haas","Racing Point"]

print("Current bonus payment: ", teams[0])

print("Rival team: ", teams[1])

teams[3] = "Aston Martin"

teams.append("Buggati")
teams.append("Lamborghini")

print(teams)

numberInput = int(input("Enter number to replace: "))
nameInput = input("Enter name: ")

teams[numberInput-1] = nameInput
print(teams)