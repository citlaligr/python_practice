def game_over():
    print("💀 Game over")


def win():
    print("🏆 You Win!")


def play_game():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.\n")

    way = input("Choose left or right: ").strip().lower()

    if way == "left":
        action = input("swim or wait: ").strip().lower()

        if action == "wait":
            door = input("Red, Blue or Yellow: ").strip().lower()

            if door == "yellow":
                win()
            elif door in ["red", "blue"]:
                game_over()
            else:
                print("Invalid option")

        elif action == "swim":
            game_over()
        else:
            print("Invalid option")

    elif way == "right":
        game_over()
    else:
        print("Invalid option")


if __name__ == "__main__":
    play_game()
