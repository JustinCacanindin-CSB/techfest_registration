# Task 1 done


print("Welcome to SMIT TechFest!")
print("Organized by Justin_Cacanindin of APPDAET BTCS1\n")

participant_input = input("How many participants will register? ")


if participant_input.isdigit():
    participant_count = int(participant_input)
else:
    print("Invalid number of participants.")
    exit()


if participant_count <= 0:
    print("Invalid number of participants.")
    exit()


