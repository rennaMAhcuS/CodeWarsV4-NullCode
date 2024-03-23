from engine.main import Game
# import script
# import script_development
import sample_scripts.scriptred as red
import testing_scripts.script_opponent as opponent
from random import randrange as rand

if __name__ == "__main__":
    # dim = rand(2, 65, 2)
    G = Game((40, 40), red, opponent)
    G.run_game()
