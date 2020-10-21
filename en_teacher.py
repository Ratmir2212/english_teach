import random
from random import randint
def guess_word_by_sentence(word):
  XP = 0
  print("choose the correct option for this sentence: ", db_sentence[word])
  some_words = random.sample(list(db_sentence.keys()), 4)
  if word in some_words:
    print(some_words)
  else:
    some_words[randint(0, 3)] = word
    print(some_words)
  while True:
    answer = input(': ')
    if answer == word or answer == str(some_words.index(word) + 1):
      XP += 5
      print("Congratulation! You guessed right, you spent", str(XP), "tries")
      break
    else:
      print("Sorry, but you didn't guess right:( Try again")
  return XP
def load_db():
    path_db = "db_en_ru.txt"
    db = {}
    with open(path_db, "r") as f:
        k = f.read()
        c = k.split('\n')
    for i in c:
        kluch = i.split('-')[0]
        znach = i.split('-')[1]
        db[kluch] = znach
    return db
def write_score(name, point):
    """
    :param name: name player
    :param point: score
    :return: None
    """

    with open("file_of_scores", "r") as f:
        d = f.readlines()
    is_add = False
    for i in range(len(d)):
        if name in d[i]:
            new_point = int(d[i].split("-")[1]) + point
            d[i] = name + " - " + str(new_point) + "\n"
            is_add = True
            break

    if not is_add:
        text = name + " - " + str(point) + "\n"
        d.append(text)

    text = ""
    for line in d:
        text += line

    with open("file_of_scores", "w") as f:
        f.write(text)
def guess_word(word):
    max_XP = 10
    help_letters = []
    while True:
        print(word, "in rasian")
        answer = input("")
        if answer == db[word]:
            print("Excellent! You guessed right, you spend", str(10 - max_XP + 1), " try")
            return max_XP
        else:
            ran = randint(0, len(db[word])-1)
            if ran in help_letters:
                ran = randint(0, len(db[word])-1)
            help_letters.append(ran)
            print("Sorry, but you didn't guess right:( Try again")
            print(show_helps(help_letters, word))
            if max_XP > 0:
                max_XP -= 1
def write_score(name, point):
    """
    :param name: name player
    :param point: score
    :return: None
    """
    path = "file_of_scores"
    with open(path, "r") as f:
        d = f.readlines()
    is_add = False
    for i in range(len(d)):
        if name in d[i]:
            new_point = int(d[i].split("-")[1]) + point
            d[i] = name + " - " + str(new_point) + "\n"
            is_add = True
            break

    if not is_add:
        text = name + " - " + str(point) + "\n"
        d.append(text)

def show_helps(letters, word):
    show = []
    for i in range(len(db[word])):
        show.append('_ ')
    for x in letters:
        show[x] = db[word][x]
    show_letters = ""
    for i in show:
        show_letters += i
    return show_letters

if __name__ == "__main__":
    print("Hello! what's your name?")
    name = input(": ")
    db = load_db()
    tasks = random.sample(db.keys(), 5)
    XP = 0
    for word in tasks:
        XP += guess_word(word)

    print("Congratulations! You scored {} XP".format(XP))
    print(":)")
    write_score(name, XP)