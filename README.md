## **Project Description:**
This project involves the development of a machine learning model capable of recognizing human emotions from images. The model is integrated into an application using Streamlit, which provides an interactive user interface for real-time emotion detection.

## **Problem Statement:**
Emotion recognition is a challenging aspect of computer vision and artificial intelligence, with significant implications in various fields such as psychology, marketing, and human-computer interaction. The goal is to create an automated system that accurately identifies human emotions from facial expressions in images.

## **Project Methodology:**
- A convolutional neural network (CNN) model was trained on a dataset of facial expressions to classify emotions.
- The model was saved and loaded into the Streamlit app.
- The app accepts an image path input from the user, processes the image, and uses the model to predict the emotion.
- The predicted emotion is displayed to the user along with the input image.

## **Contributions:**
- Development of a robust emotion classification model.
- Creation of an accessible application for non-technical users to leverage AI for emotion recognition.
- Provision of a tool that can be used for psychological analysis or enhancing user experience in various digital platforms.

## **Deployment Process:**
The model was deployed within a Streamlit application, which was set up to:
- Allow users to input an image path.
- Process and predict the emotion from the image using the pre-trained model.
- Display both the result and the image within the app interface.

## **Impact and Practical Applications:**
The project has potential applications in:
- Enhancing user experience by adapting responses or content based on detected emotions.
- Assisting psychologists in analyzing patients' emotional states.
- Providing insights for market researchers on consumer reactions to products or advertisements.

## **Conclusion:**
The human emotion recognition project successfully demonstrates how AI can be utilized to interpret complex human expressions. The integration of this technology into a user-friendly application paves the way for numerous practical applications that can benefit various sectors by providing deeper emotional insights.

I hope this description serves your needs well. If you require further details or adjustments, please let me know!



## **System Demo:**

![The System Demo](https://github.com/Mutiu123/human-emotion-recognition/blob/main/demo/demo1.png)



## **To run the model**
1. **Clone the Repository**:
   - First, clone the repository containing the heart disease prediction system code to your local machine. You can do this using Git or by downloading the ZIP file from the repository.


2. **Run the Streamlit App**:
   - In the same terminal or command prompt, execute the following command to run the Streamlit app:
     ```
     streamlet run app.py
     ```
   - This will start the local development server, and you'll see a message indicating that the app is running.
   - Open your web browser and visit `http://localhost:8501` (or the URL provided in the terminal) to access the interactive web app.

3. **Predict Heart Disease**:
   - On the Streamlit app, enter the message of your choice.
   - After entering the message, click the “validate” button.
