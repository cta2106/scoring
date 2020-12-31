## Probability in Scoring
Simulating a game of scoring between a boy that plays randomly and a computer that plays optimally

From Alexander Bogomolny's [book](https://www.amazon.com/Cut-Knot-Probability-Alexander-Bogomolny/dp/157955041X): 
[@CutTheKnotMath](https://twitter.com/CutTheKnotMath)

## Problem
A boy plays a game of Scoring with a computer without yet learning to play optimally, but the computer makes no mistakes. They start with a pile of 14 stones and remove 1, 2, 3, 4, or 5 stones at a time. The player to remove the last stone wins. The boy goes first.

What is the probability of his winning the game?

## Solution
Will leave as an exercise to the reader. Final answer is 0.04.

## Running Monte-Carlo Simulation
Update the desired number of iterations in your simulation by modifying `n_iter` in `config.yml` and run the following command in your terminal.

```python
python main.py
```

