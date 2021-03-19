# Overview

Do you like to take handwritten notes as the day progress of things to do or task assignments during meetings? text2ThingsToDo will help you convert those todos from handwritten text and into a Things todo item. It works at the command line by taking an image file as an input, extracting to-dos and adding them to your Things ToDo inbox. For best results, it is recommended to format hand written todos as such:

```
ToThings: 3-18-21
    1. Write comparision with prior report
    2. Copy over results
        - Try using image2Text to convert png tables
        to CSV?
    3. Call team lead for timeline update
```

The program will parse notes of the above format and add them to your Things3 todo list app inbox.

# How to Use

To use the program you will need to spin up a free-tier Azure Cognitive Services Computer Vision resource. Currently, you can use the program at the command line. Download the code contained in src and simply run:

```
python src/processText.py '/path/to/your/imageFile'
```
