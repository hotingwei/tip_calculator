print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill?\n"))
num_people = int(input("How many people to split the bill?\n"))

while True:
	percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))

	if percentage_tip == 10 or percentage_tip == 12 or percentage_tip == 15:
		break 
	else:
		print("The percentage tip can only accept 10, 12, or 15!")

amount = total_bill * (1 + (percentage_tip / 100)) / num_people
print("Each person should pay:", amount)

