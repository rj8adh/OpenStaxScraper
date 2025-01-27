def scrapePage(url: str):
    import requests
    import bs4

    finalAnswers = {}

    soup = bs4.BeautifulSoup(requests.get(url).text, features="lxml")

    # questionStems = soup.find_all('div', attrs={'data-type':'question-stem'})
    questionBoxes = soup.find_all('div', attrs={'class':'os-problem-container'})

    # print(type(questionBoxes))

    for box in questionBoxes:
        # Feeding the box html to bs4 so we can parse it(the encoding and decoding is to turn wonky html text to normal text)
        boxSoup = bs4.BeautifulSoup(box.text.encode('latin1').decode('utf-8'), features="lxml")


        # Getting the questionbox text
        questionBoxData = boxSoup.find('p').getText()
        
        # Getting answer choices and question from question box data
        answerChoiceList = questionBoxData.split("\n\n\n")
        question = answerChoiceList.pop(0)

        # Filters all empty items and newlines in the list out
        answerChoiceList = [x for x in answerChoiceList if x]
        answerChoiceList = [item.replace("\n", "") for item in answerChoiceList]

        finalAnswers[question] = answerChoiceList
        # print(question)
        # print(answerChoiceList)
    # print(finalAnswers)
    return finalAnswers

print(scrapePage("https://openstax.org/books/biology-ap-courses/pages/2-critical-thinking-questions"))
