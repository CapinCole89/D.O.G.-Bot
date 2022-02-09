from replit import db


sad_words = [
  "sad",
  "depressed",
  'unhappy',
  'miserable',
  'depressing',
  'trash',
  'garbage',
  'i suck',
  "lonely",
  ]

starter_encouragements = [
  'Cheer up!',
  "Just keep swimming!",
  "Sucking at something is just the first step to being sort of good at something!"
  ]

def create_encouragement(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]


def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) >= index:
    del encouragements[index]
    db["encouragements"] = encouragements


def create_haiku(haiku):
  if "haikus" in db.keys():
    haikus = db["haikus"]
    haikus.append(haiku)
    db["haikus"] = haikus
  else:
    db["haikus"] = [haiku]


def delete_haiku(index):
  haikus = db["haikus"]
  if len(haikus) >= index:
    del haikus[index]
    db["haikus"] = haikus