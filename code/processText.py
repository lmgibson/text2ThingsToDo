from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials

import sys
import time
import projectSecrets
import utilities


def processImage(image, computervision_client):
    print("===== Batch Read - local =====")

    # Call API with image and raw response (allows you to get the operation location)
    recognize_handwriting_results = computervision_client.read_in_stream(
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


if __name__ == '__main__':

    # Authentication and Variable Creation
    subscription_key, endpoint = secrets.keys()

    # Creating client interface with resource
    computervision_client = ComputerVisionClient(
        endpoint, CognitiveServicesCredentials(subscription_key))

    # Evaluating Image
    local_image_path = sys.argv[1]
    textList = utilities.processImage(local_image_path, computervision_client)
    utilities.sendToThings(textList)
