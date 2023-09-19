player_positions=input("What position are you located? ")

column=player_positions[0].upper()
number=int(player_positions[1])

if column in "ACEG" and number%2==1: print("black")
elif column in "BDFH" and number%2==0: print("black")
elif column in "ACEG" and number%2!=1: print("white")
elif column in "BDFH" and number%2!=0: print("white")
else:print("please enter a valid position")