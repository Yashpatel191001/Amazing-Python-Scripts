# Text Emotion Detection

For detecting emotions from the text, I will perform a few steps that will start with preparing the data. Then the next step will be tokenization where the textual data will be converted into tokens and from these tokens, we have to identify the emotional words.

These emotional words will be the keyword to classify the emotions of a text. Next, we’ll frame this task in such a way that a text will be taken as an input and the emoji that represents the emotions in that text is generated as the output.

## Getting Started

To get started, follow the instructions below.

## Prerequisites

Make sure you have the following libraries installed:

- re
- collections
- sklearn
- pandas

## Installation

Clone the repository:
```shell
git clone https://github.com/viv3k19/textEmotion_Detection-using-Python-ML.git
```

## Usage

1. Open the `textEmotion_Detection.ipynb` notebook.
2. Run the cells in the notebook to train the machine learning models and detect emotions in text.

## Dataset

The dataset used for this task is stored in the file `text.txt`. It consists of labeled text instances with corresponding emotions.

## Functions

The following functions are defined in the code:

### `read_data(file)`

This function reads the data from the specified file and returns it as a list.

### `ngram(token, n)`

This function generates n-grams from a given token.

### `create_feature(text, nrange=(1, 1))`

This function creates features from the input text using n-grams.

### `convert_label(item, name)`

This function converts the label into a human-readable format based on the specified names.

### `train_test(clf, X_train, X_test, y_train, y_test)`

This function trains and tests a classifier using the provided data.

## Machine Learning Models

The following machine learning models are used for emotion detection:

- Support Vector Machine (SVC)
- Linear Support Vector Classifier (LinearSVC)
- Random Forest Classifier
- Decision Tree Classifier

The training and test accuracies for each classifier are printed in the notebook.

## Detecting Emotion

The notebook demonstrates how to assign emojis to each emotion label and use the trained model to detect emotions in input sentences.

## Example Sentences

The following sentences are provided as examples:

1. "This looks so bad"
2. "I have a fear of nightmares"
3. "My dog died yesterday"
4. "I don't love you anymore..!"

The corresponding predicted emotions are displayed using emojis.

## Screenshots

* Accuracy & Test Results

![accuracyNTestResults](https://github.com/viv3k19/textEmotion_Detection-using-Python-ML/assets/82309435/24746431-5579-4020-819b-2fbea15d2e7f)

* Analytics

![analysis](https://github.com/viv3k19/textEmotion_Detection-using-Python-ML/assets/82309435/74f6a60e-dbd6-4cc9-a86f-6ae88197a323)

* Output

![output](https://github.com/viv3k19/textEmotion_Detection-using-Python-ML/assets/82309435/06e56e68-b536-4ab9-b3f6-4395c8c3ff3b)

# Project Creator
* Vivek Malam - Feel free to contact me at viv3k.19@gmail.com for any questions or feedback.

