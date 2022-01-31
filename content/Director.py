from content.Cards import cards

class director:
    def __init__(self):
        self.card1 = 0
        self.card2 = 0
        self.action = ""
        self.score = 300
        self.playing = True
        self.succeed = True

        card = cards()
        card.new_card()
        self.card1 = card.card

    def start(self):
        print("Remember: if you wish to quit, just type DONE or END.")
        while self.playing:
            self.get_input()
            if not self.playing:
                break
            self.game_tick()
            self.output_state()
        print("Thanks for playing!")

    def get_input(self):
        valid = False
        while not valid:
            self.action = input(f"The current card is {self.card1}\nDo you bid High, or Low? [h/l] ").lower()
            if self.action == "h" or self.action == "l":
                valid = True
            elif self.action == "done" or self.action == "end":
                valid = True
                self.playing = False
            else:
                print("Invalid input, try again.")

    def game_tick(self):
        card = cards()
        card.new_card()
        self.card2 = card.card
        if self.action == "h":
            if self.card1 <= self.card2:
                self.score += 100
                self.succeed = True
            else:
                self.score -= 75
                self.succeed = False
        elif self.action == "l":
            if self.card1 >= self.card2:
                self.score += 100
                self.succeed = True
            else:
                self.score -= 75
                self.succeed = False
        if self.score <= 0:
            self.playing = False
        self.card1 = self.card2

    def output_state(self):
        print(f"The next card was: {self.card2}")
        if self.succeed:
            print("You guessed Right!")
        else:
            print("You guessed Incorrectly.")
        print(f"Your score is: {self.score}\n\n")