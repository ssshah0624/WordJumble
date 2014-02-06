import sys
import itertools
from wordlist import Wordlist

word_list = Wordlist()

def unjumble(jumbled_word):
	""" Compare all words within a downloaded word list 
	to jumbled word """

	word = list(jumbled_word)
	wordList = []
	for x in word_list.words:
		ref_word = removeTags(x)
		if len(ref_word) <= len(word):
			if isSubset(list(ref_word),word):
				wordList.append(ref_word)
	print wordList

def removeTags(word):
	""" Remove end tags for each word list word 
	for consistency & comparability """

	temp = list(word)
	temp.remove('\r')
	temp.remove('\n')
	return ''.join(temp)

def isSubset(dictionaryWord, jumbledWord):
	""" Return True if dictionaryWord is a 
	subset of jumbledWord based on character matching and
	character frequency """

	for character in dictionaryWord:
		if character not in jumbledWord:
			return False
		if frequency(character, dictionaryWord) > frequency(character, jumbledWord):
			return False
	return True

def frequency(character, word):
	""" Return frequency of character in word """

	freq = 0
	for x in list(word):
		if x == character:
			freq+=1
	return freq

#Main method
if __name__ == "__main__":
	if(len(sys.argv) != 2):
		print("Invalid input!")
		sys.exit()

	jumbled_word = sys.argv[1]
	unjumble(jumbled_word)




