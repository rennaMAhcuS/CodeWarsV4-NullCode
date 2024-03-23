from engine.main import Game
import script
import script_development
import sample_scripts.scriptred as red
import testing_scripts.script_opponent as opponent
from random import randrange as rand

if __name__ == "__main__":
    dim = int(rand(10, 65, 2))
    G = Game((dim, dim), opponent, script_development)
    # G = Game((20, 20), opponent, script_development)
    G.run_game()
