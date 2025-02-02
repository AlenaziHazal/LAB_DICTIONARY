weather = {
    "Riyadh":{
        "date":"2023/12/1",
        "temperature":"45",
        "humidity":"yes",
        "weather condition":"sunny"
        },
    "Arar":{
        "date":"2023/12/1",
        "temperature":"23",
        "humidity":"no",
        "weather condition":"sunny"
        },
    "Rafha":{
        "date":"2023/12/1",
        "temperature":"22",
        "humidity":"yes",
        "weather condition":"rainy"
        },
    "Haiel":{
        "date":"2023/12/1",
        "temperature":"15",
        "humidity":"yes",
        "weather condition":"rainy"
        },
    "Damam":{
        "date":"2023/12/1",
        "temperature":"55",
        "humidity":"no",
        "weather condition":"sunny"
        },
    "Abha":{
        "date":"2023/12/1",
        "temperature":"5",
        "humidity":"yes",
        "weather condition":"rainy"
        }
}
user_input = input("Enter city name to see the weather: ")

def fetch_data(city,date,temperature,humidity,weather_condition):
    weather.update({city:{"data":date,"temperature":temperature,"humidity":humidity,"weather_condition":weather_condition}})
    print("Add city successfully")
    print(f"{user_input}:{weather[user_input]}")
    return weather


if not user_input in weather:
    print(f"Sorry we don't have the info for {user_input}")
    choisen = int(input("If you want to insert city enter 1, If you don't enter 2: "))
    if choisen == 1:
        city_name = input("If you want to add a new city enter the name: ")
        date = input("If you want to add date to a new city enter the date: ")
        temperature = input("If you want to add temperature to a new city enter the temp: ")
        humidity = input("If you want to add humidity a new city enter the humidity: ")
        weather_condition = input("If you want to add weather condition to a new city enter the condition. Hint: sunny,rainy: ")
        fetch_data(city_name,date,temperature,humidity,weather_condition)
    else:
        print("Thank for your time")
else:
    data = weather[user_input]
    print(f"The weather in {user_input} on {data['date']} is {data['temperature']} and the weather condition is {data['weather condition']}")