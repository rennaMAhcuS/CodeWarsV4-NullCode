from engine.main import Game
import scriptblue
import scriptred
import sample_scripts.sample1
import sample_scripts.sample2
import sample_scripts.sample3

if __name__ == "__main__":
    G = Game((40, 40), scriptred, sample_scripts.sample3)
    G.run_game()
