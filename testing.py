# days above average temperature

# number_of_days = int(input("How many days?: "))
# temperatures = []
# for i in range(1, number_of_days + 1):
#     temperatures.append(int(input(f"Highest temperature on day {i}: ")))
# average_temperature = round(sum(temperatures) / len(temperatures), 1)
# number_of_above_average_days = len([i for i in temperatures if i > average_temperature])
# print(f"Average temperature: {average_temperature}")
# print(f"{number_of_above_average_days} day(s) above average")


number_of_days = None
while type(number_of_days) != int:
    try:
        number_of_days = int(input("How many days?: "))
    except:
        print("Invalid input")
temperatures = []
for i in range(1, number_of_days + 1):
    temperature = None
    while type(temperature) != int:
        try:
             temperature = int(input(f"Highest temperature on day {i}: "))
        except:
            print("Invalid input")
    temperatures.append(temperature)
average_temperature = round(sum(temperatures) / len(temperatures), 1)
number_of_above_average_days = len([i for i in temperatures if i > average_temperature])
print(f"Average temperature: {average_temperature}")
print(f"{number_of_above_average_days} day(s) above average")