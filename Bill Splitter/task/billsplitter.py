
MSG_NUMBER_OF_PEOPLE = "Enter the number of friends joining (including you):"
MSG_ZERO_JOINING = "No one is joining for the party"
MSG_NAMES = "Enter the name of every friend (including you), each on a new line:"

print(MSG_NUMBER_OF_PEOPLE)
num_of_people = input()
print()

if not num_of_people.isnumeric() or int(num_of_people) <= 0:
    print(MSG_ZERO_JOINING)
else:
    print(MSG_NAMES)
    people = [input() for _ in range(int(num_of_people))]
    people_bills = dict.fromkeys(people, 0)
    print(people_bills)


