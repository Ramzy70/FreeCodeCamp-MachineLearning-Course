# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import itertools

import random

def player(prev_opponent_play,
           opponent_history=[],
           play_order= [{comb: 0 for comb in [''.join(move) for move in itertools.product('RPS', repeat=7)]}]):

  if not prev_opponent_play:
    prev_opponent_play = 'R'
  opponent_history.append(prev_opponent_play)

  last_ten = "".join(opponent_history[-7:])
  if len(last_ten) == 7:
    play_order[0][last_ten] += 1

  potential_plays = [
      "".join(opponent_history[-6:]) + "R",
      "".join(opponent_history[-6:]) + "P",
      "".join(opponent_history[-6:]) + "S",
  ]

  sub_order = {
      k: play_order[0][k]
      for k in potential_plays if k in play_order[0]
  }

  if not sub_order:
    # If no pattern is found, choose randomly
    prediction = random.choice(['R', 'P', 'S'])
  else:
    prediction = max(sub_order, key=sub_order.get)[-1:]

  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
  return ideal_response[prediction]
