if __name__ == "__main__":
    a = 0
    tries = 0
    numbers = []
    while a != 5:
        a = int(input("Write 5!"))
        tries = tries + 1
        numbers.append(a)
        if a == 5:
            print("Thank you!")
        else:
            msg = "I said 5"
            for i in range(tries):
                msg = msg + "!"
            print(msg)
            n_msg = "You wrote"
            for i in range(len(numbers)):
                n_msg = n_msg + str(numbers[i]) + ", "
            print(n_msg)
