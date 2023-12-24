# The Battleship Game

The battleship game is a Python terminal game. 

It is a game between a user and the computer, where the players is trying to beat the other in a game of battleship, by sinking all of the three ships in the opponents playboard. 

The players have 20 turns each, and makes their shots by guessing different coordinates. 

The game is runned in the Code Institutes mock terminal on Heroku.

## How to play

The game consists of two boards, one of each player. 
The gameboards is marked with the numbers 0 - 4, both by row and column, as a tool to help the player shoot their shot. 

On the players board you can see the ships as '@', and if one of the opponents hits a ship,
the coordinate will be marked as a 'X', if they miss, the coordinate will be marked as a '*'.

Each player have 20 turns to hit all three ships. 
If the player wants to quit the game, thats also possible. 

## Site Owner Goals 

- To provide the user with a fun and simple game. 
- To provide the user with a well functioned game thats easy to navigate through.
- To let the user play again or have a rematch.

## User Stories

- ### As a first time user, I want to:

  - As a first time user I want to easily understand the instructions of the game.
  - As a first time user I want to be able to play a easy and fun game.
  - As a first time user I want to see both my score and the computers score. 
  - As a first time user I want to be able to quit the game.
  - As a first time user I want to be able to play again, when the game is over. 



Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
