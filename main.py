
from ascii_imgs.ascii import logo

data_dict = {}
winner_name = 0
max_value = 0
print(logo)
print("Welcome to the secret auction programm")


def start_funct():
    global data_dict, max_value, winner_name
    user_name = input("Whats your name? ")
    user_bid = int(input("Whats your bid? $"))
    any_people_answer = input("Are there any other bidders? Y/N ")
    data_dict.update({user_name: user_bid})
    print(data_dict)
    if any_people_answer == "Y":
        start_funct()
    else:
        for keys in data_dict:
            if data_dict[keys] > max_value:
                max_value = data_dict[keys]
                winner_name = keys
        print(f"The winner is {winner_name} with a bid of ${max_value}")


def main():
    start_funct()


if __name__ == "__main__":
    main()
