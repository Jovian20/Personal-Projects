import random
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10

        elif self.rank == 'A':
            return 11

        else:
            return int(self.rank)

    def __str__ (self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit,rank) for suit in ['Diamonds', 'Clovers', 'Hearts', 'Spades'] for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]
        random.shuffle(self.cards)

    def deal_cards(self):
        return self.cards.pop()

class Blackjack:
    def __init__ (self):
        self.Deck = Deck()
        self.players_cards = []
        self.dealers_cards = []
        self.dealers_points = 0
        self.players_points = 0

    def deal_initial_cards(self):
        for _ in range(2):
            self.players_cards.append(self.Deck.deal_cards())
            self.dealers_cards.append(self.Deck.deal_cards())

    def calculate_hand_value(self, hand):
        value = sum(card.value() for card in hand)
        aces = sum(1 for card in hand if card.rank == 'A')
        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value

    def play(self):
        self.deal_initial_cards()
        print("Player's hands: ", ",".join(str(card) for card in self.players_cards))
        print("Dealer's hand:", str(self.dealers_cards[0]), "and a hidden card")

        while True:
            player_value = self.calculate_hand_value(self.players_cards)
            if player_value > 21:
                print("Player busts!! Dealer is the winner!")
                return "dealer"

            action = input("Do you want to hit or stand? ").strip().lower()

            if action == 'hit':
                self.players_cards.append(self.Deck.deal_cards())
                print("Player's hands: ", ",".join(str(card) for card in self.players_cards))

            elif action == 'stand':
                break

        while self.calculate_hand_value(self.dealers_cards) < 17:
            self.dealers_cards.append(self.Deck.deal_cards())

        print("Dealer's hands: ", ",".join(str(card) for card in self.dealers_cards))
        dealer_value = self.calculate_hand_value(self.dealers_cards)
        player_value= self.calculate_hand_value(self.players_cards)

        if dealer_value > 21 or dealer_value < player_value:
            print("Player wins!!")
            return "player"

        elif dealer_value > player_value:
            print("Dealer wins!!")
            return "dealer"

        else:
            print("It's a tie!!")
            return "tie"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    player_points = 0
    dealer_points = 0

    while True:
        game = Blackjack()
        result = game.play()

        if result == "player":
            player_points += 1
        elif result == "dealer":
            dealer_points += 1

        print(f"Player's points: {player_points}, Dealer's points = {dealer_points}")

        next_game = input("Do you want to play another game? (Y/N)").strip().lower()
        print("\n")
        if next_game != "y":
            print("Thanks for playing!")
            break


