import string
import nltk
# from textblob import TextBlob
# nltk.download('brown')
review = input("Please enter a review: \n")
lex_file = open("Lexicons/attribute_lexicon.txt")
lex_lines = lex_file.read()
lex_words = lex_lines.strip().split(",")
for i in range(len(lex_words)):
    lex_words[i] = lex_words[i].strip()
words_in_review = review.split(" ")
# blob = TextBlob(review)
# print(blob.noun_phrases)
food_words = []
f_words = open("Lexicons/food_list.txt")
words_line = f_words.read()
words = words_line.strip().split("\n")
for i in range(len(words)):
    words[i] = words[i].lower()

for i in range(len(words_in_review)):
    # words_in_review[i] = words_in_review[i].lower().strip(".").strip(",").strip("!").strip()
    words_in_review[i] = "".join((char for char in words_in_review[i] if char not in string.punctuation))
for i in range(len(words_in_review)):
    words_in_review[i] = words_in_review[i].replace(u'\xa0','')
for f in words_in_review:
    if f.lower().strip(".").strip() in words:
        food_words.append(f)
attributes = []
if len(food_words) > 0:attributes.append("food")
for word in lex_words:
    if word.lower() in words_in_review:
        attributes.append(word)
print (attributes)