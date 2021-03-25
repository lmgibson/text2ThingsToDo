from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
import re
import time
import webbrowser
import urllib


def processImage(image, computervision_client):
    print("===== Batch Read - local =====")
    # Open local image file
    # local_image_handwritten = open(image, "rb")

    # Call API with image and raw response (allows you to get the operation location)
    recognize_handwriting_results = computervision_client.read(
        image, raw=True)

    # Get the operation location (URL with ID as last appendage)
    operation_location_local = recognize_handwriting_results.headers["Operation-Location"]
    # Take the ID off and use to get results
    operation_id_local = operation_location_local.split("/")[-1]

    # Call the "GET" API and wait for the retrieval of the results
    while True:
        recognize_handwriting_result = computervision_client.get_read_result(
            operation_id_local)
        if recognize_handwriting_result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    # Print results, line by line into a dictionary
    results = []
    if recognize_handwriting_result.status == OperationStatusCodes.succeeded:
        for text_result in recognize_handwriting_result.analyze_result.read_results:
            for line in text_result.lines:
                results.append(line.text)

    return results


def createThingsURL(parseDict):
    # Extracting elements
    htmls = []
    for idx, ToDo in enumerate(parseDict):
        for i in ToDo:
            ToDo[i] = urllib.parse.quote_plus(ToDo[i])
        html = "things:///add?" + urllib.parse.urlencode(ToDo)
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
    # Send to things
    # for i in htmls:
    # webbrowser.open(i)
