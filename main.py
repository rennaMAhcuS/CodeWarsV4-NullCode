from engine.main import Game
# import script
import script_development
import sample_scripts.scriptred
import testing_scripts.script_opponent as opponent
from random import randrange as rand

if __name__ == "__main__":
    # dim = rand(2, 65, 2)
    G = Game((40, 40), sample_scripts.scriptred, sample_scripts.scriptred)
    G.run_game()
