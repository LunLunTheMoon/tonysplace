label weekend_cleaning: 
  $wcd = GAME.week
  if wcd == 0:
    jump weekend_cleaning_start
  else: 
    jump weekend_cleaning_random


label weekend_cleaning_start:
  scene bg_office
  $ M = title(eSKYLER,'max')

  "Tuesday is the slowest day of the week for any bar, and morning the slowest time. "
  "To pass some time, I open Julia's report and thumb through the first few pages skeptically."
  "It appears to be an analysis of how environmentals like cleanliness effect alchohol sales."
  "The study covers three of her resturant properties in three vastly different neighborhoods"

  max "This can't be right.."

  "The numbers are unbelievable."
  "Every bar, independent of any other factors show a 30% week over week increases in alchohol sales for several months.. "
  "Due to nothing but a weekly deep-cleaning"
  "I think about Tony's place.. "
  "How your shoes stick to the floor when you walk..."
  "How everything smells like stale cigarette ash and piss..."
  "The bubblegum under the tables, and the greasy streaked mirror over the bar."

  max "SKYLER!"

  show skyler at right
  
  skyler "Yeah [M]"

  max "I'm looking at some projections here, and the bottom line is, it could really save our bacon if we could get the place cleaned once a week"

  "She raises an incredulous eyebrow; already aware of what I'm asking. She doesn't seem inclined to help."

  skyler "So hire a cleanining company"

  max "You know we can't afford that. I need your help. I can't do it alone. I was thinking Tuesday Morning.."

  skyler "Lemme stop you there. What's in this for me?"
  
  "skyler tilts her head to the side expectantly, placing one hand on her hip"

  jump wc_choice

label wc_choice:
  menu:
    "Put the bitch in her place":
      jump wc_are_u_sure_1
    "Bargain/beg her":
      jump wc_are_u_sure_2


label wc_are_u_sure_1:
  "This choice will put you in a dominant position with Skyler."
  "Are you sure this is what you want?" 

  menu: 
    "Yep. Skyler belongs to me now.":
      jump weekend_cleaning_1
    "Um... nah, this doesn't feel right.":
      jump wc_choice


label wc_are_u_sure_2:
  "This choice will put you in a submissive position with Skyler."
  "Are you sure that's what you want?" 

  menu: 
    "Yeah. I want to give Skyler whatever she wants":
      jump weekend_cleaning_2
    "Um... nah, this doesn't feel right.":
      jump wc_choice


label weekend_cleaning_1:
  "anger wells within me." 
  
  max "What's in it for you? How about I let you keep your fucking job?"

  max "How about I don't throw your stupid, lazy ass out on the street? How would that be?"

  "The girl blinks petulantly, dropping her hand from her hip in an unconcious sign of defeat."

  max "How about I let you clean the place on Tuesday before we open instead of making you do it in a french maid's uniform on Friday night?"

  skyler "Ok! Fine whatever. Sorry [M]"

  "Danm... that felt..."
  "{i} GOOD {/i}"

  "Good. It's settled, stop pouting and get a mop and a bucket. I want that bar spotless by the time we open."

  skyler "Yes [M]"

  "Brought to heel. I swallow hard. My hands are shaking a little bit."

  max "Oh, and report here next Tuesday morning. Be ready to scrub this shithole top to bottom every week."

  skyler "... you're the boss"

  max "Good girl, now get the fuck out."

  hide skyler

  scene skyler_clean_1

  "I have to hand it to her, she got the place cleaned up pretty well. A few more weeks of this and we should see some additional profit"



label weekend_cleaning_2:
  max "*sigh* What do you want for it? I already give you all the booze you can drink."

  skyler "Say pretty please" 

  max "w- what?!"

  "I act incredulous, but I already know where this is headed. She'll start light, and a few weeks from now she'll have me on my knees between her legs."
  
  skyler "You heard me. Say Miss Skyler, pretty please help me clean up on Tuesdays."

  "..."

  "My cheeks go red as I formulate the words. I'd be lying if I said it didn't turn me on a little bit..."
  "or alot even"

  max "Pretty please Miss Skyler, help me clean up on Tuesdays."

  skyler "Ok. I'll help you clean. I'll be the supervisor, and you'll be the worker."

  max  "uh.."

  skyler "Now be a good worker, and take this mop and bucket, and get to work. I want this place spotless by the time we open."

  max  "Sky-"
  
  skyler "AH! You heard me. Get cleaning. We're gonna meet here every Tuesday morning from now on, and I'll make sure you do it right."

  "blood continues to flush my cheeks as I take the mop and follow Skyler into the bar" 

  scene max_clean_1

  "it's a long morning of cleaning, and I do all the work, while Skyler sits around and chats. But at least the bar gets pretty clean.  A few more weeks of this, and we should start seeing some additional profit."

