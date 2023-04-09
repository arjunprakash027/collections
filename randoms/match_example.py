def find_day(day):
    day = day.lower()
    match day:
        case "mon" | "tue" |"wed" | "thu" | "fri" :
            print("weekday")
        case "sat" | "sun":
            print("weekend")
        case _:
            print("its not a valid day")

day = input("enter the day: ")
find_day(day)
        