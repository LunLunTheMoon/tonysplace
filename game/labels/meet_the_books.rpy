label meet_the_books:
  scene bg_books
  max "Sigh.."

  "After looking through the books for a few hours, I remain mystified, but I've been in business school long enough to know that the place is in real trouble."
  "I expected maybe two ledger books.. one for Tony's above-the-table dealings and another for.. well the more creative side of the business.."
  "...But there are five ledgers in total, all overlapping like venn-diagrams of illicit undertakings, and they're all in the red"
  "I expected a leech or two, but as far as I can tell, our entire weekly income is being entirely consumed by a horde of bookies and loan sharks."
  "What's worse, Tony appears to have leveraged the place to pay for his gambling debts, but not to a bank.. rather to someone or something that's only identified as '{i}J{/i}'."
  "The way everything is spread out, with Uncle Tony's crazy accounting system, I can't even really tell how much we owe, or to whom. And whoever this J person is, I can't tell how he's being paid his vig."

  show skyler at right
  skyler "Hey bosslady. Can you help me? This guy wants some top-shelf whisky, but I don't have the key to the cabinet."
  max "sigh. Sure I'll be right there"

  $disable_interaction("meetTheBooks")
  $GAME.end_turn()
