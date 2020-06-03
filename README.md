# Monty Hall Game

The Monty Hall problem was based on the popular American game show Let's Make a Deal. On this show, the contestant are asked to select one door from an option of three. Behind the three doors, only one contains a prize. After the contestant selects a door, the game show host would then proceed to reveal one of the doors not chosen by the constestant and without a prize, and ask if the contestant would like to switch his choice to the other remaining door. Probablistically speaking, if the contestant switches his/her choice everytime, he/she should end up with the prize 2/3 of the time, vs 1/3 if he/she doesn't switch.  This game is an attempt to test this hypothesis.

## Intructions:
To play a single game: 
<br /><code>python MontyHallGame.py</code>

To run a simulation for multipl games:
<br /><code>python MontyHallGame.py 0 1000</code>
<br />Where:

- 0 is to stay with the door choice, whereas 1 is to switch doors
- 1000 is for the number of games


## Results:
Two simulations were performed with 1000 rounds each.
- The round with default in switching doors resulted in 682 wins.
- The round with default in staying with the original door resulted in 311 wins.
This result confirms with the original hypothesis of winning about 2/3 of the rounds if the contestant always switches doors.