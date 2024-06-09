from enumchoice import EnumChoice
from enum import Enum

class Suit(Enum):
    CLUBS = '♣'
    DIAMONDS = '♦'
    HEARTS = '♥'
    SPADES = '♠'

class Height(Enum):
    TWO = '2'
    THREE = '3'
    FOUR = '4'    
    FIVE = '5'
    SIX = '6'
    SEVEN ='7'
    EIGHT ='8'
    NINE ='9'
    TEN ='10'
    JACK ='J'
    QUEEN ='Q'
    KING ='K'
    ACE ='A'

class Vulnerability(Enum):
    GREEN = "All vunerable"
    RED = "All non-vunerable"
    VULNERABLE = "You: vurnelable, opponents: non-vurnerable"
    NONVULNERABLE = "You: non-vurnelable, opponents: vurnerable"

class Bid(Enum):
    PASS = 'pass'
    DOUBLE = 'x'
    REDOUBLE = 'xx'
    ONE_CLUBS = '1♣'
    ONE_DIAMONDS = '1♦'
    ONE_HEARTS = '1♥'
    ONE_SPADES = '1♠'
    ONE_NT = '1NT'
    TWO_CLUBS = '2♣'
    TWO_DIAMONDS = '2♦'
    TWO_HEARTS = '2♥'
    TWO_SPADES = '2♠'
    TWO_NT = '2NT'
    THREE_CLUBS = '3♣'
    THREE_DIAMONDS = '3♦'
    THREE_HEARTS = '3♥'
    THREE_SPADES = '3♠'
    THREE_NT = '3NT'
    FOUR_CLUBS = '4♣'
    FOUR_DIAMONDS = '4♦'
    FOUR_HEARTS = '4♥'
    FOUR_SPADES = '4♠'
    FOUR_NT = '4NT'
    FIVE_CLUBS = '5♣'
    FIVE_DIAMONDS = '5♦'
    FIVE_HEARTS = '5♥'
    FIVE_SPADES = '5♠'
    FIVE_NT = '5NT'
    SIX_CLUBS = '6♣'
    SIX_DIAMONDS = '6♦'
    SIX_HEARTS = '6♥'
    SIX_SPADES = '6♠'
    SIX_NT = '6NT'
    SEVEN_CLUBS = '7♣'
    SEVEN_DIAMONDS = '7♦'
    SEVEN_HEARTS = '7♥'
    SEVEN_SPADES = '7♠'
    SEVEN_NT = '7NT'



print(Vulnerability.GREEN.value)