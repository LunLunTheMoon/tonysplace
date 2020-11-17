label intro:
  scene bg_street
  "This is Tony's place, or at least that's what the locals call it."
  "It probably doesn't look like much to you, but to me, and the old-timers in the neighborhood, it's like a second home"
  "Especially to me. You see, Tony is my uncle."
  jump backInTheDay


label backInTheDay:
  scene bg_flashbackstreet
  """
  I've been coming here every day since I was 10 years old.

  This is where I came after Dad went to jail and Mom collapsed into pills and alchohol.
  
  Whenever I needed a hot meal or a safe place to do my homework...

  Whenever I needed a sense of family and a guiding hand to keep me on the right path...

  Whenver I needed to come home to a sane and warm place...

  I came to Uncle Tony's place

  So when I got word that Uncle Tony was ill, I left school in the middle of the semester to come home.
  """
  jump tonyDeathBed

label tonyDeathBed:
  scene bg_hospital
  """
  The salty old man lies dying in a hospital bed; his body eaten away by cancer. 
  
  His hollow eyes settle on me, alight with recognition and relief.

  I cannot believe how changed he is since I last saw him.
  """

  show tony dying at right
  tony "Good. *cough* Good. I hoped we could talk.."
  show max suprised at left
  max "Uncle Tony... "
  tony "Shut-up. Don't say anything. Just listen kid. You were the best thing to ever happen to us, you know? Maybe the only good thing."
  "My eyes tear up, as do his. He is my only family, and I love him like a father."
  tony "I'm leaving you the bar. The place is yours kid, god help you"
  max "No, Uncle Tony, I couldn't -- "
  tony "You can. You can and you WILL."
  "The tough old man grabs my hand with suprising strength, shaking it emphatically"
  tony "I'm glad you came, so you can hear it from my lips. So you can look in my eye, and hear my final wish from me, and not through some sonofabitch lawyer."
  max "..."
  tony """
    I want you to quit school. Fuck college you hear me?. It's a fucking scam kid. I told you then, and I tell you now. 

    Come home, save the place. It's sinking, and only you can make it float again kid.

    Do it for me -- for the neighborhood.

    I know you *cough* I know you understand kid. You're the only one left who understands.
  """
  max "We can talk about it when you get better Uncle Tony"
  tony "I ain't getting better kid. Listen. Listen close to what I'm tellin you.."
  "His grip on my hand tightens as he closes his eyes and lays back into his deathbead"
  tony """
    Now that I'm gone, there ain't but three kinds of people in this world kid.

    People who want to fuck your asshole...

    ...people who want to take my bar...

    ...and people who want to fuck your asshole and THEN take my bar!

    Don't trust a single one of them. Not-a-one. Especially the ones who call themselves my friends

    I only got one friend in this world kid. *wheeze* and I died holdin her hand.
  """

  jump tonyDead

label tonyDead:
  scene black
  max "Uncle Tony?"
  max "UNCLE TONY?!"

  jump firstDay

