from UnitScraper import scrapeUnits
from IndividualPageScraper import scrapePage
from IndPageScrapNewline import scrapeWithNewlines
import json

questionPages = ['Review Questions']
textbookQuestPages, unitNumbers = scrapeUnits(questionPages, 'https://openstax.org/books/concepts-biology/pages/1-review-questions', 'https://openstax.org/books/concepts-biology/pages/')

allQuestions = []

for i in range(len(textbookQuestPages)):
    
    # Getting the unit
    unit = unitNumbers[i]

    print(textbookQuestPages[i])
    # If scrapePage doesn't work, try using scrapeWithNewlines, some textbooks are wonky
    allQuestions.append([unit, scrapeWithNewlines(textbookQuestPages[i])])

with open("questionsAndAnswers.json", "w") as f:
    # this line of code is really sloppy, ToDo fix when free--Get uploadDataToSheets script to work for last unit instead of adding an extra unit
    allQuestions.append([9, {'':''}])
    json.dump(allQuestions, f)