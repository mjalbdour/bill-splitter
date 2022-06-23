import random

MSG_NUMBER_OF_PEOPLE = "Enter the number of friends joining (including you):"
MSG_ZERO_JOINING = "No one is joining for the party"
MSG_NAMES = "Enter the name of every friend (including you), each on a new line:"
MSG_TOTAL_BILL = "Enter the total bill value:"
MSG_LUCKY = 'Do you want to use the "Who is lucky?" feature? Write Yes/No:'
MSG_NO_LUCKY = "No one is going to be lucky"

print(MSG_NUMBER_OF_PEOPLE)
num_of_people = input()
print()

if not num_of_people.isnumeric() or int(num_of_people) <= 0:
    print(MSG_ZERO_JOINING)
else:
    num_of_people = int(num_of_people)
    print(MSG_NAMES)
    people = [input() for _ in range(num_of_people)]
    people_bills = dict.fromkeys(people, 0.00)

    print(MSG_TOTAL_BILL)
    total_bill = float(input())
    print(MSG_LUCKY)
    lucky = input()
    lucky_one = None
    if lucky.strip().title() in "Yes":
        lucky_one = random.choice([p for p in people_bills])
        print(f'{lucky_one} is the lucky one!')
        num_of_people -= 1
    else:
        print(MSG_NO_LUCKY)

    person_bill = round(total_bill / num_of_people, 2)
    for k in people_bills:
        if k == lucky_one:
            people_bills[k] = 0
        else:
            people_bills[k] = person_bill
    print(people_bills)
