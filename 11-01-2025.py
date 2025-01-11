#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.tokenize import PunktSentenceTokenizer
#creating the instance
tokenizer = PunktSentenceTokenizer()
#test for split
input_string = "This is an example sent.The sentence"
all_sentences = tokenizer.tokenize(input_string)
print(all_sentences)


# In[2]:


import re
text="Hello, World ! 123"
text=re.sub(r'[^a-z\s]','',text)
print(text)


# In[4]:


import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Sample data
data = [
    ['spam', 'Had your mobile 11 months or more? U R entitled to Update to the latest model now!'],
    ['ham', 'Hey, are you coming to the party tonight?'],
    ['spam', 'Congratulations! You have won a $1000 gift card. Click here to claim your prize.'],
    ['ham', 'Can you send me the document by tomorrow?'],
    ['spam', 'Exclusive offer: Get 50% off on your next purchase. Limited time only.'],
    ['ham', 'Let’s catch up over lunch sometime this week.']
]

labels = [row[0] for row in data]
messages = [row[1] for row in data]

def preprocess_text(text):
    """Preprocess the text by:
    - Lowercasing
    - Removing the characters and numbers
    - Tokenizing
    - Removing stopwords
    """
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    words = text.split()
    from nltk.corpus import stopwords
    import nltk
    nltk.download('stopwords')
    stop_words = set(stopwords. words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)
preprocessed_messages = [preprocess_text(msg) for msg in messages]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(preprocessed_messages)
y = labels

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:", classification_report(y_test, y_pred))
new_sms = "Congratulations! You've won 2 free tickets to xyz, Call now to claim!"
new_sms_preprocessed = preprocess_text(new_sms)
new_sms_vectorized = vectorizer.transform([new_sms_preprocessed])
prediction = model.predict(new_sms_vectorized)

print(f"Prediction for new SMS: {prediction[0]}")


# In[ ]:




