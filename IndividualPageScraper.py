def scrapePage(url: str, keepSymbols = False):
    import requests
    import bs4

    finalAnswers = {}

    # Tags with attributes that we want to filter out
    junkAttributes = [['mrow', {'class':'MJX-TeXAtom-ORD'}, 'Ionic Charges'], ['span', {'aria-label':'\\text'}, 'Different Format Ionic Charges'], ['msup', {'':''}, 'Superscripts'], ['msub', {'':''}, 'Subscripts'], ['sub', {'':''}, 'Differently Formatted Subscripts']]

    soup = bs4.BeautifulSoup(requests.get(url).text.encode('latin1').decode('utf-8'), features="lxml")

    # questionStems = soup.find_all('div', attrs={'data-type':'question-stem'})
    questionBoxes = soup.find_all('div', attrs={'class':'os-problem-container'})

    # print(type(questionBoxes))

    for box in questionBoxes:

        answerText = []

        if (box.find('img')):
            continue

        try:
            answers = box.find_all('div', attrs={'data-type':'answer-content'})
            question = box.find('div', attrs={'data-type':'question-stem'}).getText()
        except:
            continue
        # print("\n\n", box, "\n\n")

        for answer in answers:
            # Check if the answer choices have a list formatting
            answerChoice = ""
            print(answer.prettify())
            answerList = answer.find_all('li')
            print(answerList, "\n")
            # Seperating each item in the list with a comma
            if answerList:
                for item in answerList:
                    answerChoice += item.getText() + ", "
            # Removing the comma at the end
            answerChoice = answerChoice.strip(", ")

            hasJunk = False
            # Check if the answers have any junk
            if not keepSymbols:

                # Check if the answers have any subscripts
                # hasJunk = bool(answer.find('msup')) or bool(answer.find('sub'))

                for junk in junkAttributes:
                    if (hasJunk):
                        # print(answer.getText())
                        break
                    hasJunk = bool(answer.find(junk[0], attrs=junk[1]))

                if hasJunk:
                    break

                # Make sure the answer isn't a list
                if not answerList:
                    answerChoice = answer.getText().replace("\n", "")
            answerText.append(answerChoice)

        # print(hasJunk)
            
        # If keepSymbols is False and the answer choices contain ions, skip the question-answer pair
        if ((not keepSymbols) and hasJunk):
            # print("\n\nSKIPPED AN ANSWER:\n", "\n\n")
            continue

        finalAnswers[question.replace("\n", "")] = answerText
        
    return finalAnswers

questionAnswerPairs = scrapePage("https://openstax.org/books/biology-ap-courses/pages/10-test-prep-for-ap-r-courses")

for key in questionAnswerPairs.keys():
    print(key)
    print(questionAnswerPairs[key])
    # if not questionAnswerPairs[key]:
    #     print("\n", key)
print(len(questionAnswerPairs))