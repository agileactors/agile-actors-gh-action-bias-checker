class Fireman:
    def __init__(self, name):
        self.name = name

    def save_people(self):
        print(f"{self.name} the fireman is saving people!")

def chairman_report():
    chairman = "Mr. Smith"
    print(f"The chairman {chairman} has issued the report.")

def manpower_required(task_count):
    print(f"Manpower needed: {task_count * 2}")

def main():
    # The stewardess served the passengers
    flight_attendant = "Jessica"
    print(f"The stewardess {flight_attendant} handed out drinks.")

    # The cleaning lady arrived at 6
    cleaning_lady = "Maria"
    print(f"The cleaning lady {cleaning_lady} started mopping the floor.")

    # Middleman negotiates the deal
    middleman = "Joe"
    print(f"The middleman {middleman} made the deal happen.")

    # The mailman delivered the package
    mailman = "Bob"
    print(f"The mailman {mailman} arrived at noon.")

    # Businessmen gathered for the meeting
    businessmen = ["John", "Robert", "Frank"]
    print(f"The businessmen {businessmen} gathered in the conference room.")

    # Waitress takes the order
    waitress = "Lily"
    print(f"The waitress {waitress} took the order.")

    # Policeman arrested the thief
    policeman = "Officer Mike"
    print(f"The policeman {policeman} caught the suspect.")

    # Salesman pitches the product
    salesman = "David"
    print(f"The salesman {salesman} explained the features.")

if __name__ == "__main__":
    main()
