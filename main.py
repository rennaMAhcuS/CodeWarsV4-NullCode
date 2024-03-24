from engine.main import Game
from random import randrange as rand
import script
import testing_scripts.script_opponent_A as opponentA
import testing_scripts.script_opponent_B as opponentB
import testing_scripts.script_opponent_C as opponentC
import testing_scripts.script_opponent_D as opponentD


if __name__ == "__main__":
    dim = int(rand(40, 65, 2))
    # dim = 40
    G = Game((dim, dim), opponentA, script)
    G.run_game()
