
def boom(chapters, maxProbPerPage, problemsAmountForChapters):
	amountOfSpecialProblems = 0

	#print chapters
	#print maxProbPerPage
	#print problemsAmountForChapters

	pageIndex = 1
	for probAmount in problemsAmountForChapters:
		amountOfProblemsInCurrentPage = 0

		for currentProbInChapter in xrange(probAmount):

			
			amountOfProblemsInCurrentPage += 1

			if currentProbInChapter+1 == pageIndex:
				#print "page:",pageIndex,"problem:",currentProbInChapter+1,"chapter:",probAmount
				amountOfSpecialProblems += 1

			if amountOfProblemsInCurrentPage == maxProbPerPage:
				pageIndex += 1
				amountOfProblemsInCurrentPage = 0

		

	return amountOfSpecialProblems


chapters, maxProbPerPage = raw_input().split(" ")
problemsAmountForChapters = map(int, raw_input().split(" "))


#print boom(5, 3, [4,2,6,1,10])
print boom(chapters, maxProbPerPage, problemsAmountForChapters)