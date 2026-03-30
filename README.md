To run the code in the terminal, use: python3 driver.py -o ai -x ai
If you wish to play against the ai, then use: python3 driver.py -x ai
You can choose for the ai to be either -x or -o

This code uses alpha-beta pruning that is depth limited to reduce the amount of computation time needed for each move the "ai" makes.
This can be changed in the minimax function in minimax.py

Minimax.py uses a heuristic which scores the board after every turn based on how many connections each player has.
If there is an extra connection that can be made, a greater score is returned than if that specific connection cannot be used more.
