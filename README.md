# Numbered Door Game
Numbered Door Game is a reimplementation of the door puzzles from Zero Escape: 999. This version allows the player to choose what numbers are used on the door while leaving the others behind. The player must progress through all 4 stages to win.

STILL A WORK IN PROGRESS
 
## Installation
```
pip install --save numbered-door-game
```
 
## Controls

#### Keyboard
 - Use arrow keys to move around and highlight elements, numbers and doors.
 - Use ENTER key to select numbers and add to selected door, or switch between active door.
 
#### Mouse
 - Use the mouse to highlight elements, numbers and doors. This is an alternative to using the arrow keys.
 - Use MOUSE 1 to select a highlighted element. This is an alternative to pressing the ENTER key.
  
## How to Play
 - The goal of the game is to add the available numbers together in order to get the digital root of the door.

```
   A digital root is the single digit value obtained by recursively summing digits, on each iteration
   using the result from the previous iteration to compute a digit sum. The process continues until a
   single-digit number is reached.
   
   Example
      Door value        = 9
      Numbers available = _ _ 3 _ _ 6 _ _ 9
	  
	  calculate) 
		     3 + 6 + 9 = 18
		       Add all the digits together to get 18
		     
	             18 = 1 + 8 = 9
		       18 is not a digit so we have to add the digits that make up this number in order 
		       to reduce the result to a its DIGITAL ROOT. The digits 1 and 8 make up 18 so we 
		       add those digits together resulting in 9. 9 is a digit so there is no need to 
		       reduce the result further.

			- OR -

	  calculate) 
	             3 + 9 = 12
		       We are given 3 digits: 1, 6, 9, so lets start with a different approach than 
		       above. Adding two digits, 3 and 9, resulting in 12.
		       
	             12 = 1 + 2 = 3
		       12 is not a digit so we need to reduce this number to its digital root. We have
		       1 and 2 which when added together result in 3.
		     
		     3 + 6 = 9
		       We still have the digit 6 that needs to be added to the answer, so we add 6 to
		       the result from the digital root of 3 + 9 which was 3. Adding 3 and 6 results in
		       9 with 9 being a digit so we have found our digital root and solution to the problem.
				 
	  Its also interesting to note that 9 never changes the digital root of a problem.
```
 
 - The player can only use each provided number once,and the player has to use 0 or 3-5 numbers for a door's solution. The solution will be counted as invalid otherwise.
 - After a stage is completed, all numbers used to get through the door(s) from the previous stage will then be available for the next stage rendering the unused numbers unavailable for the rest of the game.
 - Only one door has to be solved to proceed to the next stage, but this will hinder the player's progression and may stop them from winning at all.
 - In the HARD difficulty you must use all the available digits on the door.
 
## API
 
## Tests
 
## Acknowledge
 - Spike Chunsoft
 
