from engine.main import Game
import script
import scriptblue
import scriptred
import sample_scripts.sample1
import sample_scripts.sample2
import sample_scripts.sample3
import scriptblue_development
import scriptred_development
import script_development

if __name__ == "__main__":
    G = Game((40, 40), script_development, script_development)
    G.run_game()
