# Adversial Enemy in Games
Little self-learning project for Adversial AI Agents in games and stuff, like Tic Tac Toe and Connect 4


## To Download
1. If you want to try the Tic tac toe, just download the .exe file from Release
2. If you want to try the Connect 4, then download the files within the `Connect 4` folder, and run `pip install -r requirements.txt` from the same folder.


## Games
### Tic Tac Toe
Well known "X-O" game, get three X or O in a row in a 3x3 grid and you win. I thought this would be perfect to learn how algorthims like min-maxing would work. Tic Tac Toe is considered a "zero sum game", because, against two players, only one wins, and other loses. The win of Player 1 is equivalent to the loss of player 2

- Since there is a countable (albeit still large) number of total game states, I could let the algorithm run for the entire game (39=19,683 total states)
- A simple min-maxing alg which basically plays how a normal "smart" player would play: "If I were the enemy, what move would I make to make me at a disadvantage. I need to counter that move."
- If a move is advantageous for the AI (aka a win), it assigns it a score of +1. And, a draw, is a score of 0, and a loss is a score of -1.
- Since Tic-Tac-Toe is considered a solved game (that is, all game states are mapped / can be mapped quickly), the AI here is a perfect player. What this means is that you cannot win against this AI at all. At most, you can get yourself to draw.

The Big O notation for Tic Tac Toe with only min-maxing (and no time saving algorithms) would be $O(b!)$ (Move 1, AI sees 9 spots. Move 3 (after me and AI moved), AI sees 7 spots... so on)

![20260206-2211-46 1006084](https://github.com/user-attachments/assets/e76acbc2-1d74-498c-9a39-930d494c9761)


### Connect 4
Game where you have to 'drop' (that is, gravity is there: you cannot place it mid-air) tiles into a 6x7 grid. Getting 4 of your tiles in horizontal, vertical or diagnol and you win. This also uses min-maxing, but since there are now way too many game states (4,531,985,219,092 to be exact), calculating each and every one of them before the game starts will take several hundred years on a single modern PC. Hence, I implemented Alpha-Beta Pruning, and Depth Limiting in this, so that at most it takes only a few seconds.
#### Alpha-Beta Pruning
This is basically the "Why bother?" logic. When the AI is searching through a branch, it keeps track of the best move it’s already found ($\alpha$) and the best move the human can make to screw it over ($\beta$).
If the AI starts looking at a new path and sees that the human can force a score that is already worse than a move the AI found earlier, it just stops looking. 

Mathematically, whenever $\alpha \geq \beta$, we "prune" the branch and move on.

#### Depth Limiting & Iterative Deepening
Since looking all the way to the end of a 42-turn game is computationally impossible (roughly $7^{42}$ states), I implemented **Iterative Deepening**. Instead of just jumping to a fixed depth, the AI searches progressively deeper. Starting at 1 move ahead and reaching up to the `depth_limit`. This ensures that the agent always has a "best move" stored from the previous depth in case of a timeout.

Currently, the agent uses a Absolute win kind of utility check. If it reaches the depth limit without seeing a "Game Over" state, it evaluates the board as neutral (0). What this basically means is that the AI only cares about absolute wins.. potential wins for are as good as an empty board (a score of 0)

The Big O notation without any optimizing would be $O(b^{d})$, where $b=7$ and $d = 42$, but with the optimizations ive done it is closer to $O(b^{d/2})$.

![20260206-2208-00 9455303](https://github.com/user-attachments/assets/2df4735f-dfab-48f7-96d7-21c256c83d5e)


### Note
During playtesting for connect 4, I noticed a "First-Column Bias" where the AI often prefers the leftmost columns. This is a logical result of the terminal-only scoring: if the AI can't find a guaranteed win within the depth limit, all moves return a score of 0, and the algorithm defaults to the first valid action it evaluated (Column 0).
