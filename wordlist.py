import sys
class Wordlist:
	def __init__(self):
		self.words = self.getWordsFromiSpell()

	def getWordsFromiSpell(self):
		""" Store word list from iSpell in this object """

		word_list = []
		with open("ispell/english.0") as f:
			word_list = (f.readlines())
		return word_list