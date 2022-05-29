import time

## this function will search on values not key because we want multiple items returned, and keys are unique but values are not
def SelectWordsFromDict(ChosenDict, ChosenLetter):
    SelectedWordsList=[]
    print("All the words in our dictionary beginning with ",ChosenLetter)
    for key, value in ChosenDict.items():
            if value == ChosenLetter:
                time.sleep(1)
                print(key)
                SelectedWordsList.append(key)
    return SelectedWordsList

AnimalDict = {'ant': 'a',
              'bee': 'b',
              'butterfly': 'b',
              'centipede': 'c', 'cockroach': 'c',
              'cricket': 'c', 'dragonfly': 'd', 'spider': 's',
              'scorpion': 's', 'flea': 'f', 'fly': 'f', 'grasshopper': 'g',
              'wasp': 'w', 'insect': 'i', 'ladybug': 'l', 'louse': 'l', 'millipede': 'm', 'mite': 'm', 'mosquito': 'm'}

SportDict= {'american football':'a', 'archery':'a', 'athletics':'a', 'badminton':'b', 'baseball':'b', 'basketball':'b',
              'bowls':'b', 'boxing':'b', 'canoeing':'c', 'cricket':'c', 'curling':'c', 'cycling':'c', 'darts':'d',
              'diving':'d', 'decathlon':'d', 'equestrian':'e', 'fencing':'f', 'football':'f', 'formula 1':'f',
              'gaelic games':'g', 'golf':'g', 'gymnastics':'g', 'handball':'h', 'hockey':'h',
              'horse racing':'h', 'ice hockey':'i', 'judo':'j', 'mixed martial arts':'m', 'pentathlon':'p',
              'motorsport':'m', 'netball':'n', 'rowing':'r', 'rugby league':'r', 'rugby union':'r',
              'sailing':'s', 'shooting':'s', 'snooker':'s', 'squash':'s', 'swimming':'s', 'table tennis':'t',
              'taekwondo':'t', 'tennis':'t', 'triathlon':'t', 'volleyball':'v', 'weightlifting':'w' }


FoodDict={'cabbage': 'c', 'carrot': 'c', 'cauliflower': 'c', 'corn': 'c',
          'eggplant': 'e', 'garlic': 'g', 'kale': 'k', 'lettuce': 'l', 'onion': 'o',
          'potato': 'p', 'pumpkin': 'p', 'radish': 'r', 'spinach': 's', 'taro': 't', 'tomato': 't', 'tuber': 't',
          'vegetable': 'v', 'apple': 'a', 'cantaloupe': 'c', 'cherry': 'c', 'grape': 'g', 'guava': 'g', 'lemon': 'l',
          'peach': 'p', 'raspberry': 'r', 'strawberry': 's', 'lime': 'l', 'orange': 'o',
          'pear': 'p', 'apricot': 'a', 'blueberry': 'b', 'cranberry': 'c', 'melon': 'm'}


TopicChoice=''
LetterChoice=''

while TopicChoice not in ('a','s','f'):
    print("What is you favorite topic  Animals (a)/Sports(s)/Food(f)?")
    TopicChoice=input("Please choose a/s/f : ")

print("What is you favorite letter? ")
LetterChoice=input()


if TopicChoice=='a':
    TopicDict=AnimalDict
elif TopicChoice=='s':
    TopicDict=SportDict
else:
    TopicDict=FoodDict

TopicList=SelectWordsFromDict(TopicDict,LetterChoice)

time.sleep(1)
print("Your short list is: ", TopicList)
