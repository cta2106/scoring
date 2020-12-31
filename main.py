from monte_carlo import MonteCarlo
import yaml

if __name__ == "__main__":

    config = yaml.safe_load(open("config.yml"))
    mc = MonteCarlo(config["n_iter"])
    mc.run_simulation()
    print("Probability of boy winning is: {}".format(mc.boy_wins / config["n_iter"]))
