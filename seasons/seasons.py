from datetime import date
import sys
import inflect
p = inflect.engine()


class Age:
    def calculate(dateOfBirth):
        try:
            year, month, day = dateOfBirth.split("-")
            dob = date(int(year), int(month), int(day))
            value = date.today() -  dob
            min = value.days * 24 * 60
            return p.number_to_words(min).capitalize().replace(" and", "") + " minutes"
        except ValueError:
            print("Invalid date")
            sys.exit(1)


def main():
    dateOfBirth = input("Date of Birth: ")
    print(Age.calculate(dateOfBirth))





if __name__ == "__main__":
    main()
