
import re

class ElementsMatcher:

	gemsCount = 0

	matchedElements = {}


	def addElementsFirst(self, elemList):
		for elm in elemList:
			self.matchedElements[elm] = 1


	def addElements(self, elemList):
		newMatchedElms = {}

	
		for elm in elemList:
			if elm in self.matchedElements:
				newMatchedElms[elm] = 1

		self.matchedElements = newMatchedElms


	def getSharedElements(self):
		return self.matchedElements


	def addGem(self, gemCode):
		if self.gemsCount == 0:
			self.addElementsFirst(gemCode)
		else:
			self.addElements(gemCode)

		self.gemsCount += 1
			


amountOfGems = int(raw_input())

matcher = ElementsMatcher()

for gem in xrange(amountOfGems):
	matcher.addGem(raw_input())

print len(matcher.getSharedElements())