from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle
import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from numpy import mean

MODEL_PATH = "models"

import os
if not os.path.exists(MODEL_PATH):
    os.makedirs(MODEL_PATH)

test_percent = 0.2
text = []
label = []
# Load data
for line in open('./data/new_data.txt'):
    words = line.strip().split()
    label.append(words[0])
    text.append(' '.join(words[1:]))

# Input train, Input text, output train, output test
X_train, X_test, y_train, y_test = train_test_split(text, label, test_size=test_percent, random_state=42)

# Save train text
with open('./data/train.txt', 'w') as fp:
    for x, y in zip(X_train, y_train):
        fp.write('{} {}\n'.format(y, x))

# Save test text
with open('./data/test.txt', 'w') as fp:
    for x, y in zip(X_test, y_test):
        fp.write('{} {}\n'.format(y, x))

# encode label
label_encoder = LabelEncoder()
label_encoder.fit(y_train)
print(list(label_encoder.classes_), '\n')
y_train = label_encoder.transform(y_train)
y_test = label_encoder.transform(y_test)

# print(X_train[0], y_train[0], '\n')
# print(X_test[0], y_test[0])

start_time = time.time()

text_clf = Pipeline([('vect', CountVectorizer(ngram_range=(1,1),
                                             max_df=0.8,
                                             max_features=None)), 
                     ('tfidf', TfidfTransformer()),
                     ('clf', LogisticRegression(solver='lbfgs', 
                                                multi_class='auto',
                                                max_iter=10000))
                    ])

# Train
print("Starting train")
text_clf = text_clf.fit(X_train, y_train)
train_time = time.time() - start_time
print('Done training in', train_time, 'seconds.')
# Save model
pickle.dump(text_clf, open(os.path.join(MODEL_PATH, "model.pkl"), 'wb'))

model = pickle.load(open(os.path.join(MODEL_PATH,"model.pkl"), 'rb'))
y_pred = model.predict(X_test)
print('Accuracy =', mean(y_pred == y_test))