import random

class Monty():
    def __init__(self):
        self.switch_wins = 0
        self.switch_total = 0
        self.stay_wins = 0
        self.stay_total = 0
        self.doors = [0,0,0]
        self.new = [0,0] # [player_choice,remaining_door]
        self.winning_index = 0
        self.pick_index = 0
        self.switch_doors = 0
        self.final_choice = 0


    def assign_doors(self):
        # Pick a door to be winning, and assign it's value to 1
        # 0 = losing door, 1 = winning door
        self.winning_index = random.randint(0,2)
        self.doors[self.winning_index] = 1

    def pick_door(self):
        # Pick a random door for the player choice
        self.pick_index = random.randint(0,2)

    def remove_door(self):
        # If the player picked the right door, set index 0 to 1 (1/3 times)
        # If the player picked the wrong door, set index 1 to 1 (2/3 times)
        # This sets up the '50/50' scenario
        if (self.doors[self.pick_index] == 1):
            self.new[0] = 1
        else:
            self.new[1] = 1

    def switch(self):
        # Decide randomly if the player switches doors
        self.switch_doors = random.randint(0,1)
        # If they switch, their final choice is in new[1]. Otherwise it's in new[0]
        if (self.switch_doors == 1):
            self.final_choice = self.new[1]
        else:
            self.final_choice = self.new[0]

    def tally_results(self):
        # If switch doors is 0, the player stayed
        if (self.switch_doors == 0):
            # If the final choice is 1, the player won
            if (self.final_choice == 1):
                self.stay_wins += 1
            self.stay_total += 1
        else:
            if (self.final_choice == 1):
                self.switch_wins += 1
            self.switch_total += 1

    def print_results(self):
        message = ""
        if (self.switch_doors == 1):
            message += "Switched"
        else:
            message += "Stayed"
        message += " and "
        if (self.final_choice == 1):
            message += "won!"
        else:
            message += "lost!"
        print(message)

        switch_percent = 0
        stay_percent = 0
        if (self.switch_total > 0):
            switch_percent = (float(self.switch_wins) / float(self.switch_total)) * 100
        if (self.stay_total > 0):
            stay_percent = (float(self.stay_wins) / float(self.stay_total)) * 100
        print("Switched " + str(self.switch_total) + " times and won " + str(self.switch_wins) + " times.")
        print("Stayed " + str(self.stay_total) + " times and won " + str(self.stay_wins) + " times.")
        print("Total: " + str(self.switch_total + self.stay_total))
        print("Switch win percentage: " + str(switch_percent) + "%")
        print("Stay win percentage: " + str(stay_percent) + "%")
        print("--------------------------------------------------")

    def reset(self):
        self.doors = [0,0,0]
        self.new = [0,0]
        self.winning_index = 0
        self.pick_index = 0
        self.switch_doors = 0
        self.final_choice = 0

if __name__ == "__main__":
    valid = False
    run_count = 1
    while(valid == False):
        run_count = input("Run how many times?\n")
        try:
            run_count = int(run_count)
            valid = True
        except:
            print("Enter a valid integer")

    monty = Monty()
    for i in range(run_count):
        monty.assign_doors()
        monty.pick_door()
        monty.remove_door()
        monty.switch()
        monty.tally_results()
        monty.print_results()
        monty.reset()
