from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

import processText
import projectSecrets
import utilities
import streamlit as st
import webbrowser
import os


if __name__ == '__main__':
    if st.text_input("Password:", value="", type="password") == os.environ["APPPASS"]:
        st.markdown("""
                    # Handwritten todos to Things todos
                    """)

        uploaded_file = st.file_uploader(
            "First choose an image...", type="jpg")

        if uploaded_file is not None:
            # Authentication and Variable Creation
            subscription_key, endpoint = projectSecrets.keys()

            # Creating client interface with resource
            computervision_client = ComputerVisionClient(
                endpoint, CognitiveServicesCredentials(subscription_key))

            # Processing Image
            textList = processText.processImage(
                uploaded_file, computervision_client)
            results = utilities.sendToThings(textList)

            if st.button("Completed conversion. Click to upload."):
                for i in results:
                    st.text(i)
