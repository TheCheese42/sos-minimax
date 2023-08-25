# SOS Minimax

## The SOS game

Alice and Bob play against each other. There are 2000 Fields in a row. Alice starts and both set alternately an S or an O in any empty field. The first one completing an "SOS" wins, while it doesn't matter who set the other two letter of the "SOS". Proof that there is a way for Bob to always win.

## Usage

```bash
git clone https://github.com/NotYou404/sos-minimax
cd sos-minimax
python -i -m sos_minimax
```

This makes two bots play against each other:

```python
>>> score = 0
>>> board = " " * 2000
>>> while "SOS" not in board and " " in board:
...     score, board = best_move(board)
...     print(score, board)
>>> if score == -1:
...     s = "Bob looses!"
>>> elif score == 1:
...     s = "Bob wins!"
>>> else:
...     s = "Draw!"
>>> print(s)
```

Performance warning: There are way too many possible game states to go past a board length of 20, trust me.

## Performance

To increase what's possible you can set two constants:

```python
MAX_DEPTH = 100
MAX_POSSIBLE_NEW_STATES = 100
```

These are the defaults. Max depth limits the recursion depth of the minimax function calling itself. For a 10 fields board this is most of the time ~12, for a 20 fields board it's usually around 17.
Max possible new states limits the amount of items consumed from the possible_new_states() generator function. Obviously, both options (especially the latter) will decrease precision EXTREMELY!
