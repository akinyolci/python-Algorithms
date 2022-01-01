n_groups = int(input("number of groups:"))
n_players = int(input("number of players in each group:"))


def square(r):
    total = r * r
    for i in range(r):
        print("*" * r)
    return total


def triangle(r):
    total = 0
    a = r - 1
    for i in range(1, r + 1):
        total += i
        print(" " * a + "*" * i)
        a -= 1
    return total


def equilateral_triangle(r):
    total = 0
    a = 0
    while r > 0:
        total += r
        print(" " * a + (" " + "*") * r + " " * a)
        r -= 1
        a += 1
    return total


def sandglass(r):
    total = 1
    b = r
    c = r
    for i in range(1, r + 1):
        a = 1
        while r > 1:
            total += r
            print(" " * a + "* " * r + " " * a)
            a += 1
            r -= 1
    print(" " * (b) + "*")
    a = c - 1
    for i in range(2, c + 1):
        total += i
        print(" " * a + "* " * i)
        a -= 1
    return total


for group in range(1, n_groups + 1):
    for player in (1, n_players):
        print("Group {} - Player {}".format(group, player))
        a = input("Select a shape (1= Square, 2= Triangle, 3= Equilateral triangle, 4= Sandglass):")
        if a == "1":
            print("Shape is Square!")
            size = [2, 3, 4, 5, 6]
            r = int(input("Select the size of the shape (2/3/4/5/6):"))
            if r not in size:
                print("Oops, Player {} is eliminated!".format(player))
                n_players -= 1
            else:
                sonuc = int(input("How many stars exist in this square?"))
                total = square(r)
                if sonuc == total:
                    print(f"Total number of stars: {total}. Player {player} wins the game!")
                else:
                    print(f"Total number of stars: {total}. Oops, Player {player} is eliminated!")
                    n_players -= 1

        elif a == "2":
            print("Shape is Triangle!")
            size = [2, 3, 4, 5, 6]
            r = int(input("Select the size of the shape (2/3/4/5/6):"))
            if r not in size:
                print("Oops, Player {} is eliminated!".format(player))
                n_players -= 1
            else:
                sonuc = int(input("How many stars exist in this triangle?"))
                total = triangle(r)
                if sonuc == total:
                    print(f"Total number of stars: {total}. Player {player} wins the game!")
                else:
                    print(f"Total number of stars: {total}. Oops, Player {player} is eliminated!")
                    n_players -= 1

        elif a == "3":
            print("Shape is  equilateral triangle!")
            size = [2, 3, 4, 5, 6]
            r = int(input("Select the size of the shape (2/3/4/5/6):"))
            if r not in size:
                print("Oops, Player {} is eliminated!".format(player))
                n_players -= 1
            else:
                sonuc = int(input("How many stars exist in this equilateral triangle?"))
                total = equilateral_triangle(r)
                if sonuc == total:
                    print(f"Total number of stars: {total}. Player {player} wins the game!")
                else:
                    print(f"Total number of stars: {total}. Oops, Player {player} is eliminated!")
                    n_players -= 1

        elif a == "4":
            print("Shape is  sandglass!")
            size = [2, 3, 4, 5, 6]
            r = int(input("Select the size of the shape (2/3/4/5/6):"))
            if r not in size:
                print("Oops, Player {} is eliminated!".format(player))
                n_players -= 1
            else:
                sonuc = int(input("How many stars exist in this sandglass?"))
                total = sandglass(r)
                if sonuc == total:
                    print(f"Total number of stars: {total}. Player {player} wins the game!")
                else:
                    print(f"Total number of stars: {total}. Oops, Player {player} is eliminated!")
                    n_players -= 1
        else:
            print(f"Oops invalid choice! Player {player} is eliminated!")
            n_players -= 1

    if n_players > 0:
        print("{} player(s) stayed alive in Group {} !".format(n_players, group))
