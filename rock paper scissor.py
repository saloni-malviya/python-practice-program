#rock paper scissor
print("rock=1")
print("paper=2")
print("scissor=3")

player1=int(input("select what the player1 plays"))
player2=int(input("select what the player2 plays"))
if(player1==1 and player2==2):
   print("player2 is winner")
elif(player1==2 and player2==1):
   print("player1 is winner")
elif(player1==3 and player2==2 or player1==1 and player2==3):
   print("player1 is winner")
elif(player1==2 and player2==3 or player1==3 and player2==1):
   print("player2 is winner")
else:
   print("Game Draw")
