# test id - 23280666631255
import collections
import functools

def getCompanyMentions(companiesDict, review):
    foundCompanies = {}
    for word in review.split():
        if word in companiesDict:
            foundCompanies[word] = True
    return foundCompanies

def getCompaniesArr(mentionsCounts):
    arr = []
    for key in mentionsCounts:
        arr.append({
            "name": key,
            "score": mentionsCounts[key],
        })
    return arr

def sortByName(item1, item2):
    if item1["name"] < item2["name"]:
        return -1
    elif item1["name"] > item2["name"]:
        return 1
    else:
        return 0

def sortByScoreAndName(item1, item2):
    if item1["score"] < item2["score"]:
        return -1
    elif item1["score"] > item2["score"]:
        return 1
    else:
        return sortByName(item1, item2)

def getCompaniesNames(companiesObjs):
    def extractName(c):
        return c["name"]
    return list(map(extractName, companiesObjs))

def topNCompetitors(numCompetitors, topNCompetitors, competitors, numReviews, reviews):
    mentionsCounts = {}
    for competitor in competitors:
        mentionsCounts[competitor] = 0

    for review in reviews:
        mentionedCompanies = getCompanyMentions(mentionsCounts, review)
        for mentionedCompany in mentionedCompanies:
            mentionsCounts[mentionedCompany] += 1
    
    companiesArr = getCompaniesArr(mentionsCounts)
    companiesArrSorted = sorted(companiesArr, key=functools.cmp_to_key(sortByScoreAndName), reverse=True)
    print(companiesArrSorted)
    
    onlyNames = getCompaniesNames(companiesArrSorted)
    return onlyNames[0:topnCompetitors]
    

numCompetitors = 6
topnCompetitors = 2
competitors = ['newshop', 'shopnow', 'afshion', 'fashionbeats']
numReviews = 1
reviews = [
    'hey newshop here newshop fashionbeats'
]
res = topNCompetitors(numCompetitors, topnCompetitors, competitors, numReviews, reviews)
print(res)
