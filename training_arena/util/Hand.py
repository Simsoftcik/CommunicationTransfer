from training_arena.util.enums import *
from random import shuffle, choice
import random

class Hand():
    def __init__(self, seed):
        random.seed(seed)
        self.deck = self.generate_deck() #whole card deck
        self.hand = self.generate_hand() #randomly generated hand
        self.points = self.count_points() #Milton work's points (hcp)
        self.distribution = self.get_distribution() #0 - spades, 1 - hearts, 2 - diamonds, 3 - clubs
        self.longest_suit = self.get_longest_suit() #tuple (suit, lenght)
        self.second_longest_suit = self.get_second_longest_suit() #LENGHT ONLY!! not a tuple, because not necessary
        self.longest_major_suit = self.get_longest_major_suit() #tuple (suit, lenght)
        self.is_balanced = self.get_is_balanced() #Boolean; tells if hand has 2-5 cards in every suit
        self.is_strictly_balanced = self.get_is_strictly_balanced() #Boolean; tells if hand has 2-4 cards in every suit
        self.vulnerability = choice([Vulnerability.GREEN, Vulnerability.RED, Vulnerability.VULNERABLE, Vulnerability.NONVULNERABLE]) #vulnerability
        self.first_hand_num = choice([1,2,3,4]) #on which position sits dealer
        self.hand_num = choice([1,2,3,4]) #on which hand the opening takes place
        self.vulnerability_colors = self.generate_vulnerability_colors()
        self.is_candidate_for_block= self.longest_suit[1] >= 6 or self.has_two_fives() #tells has blocking distribution
        self.sort_hand()

        
###########################################################################################################
#Internal functions for functionality of the class
    """generates deck"""
    def generate_deck(self):
        cards = []
        for suit in Suit:
            for height in Height:
                cards.append((height, suit))
        return cards

    """generates random hand"""
    def generate_hand(self):
        shuffle(self.deck)
        return self.deck[:13]

    """counts Milton Work's points for a hand"""
    def count_points(self):
        points = 0
        for card in self.hand:
            if card[0] == Height.JACK:
                points+=1
            elif card[0] == Height.QUEEN:
                points+=2
            elif card[0] == Height.KING:
                points+=3
            elif card[0] == Height.ACE:
                points+=4
        return points

    """finds number of cards in each color"""
    def get_distribution(self):
        clubs = diamonds = hearts = spades = 0
        for card in self.hand:
            if card[1] == Suit.CLUBS:
                clubs+=1
            elif card[1] == Suit.DIAMONDS:
                diamonds+=1
            elif card[1] == Suit.HEARTS:
                hearts+=1
            elif card[1] == Suit.SPADES:
                spades+=1
        return (spades, hearts, diamonds, clubs)
    
    
    """checks if hand has strictly balanced distribution (2-4 cards each color)"""
    def get_is_strictly_balanced(self):
        for num_in_suit in self.distribution:
            if num_in_suit<2 or num_in_suit>4:
                return False
        return True
    
    """checks if hand has balanced distribution (2-5 cards each color)"""
    def get_is_balanced(self):
        for num_in_suit in self.distribution:
            if num_in_suit<2 or num_in_suit>5:
                return False
        return True
    
    """check if points are in range (a,b)"""
    def points_in_range(self, a,b):
        return self.points>=a and self.points<=b
    
    """tells if hand has at least 5 spades"""
    def has_five_spades(self):
        return self.distribution[0]>=5

    """tells if hand has at least 5 hearts"""
    def has_five_hearts(self):
        return self.distribution[1]>=5

    """returns the oldest among the longest colors"""
    def get_longest_suit(self):
        longest = max(self.distribution)
        for index, num_in_suit in enumerate(self.distribution):
            if num_in_suit == longest:
                if index == 0:
                    return (Suit.SPADES, longest)
                elif index == 1:
                    return (Suit.HEARTS, longest)
                elif index == 2:
                    return (Suit.DIAMONDS, longest)
                elif index == 3:
                    return (Suit.CLUBS, longest)
    
    """returns the second longest suit"""
    def get_second_longest_suit(self):
        idx_of_longest = 3 #default value
        if self.longest_suit[0] == Suit.CLUBS:
            idx_of_longest = 3
        elif self.longest_suit[0] == Suit.DIAMONDS:
            idx_of_longest = 2
        elif self.longest_suit[0] == Suit.HEARTS:
            idx_of_longest = 1
        elif self.longest_suit[0] == Suit.SPADES:
            idx_of_longest = 0

        second_longest = 0

        for index, num_in_suit in enumerate(self.distribution):
            if(num_in_suit > second_longest and index != idx_of_longest):
                second_longest = num_in_suit
        return second_longest
                
    """returns the oldest among the longest major colors"""
    def get_longest_major_suit(self):
        if self.distribution[1]>self.distribution[0]:
            return (Suit.HEARTS, self.distribution[1])
        else:
            return (Suit.SPADES, self.distribution[0])
        
    """Tells if hand has two five-carded suits"""
    def has_two_fives(self):
        fives_count = 0
        for num_in_suit in self.distribution:
            if num_in_suit==5:
                fives_count+=1
        return fives_count==2
    
    """Gets Bid that should be bidded supposing the hand is of blocking type"""
    def get_block_candidate(self):
        # Clubs blocks
        if self.distribution[3] == 7:
            return Bid.THREE_CLUBS.value
        if self.distribution[3] >= 8:
            return Bid.FOUR_CLUBS.value
        
        # Diamonds blocks
        if self.distribution[2] == 7:
            return Bid.THREE_DIAMONDS.value
        if self.distribution[2] >= 8:
            return Bid.FOUR_DIAMONDS.value
        
        # Hearts blocks
        if self.distribution[1] == 6:
            return Bid.TWO_DIAMONDS.value
        if self.distribution[1] == 7:
            return Bid.THREE_HEARTS.value
        if self.distribution[1] >= 8:
            return Bid.FOUR_HEARTS.value
        
        # Spades blocks
        if self.distribution[0] == 6:
            return Bid.TWO_DIAMONDS.value
        if self.distribution[0] == 7:
            return Bid.THREE_SPADES.value
        if self.distribution[0] >= 8:
            return Bid.FOUR_SPADES.value
        
        #Duo color hands
        if self.distribution[1] == 5 and (self.distribution[0] == 5 or self.distribution[2] == 5 or self.distribution[3] == 5):
            return Bid.TWO_HEARTS.value
        if self.distribution[0] == 5 and (self.distribution[2] == 5 or self.distribution[3] == 5):
            return Bid.TWO_SPADES.value
        
        else:
            return Bid.PASS.value

