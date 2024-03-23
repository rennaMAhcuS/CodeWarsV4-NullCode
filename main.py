from engine.main import Game
from random import randrange as rand
# import script
import script_development
import testing_scripts.script_opponent as opponent

if __name__ == "__main__":
    dim = int(rand(40, 65, 2))
    G = Game((dim, dim), opponent, script_development)
    # G = Game((20, 20), opponent, script_development)
    G.run_game()
