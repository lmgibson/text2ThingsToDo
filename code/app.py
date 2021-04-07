from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

import processText
import projectSecrets
import utilities
import streamlit as st
import os


if __name__ == '__main__':
    if st.text_input("Password:", value="", type="password") == os.environ["APPPASS"]:
        st.markdown("""
                    # Handwritten todos to Things todos
                    """)

        uploaded_file = st.file_uploader(
            "Upload an image (png or jpg)", type=['png', 'jpg'])

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

            st.text(
                "Copy paste the links below into a browser to upload the todos to things.")
            for i in results:
                st.text(i)
