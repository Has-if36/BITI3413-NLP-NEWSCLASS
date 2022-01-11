import tensorflow as tf
from tensorflow import keras
import streamlit as st
from newspaper import Article
from nltk.corpus import stopwords
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.stem import WordNetLemmatizer
import pandas as pd
import numpy as np
import re
import os
import sys

# Modifiable Variables
# link = 'https://www.sciencedaily.com/releases/2021/12/211228135848.htm'
# top_n = 5

# Dictionary & Function Definition
inverse_label = {
    0: 'Business',
    1: 'Cars',
    2: 'Entertainment',
    3: 'Family',
    4: 'Health',
    5: 'Politics',
    6: 'Religion',
    7: 'Science',
    8: 'Sports',
    9: 'Technology',
    10: 'Travel'
}

stopword_list = stopwords.words('english')
tokenizer = ToktokTokenizer()


def remove_special_characters(text, remove_digits=False):
    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'
    text = re.sub(pattern, '', text)

    pattern = r'[~|!|@|#|$|%|^|*|(|)|_|+|-|=|?|<|>|,|.|:|;]'
    text = re.sub(pattern, '', text)

    pattern = r'[&]'
    text = re.sub(pattern, 'and', text)

    pattern = r'[/]'
    text = re.sub(pattern, 'or', text)

    return text


def remove_stopwords(text, is_lower_case=False):
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    if is_lower_case:
        filtered_tokens = [token for token in tokens if token not in stopword_list]
    else:
        filtered_tokens = [token for token in tokens if token.lower() not in stopword_list]
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text


def lemmatization(text):
    wordnet_lemmatizer = WordNetLemmatizer()
    tokens = tokenizer.tokenize(text)
    filtered_text = ''
    for token in tokens:
        filtered_text += wordnet_lemmatizer.lemmatize(token).lower() + ' '
    # tokens = [token.strip() for token in tokens]
    # filtered_text = ' '.join(filtered_tokens)
    return filtered_text


# Load Model
model = tf.keras.models.load_model('./model/news_genre_classification.h5')

# Webapp
st.title("News Genre Classification")
link = st.text_input("Insert Link Here:", "")

dropdown_n = st.selectbox("Top # Categories: ",
                          ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'], index=2)

if (st.button('Classify')):
    try:
        top_n = int(dropdown_n)
        result = link

        # Fetch Article
        article = Article(link)
        article.download()
        article.parse()

        articleText = article.text
        # Data Cleaning
        filtered_text = remove_special_characters(articleText, remove_digits=True)
        filtered_text = lemmatization(filtered_text)
        filtered_text = remove_stopwords(filtered_text)

        finalArticle = word = ""
        characterIndex = 0
        wordIndex = 0

        textArray = articleText.split(" ")
        for word in textArray:
            if characterIndex + len(word) < 70:
                finalArticle += word + " "
                characterIndex += len(word)
            else:
                finalArticle += "\n" + word + " "
                characterIndex = len(word)

        # Count Words
        word_column = 'words'  # Column for List of Words
        words = pd.read_csv('model/word_list_input.csv')
        words = words[word_column].to_numpy()
        freq = np.zeros(len(words), dtype=int)

        tokens = tokenizer.tokenize(filtered_text)
        freq = np.zeros(len(words), dtype=int)

        for word in tokens:
            for i, sel_word in enumerate(words):
                if word == sel_word:
                    freq[i] += 1

        # Prediction
        freq = np.reshape(freq, (1, 147))
        pred = model.predict(freq)

        # Get Output

        # max = None
        # for i, out in enumerate(pred):
        # max = np.amax(out)
        # max_index = np.argmax(out)
        # print(inverse_label[max_index], inverse_label[y_test[i]], max)
        # print('Genre:', inverse_label[max_index])
        # print('Confidence:', max)

        genrePrediction = ""
        top_pred = []
        for out in pred:
            # Sorts Predictions
            pred_sort = np.sort(out)[::-1]
            pred_sort_index = np.argsort(out)[::-1]

            # Initialise and Overwrite Top N
            for i in range(0, top_n):
                top_pred.append([pred_sort_index[i], pred_sort[i]])

            for i, each in enumerate(top_pred):
                genrePrediction += '#' + str(i + 1) + "\t: (" + str(round(each[1] * 100, 2)) + '%) \t' + inverse_label[
                    each[0]] + "\n"

        st.success('Operation Successfully Executed!')
        title_genre = 'Top ' + str(top_n) + ' Predicted Genre'
        st.header(title_genre)
        st.text(genrePrediction)
        st.text('')
        st.header('Article')
        st.text(finalArticle)
    except Exception as e:
        err = 'Failed to Execute:\n' + str(e)
        st.error(err)