###########################################################################################################
# external functions for the arena
    """what should you bid as an opening with this hand (according to polish system called 'Strefa')"""
    def what_should_open(self):
        if self.points>=23:
            return Bid.TWO_CLUBS.value, 'z rękami 23+HCP otwieramy Acola'
        
        # Section below is for all situations limited 0-22hcp (additionaly hands according to rule of 20)
    
        if self.points>=12 or (self.points + self.longest_suit[1]+self.second_longest_suit>=20):
            # major priority openings
            if self.longest_major_suit[1]>=5:
                if self.points_in_range(15,17) and self.is_balanced:
                    return Bid.ONE_NT.value, 'mając 15-17 HCP oraz 2-5 kart w każdym kolorze, otwieramy 1NT'
                elif self.points_in_range(21,22) and self.is_balanced:
                    return Bid.TWO_NT.value, 'ze składem zrównoważonym w przedziale 21-22HCP otwieramy 2NT'
                else:
                    if self.longest_major_suit[0]==Suit.SPADES:
                        return Bid.ONE_SPADES.value, 'z piątką pików w przedziale 12-22pc w innych przypadkach niż 15-17 na zrównoważonym lub 21-22 na zrownoważonym otwieramy 1S'
                    else:
                        return Bid.ONE_HEARTS.value, 'z piątką kierów w przedziale 12-22pc w innych przypadkach niż 15-17 na zrównoważonym lub 21-22 na zrównoważonym lub posiadając co najmniej tak długi kolor pikowy otwieramy 1S'
            
            # no major priority detected, then:

            # balanced hands with no major longers
            if (self.is_strictly_balanced and (self.points_in_range(12,14) or self.points_in_range(18,20))):
                return Bid.ONE_CLUBS.value, 'ze składem zrównoważonym w przedziale 12-14 lub 18-20 HCP otwieramy 1C'
            elif self.is_balanced:
                if self.points_in_range(15,17):
                    return Bid.ONE_NT.value, 'mając 15-17 HCP oraz 2-5 kart w kazdym kolorze, otwieramy 1NT'
                elif self.points_in_range(21,22):
                    return Bid.TWO_NT.value, 'ze składem zrównoważonym w przedziale 21-22HCP otwieramy 2NT'
                
            # unbalanced hands with no major longers
            if self.longest_suit[1]>=5 and self.longest_suit[0] == Suit.DIAMONDS: 
                return Bid.ONE_DIAMONDS.value, 'Gdy nie mamy starszej piątki i nie są spełnione warunki o składzie zrównoważonym, a nasz najdłuższy kolor to karo i mamy w nim 5 kart i mamy 12-22HCP, powinniśmy otworzyć 1D'
            elif self.longest_suit[1]>=5 and self.longest_suit[0] == Suit.CLUBS:
                return Bid.ONE_CLUBS.value, 'Gdy nie mamy starszej piątki, warunki o składzie zrównoważonym nie są spełnione, a nasz najdłuższy kolor to trefl i mamy w nim 5 kart i mamy 12-22HCP, otwieramy 1c'
            
            #last possible scenario- 4441 distribution
            if self.distribution[2]==1:
                return Bid.ONE_CLUBS.value, 'Ze składem 4441 i singlem karo otwieramy trefla'
            else:
                return Bid.ONE_DIAMONDS.value, 'Ze składem 4441 otwieramy karo'


        # Blocks
        if self.is_candidate_for_block:
            block_candidate = self.get_block_candidate();

            # vulnerable
            if self.vulnerability == Vulnerability.VULNERABLE:
                if self.points_in_range(0,10):
                    return block_candidate, 'Mamy dostatecznie dużo punktów, by blokować z tą ręką w korzystnych'
            
            # all green
            elif self.vulnerability == Vulnerability.GREEN:
                if self.hand_num == 1:
                    if self.points_in_range(3,10):
                        return block_candidate, 'Mamy dostatecznie dużo punktów, by blokować z tą ręką'
                elif self.hand_num == 2:
                    if self.points_in_range(5,10):
                        return block_candidate, 'Mamy dostatecznie dużo punktów, by blokować z tą ręką'
                elif self.hand_num == 3:
                    if self.points_in_range(3,10):
                        return block_candidate, 'Mamy dostatecznie dużo punktów, by blokować z tą ręką'
                    
            # all red
            elif self.vulnerability == Vulnerability.RED:
                if self.hand_num == 1:
                    if self.points_in_range(5,10):
                        return block_candidate, 'Mamy dostatecznie dużo siły, by blokować z tą ręką pomimo obustronnych czerwonych założeń'
                elif self.hand_num == 2:
                    if self.points_in_range(7,10):
                        return block_candidate, 'Mamy dostatecznie dużo siły, by blokować z tą ręką pomimo obustronnych czerwonych założeń'
                elif self.hand_num == 3:
                    if self.points_in_range(3,10):
                        return block_candidate, 'Mamy dostatecznie dużo siły, by blokować z tą ręką pomimo obustronnych czerwonych założeń'
                    
            # non-vulnerable
            elif self.vulnerability == Vulnerability.NONVULNERABLE:
                if self.hand_num == 1:
                    if self.points_in_range(7,10):
                        return block_candidate, 'Założenia są niekorzystne, jednak mamy odpowiedzialną kartę na blok i możemy go zaryzykować'
                elif self.hand_num == 2:
                    if self.points_in_range(9,10):
                        return block_candidate, 'Załozenia są niekorzystne, jednak mamy odpowiedzialną kartę na blok i możemy go zaryzykować'
                elif self.hand_num == 3:
                    if self.points_in_range(5,10):
                        return block_candidate, 'Załozenia są niekorzystne, jednak mamy odpowiedzialną kartę na blok i możemy go zaryzykować'
        
        return Bid.PASS.value, 'Nie ma powodów by otworzyć z tą ręką (lub algorytm ich nie zna :)))'
    
    def sort_hand(self):
        def sort_key(card):
            value = i = 0
            match card[0]:
                case Height.TWO:
                    value = 0
                case Height.THREE:
                    value = 1
                case Height.FOUR:
                    value = 2
                case Height.FIVE:
                    value = 3
                case Height.SIX:
                    value = 4
                case Height.SEVEN:
                    value = 5
                case Height.EIGHT:
                    value = 6
                case Height.NINE:
                    value = 7
                case Height.TEN:
                    value = 8
                case Height.JACK:
                    value = 9
                case Height.QUEEN:
                    value = 10
                case Height.KING:
                    value = 11
                case Height.ACE:
                    value = 12
            
            match card[1]:
                case Suit.CLUBS:
                    i = 0
                case Suit.DIAMONDS:
                    i = 1
                case Suit.HEARTS:
                    i = 2
                case Suit.SPADES:
                    i = 3
        
            return value + 13 * i
        
        return sorted(self.hand, key=sort_key, reverse=True)
    
    def generate_vulnerability_colors(self):
        colors = []
        users_position = ((self.hand_num + self.first_hand_num) % 4) + 1
        is_on_even = users_position % 2

        if self.vulnerability == Vulnerability.GREEN:
            for _ in range(4):
                colors.append('#00b33c')
        
        elif self.vulnerability == Vulnerability.RED:
            for _ in range(4):
                colors.append('#ff1a1a')

        elif self.vulnerability == Vulnerability.NONVULNERABLE:
            for i in range(1,5):
                if i % 2 == is_on_even:
                    colors.append('#ff1a1a')
                else:
                    colors.append('#00b33c')

        elif self.vulnerability == Vulnerability.VULNERABLE:
            for i in range(1,5):
                if i % 2 != is_on_even:
                    colors.append('#ff1a1a')
                else:
                    colors.append('#00b33c')
        
        return colors