from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials

import os
import projectSecrets
import utilities
import streamlit as st
from PIL import Image

if __name__ == '__main__':
    st.markdown("""
                # Paper todo to Things3
                """)
    uploaded_file = st.file_uploader("First choose an image...", type="jpg")

    if uploaded_file is not None:
        # Authentication and Variable Creation
        subscription_key, endpoint = projectSecrets.keys()

        # Creating client interface with resource
        computervision_client = ComputerVisionClient(
            endpoint, CognitiveServicesCredentials(subscription_key))

        # Prepping Image
        image = Image.open(uploaded_file)
        st.text(type(image))

        # Evaluating Image
        textList = utilities.processImage(image, computervision_client)
        results = utilities.sendToThings(textList)

        for i in results:
            st.text(i)
