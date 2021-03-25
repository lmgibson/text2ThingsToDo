from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials

import sys
import re
import time
import webbrowser
import urllib
import secrets
import utilities


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
