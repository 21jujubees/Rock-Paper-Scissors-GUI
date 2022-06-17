import random
from tkinter import *
from tkinter.ttk import *
import pygame

class Player(): # This is the player class, we use this to track stats across multiple games.
  def __init__(self, name):
    self.__name = name # Player name
    # These 3 variables track the player's win-loss record
    self.__wins = 0
    self.__losses = 0
    self.__ties = 0
  
    # This function increments the win-loss counter appropriately
  def keepScore(self, result): # Result is passed into this function as an integer
    if result == 0:
      self.__losses += 1
      return self.__losses
    elif result == 1:
      self.__wins += 1
      return self.__wins
    elif result == 2:
      self.__ties += 1
      return self.__ties
    else:
      return

def gameLogic(userMove, player):
    
    compMove = random.choice(["Rock", "Paper", "Scissors"])
    
    winConditions = {
        "Rock": "Paper",
        "Paper": "Scissors",
        "Scissors": "Rock"
    }
    
    pics = {
        "Rock": rockPic,
        "Paper": paperPic,
        "Scissors": scissorsPic,
    }
    
    
    userMoveLabel.config(image = pics[userMove])
    compMoveLabel.config(image = pics[compMove])
    
    if userMove == compMove:
        resultLabel.config(text = "There is a draw!")
        
    elif userMove in winConditions[compMove]:
        resultLabel.config(text = "Player wins!")
        playerScoreLabel.config(text = "Player: " + str(player.keepScore(1)))
        
    else:
        resultLabel.config(text = "CPU wins!")
        compScoreLabel.config(text = "CPU: " + str(player.keepScore(0)))

window =  Tk()
window.title("Rock Paper Scissors Game")

Label(window, text = "Rock, Paper, Scissors").grid(row = 0, sticky = N, pady = 10, padx = 200)
Label(window, text = "Please select an option").grid(row = 1, sticky = N)

playerScoreLabel = Label(window, text = "Player: ")
playerScoreLabel.grid(row = 2, sticky = W)

compScoreLabel = Label(window, text = "CPU: ")
compScoreLabel.grid(row = 2, sticky = E)

userMoveLabel = Label(window)
userMoveLabel.grid(row = 3, sticky = W)

compMoveLabel = Label(window)
compMoveLabel.grid(row = 3, sticky = E)

resultLabel = Label(window)
resultLabel.grid(row = 4, sticky = N)


player = Player("YOU")

rockPic = PhotoImage(file = "images/rock.png")
rockPic = rockPic.subsample(2,2)
rockButton = Button(window,text="Rock",width = 15, image = rockPic, command = lambda:gameLogic("Rock", player))
rockButton.grid(row = 5, sticky = W, padx = 50, pady = 20)

paperPic = PhotoImage(file = "images/paper.png")
paperPic = paperPic.subsample(2,2)
paperButton = Button(window,text="Paper",width = 15, image = paperPic, command = lambda:gameLogic("Paper", player))
paperButton.grid(row = 5, sticky = N, pady = 20)

scissorsPic = PhotoImage(file = "images/scissors.png")
scissorsPic = scissorsPic.subsample(2,2)
scissorsButton = Button(window,text="Scissors",width = 15, image = scissorsPic, command = lambda:gameLogic("Scissors", player))
scissorsButton.grid(row = 5, sticky = E, padx = 50, pady = 20)

pygame.mixer.init()
pygame.mixer.music.load("music/song.mp3")
pygame.mixer.music.play(loops=-1)

window.mainloop()
