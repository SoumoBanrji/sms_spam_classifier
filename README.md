# sms_spam_classifier

![spam_classifier_ui](https://user-images.githubusercontent.com/101920267/235896543-6bdee591-c254-44e8-b4c9-0a74c0f975a3.PNG)

![spam_classifier_ui1](https://user-images.githubusercontent.com/101920267/235896567-60a6bd76-5dce-4430-b772-13689175345e.PNG)

## Project Overview

This project aims to build a machine learning model that can predict whether a given SMS/Email is spam or not. The model is trained on the SMS Spam Collection Dataset available on Kaggle.

### The project involves:

* Exploring and visualizing the dataset
* Preprocessing and cleaning the text data
* Vectorizing the text data using TF-IDF Vectorizer
* developing classification models, evaluating each one's performance in terms of accuracy and precision scores
* Deploying the model using Streamlit

## Code Files

* data folder: Contains the dataset used in this project.
* saved_pkl folder: contains the saved pickle file of the trained model as model.pkl and TF-IDF Vectorizer as vectorizer.pkl
* sms-spam-detection.ipynb: Jupyter notebook with the code for data preprocessing, model training, and evaluation.
* app.py: Python script that deploys the model using Streamlit.


## Model Selection

We trained several models using different algorithms and hyperparameters, and evaluated each model using a validation set. The following table shows the accuracy and precision scores of each model:

![model_performence_info](https://user-images.githubusercontent.com/101920267/235911051-1801de8a-5f62-416d-9e22-e366ca7799ae.PNG)

According to these data, the model with the best accuracy the best accuracy, according to these data, is SVC, with an accuracy of 0.975822, while the model with the highest precision, according to these results, is NB, with a precision of 1.000000 and a high accuracy score of 0.970986. Nb is the MultinomialNB algorithm I picked for my project based on this.

Here is the confusion matrix of this model

![confusion_matrix](https://user-images.githubusercontent.com/101920267/235913540-5f9b99c9-e29a-42f3-a2b8-56d74e567f5d.PNG)

## Conclusion

This project shows how to classify texts using machine learning models. The deployed model could potentially be used to determine whether or not an SMS or email is spam.


