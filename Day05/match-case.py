status = input("Enter the status(200, 404,500 or 501: ")

match status:
    case 200:
        print("Success!")
    case 404:
        print("Not Found")
    case 500 | 501:  # You can use | for "OR"
        print("Server Error")
    case _:          # The underscore is the "default" case
        print("Unknown Status")
