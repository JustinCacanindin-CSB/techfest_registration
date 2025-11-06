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


# Task 2: 

participants = []  

for i in range(participant_count):
    name = input("Enter participant name: ")
    track = input("Enter chosen track: ")
    participants.append({"name": name, "track": track})

print("\nRegistered Participants:")
for index, p in enumerate(participants, start=1):
    print(f"{index}. {p['name']} - {p['track']}")

# Task 3: 

track_set = {p["track"] for p in participants}

if len(track_set) < 2:
    print("\nNot enough variety in tracks.")
else:
    print("\nTracks offered in this event:")
    print(", ".join(track_set))
