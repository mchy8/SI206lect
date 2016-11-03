# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns DOWN
# 3) Replace nouns 15% of the time, everything else 10% DONE

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")

# code developed by Jackie Cohen; revised by Paul Resnick
# further revised by Colleen van Lent for Python3
#sfsgf
import nltk # requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
import random
from nltk.book import *
from nltk.corpus import gutenberg
from nltk import word_tokenize,sent_tokenize

tagged_tokens = nltk.pos_tag(text2)


tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "RB":"an adverb"}
substitution_probabilities = {"NN":.5,"NNS":.5,"VB":.1,"JJ":.1,"RB":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []
x =tagged_tokens[:150]

for (word, tag) in tagged_tokens[:150]:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))


def spacing(listy):
	lst2 = []
	for words in listy:
		if words in [",","?",".","!",":"]:
			lst2.append(words)
		else:
			lst2.append(" "+ words)
	print("".join(lst2))

og =[]
print("\n")
print("ORIGINAL TEXT")
b = tagged_tokens[:150]
for thing in b:
	og.append(thing[0])
og1 = spacing(og)
#print(type(og1))

print("\n")
print("NEW TEXT")
print("\n")
print("".join(final_words))



print("\n\nEND*******")
