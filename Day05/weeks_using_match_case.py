def dayOfWeek(x):
    x = x.upper()
    match x:
        case 'M':
            return "MONDAY"
        case "T":
            return "TUESDAY"
        case "W":
            return "WEDNESDAY"
        case "R":
            return "THURSDAY"
        case "F":
            return "FRIDAY"
        case "S":
            return "SATURDAY"
        case "U":
            return "SUNDAY"
        case _:
            return "Invalid input"

print(dayOfWeek(input("Enter a day of the week (M, T, W, R, F, S, U): ")))