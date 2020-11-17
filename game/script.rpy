# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define max = Character("Max")
define tony = Character("Tony")
define sky = Character("Skyler")
define julia = Character("Julia")

python:
  DEBUG = True
  GAME.reset()
  ePLAYER.flags = {}
  ePLAYER.attributes = {}
  ePLAYER.stats = {}
  ePLAYER.multipliers = {}
  ePLAYER.inventory = {}
  ePLAYER.wearing = {}
  ePLAYER.wear( Wearable('panties', 'underwear', 'white cotton panties' ))
  ePLAYER.wear( Wearable('bra', 'undershirt', 'pink underwire bra' ))
  ePLAYER.wear( Wearable('tanktop', 'shirt', 'black tank-top' ))
  ePLAYER.wear( Wearable('jeans', 'pants', 'blue-jeans' ))

# The game starts here.

label start:
  jump intro
