highest_Temperature = [0] * 31
print(highest_Temperature)

def update_temperature(day, temperature):
    highest_Temperature[day-1] = temperature
    print("Temperature updated to :{temp}".format(temp = highest_Temperature[day-1]))

def get_temperature(day):
    temperature = highest_Temperature[day-1]
    print("Temperature is {temp}".format(temp = temperature))

update_temperature(3, 30)
get_temperature(3)