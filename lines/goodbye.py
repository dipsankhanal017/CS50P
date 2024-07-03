def main():
    print(sayGoodbye(input("Name: ")))

#this is a lamda function

sayGoodbye = lambda name : f"Goodbye, {name}"


#calling main here
if __name__ == "__main__":
    main()
