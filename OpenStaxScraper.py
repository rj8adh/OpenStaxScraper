from UnitScraper import scrapeUnits
from IndividualPageScraper import scrapePage
from IndPageScrapNewline import scrapeWithNewlines

textbookQuestPages = scrapeUnits(['Review Questions', 'Critical Thinking Questions', 'Test Prep for APÂ® Courses'], 'https://openstax.org/books/biology-ap-courses/pages/2-review-questions', 'https://openstax.org/books/biology-ap-courses/pages/')

allQuestions = []

for i in range(len(textbookQuestPages)):
    print(textbookQuestPages[i])
    allQuestions.append(scrapePage(textbookQuestPages[i]))

for pageQuestions in allQuestions:
    print(pageQuestions)