import re
from urllib import parse


def createThingsURL(parseDict):
    # Extracting elements
    htmls = []
    for idx, ToDo in enumerate(parseDict):
        html = "things:///add?" + parse.urlencode(ToDo, quote_via=parse.quote)
        htmls.append(html)

    return htmls


def findStartOfNotes(textList):
    notesStart = None
    for idx, i in enumerate(textList):
        if i.lower().replace(" ", "").startswith('tothings'):
            notesStart = idx
        else:
            pass
    return notesStart


def sendToThings(textList):
    # Find start of notes
    notesStart = findStartOfNotes(textList)

    # Parse notes
    parseDict = []
    i = 0
    j = -1

    for i in range(0, len(textList)):
        if re.search('^[0-9]', textList[i].lower().replace(" ", "")):
            parseDict.append({'title': textList[i]})
            j += 1
        elif re.search('^\-', textList[i]):
            parseDict[j]['checklist-items'] = textList[i]
        else:
            pass

    # Create URLs
    htmls = createThingsURL(parseDict)
    return htmls
