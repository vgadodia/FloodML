import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("final_data.csv")
y = data['class']
X = data.drop('class', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)

classifier = RandomForestClassifier(n_estimators = 50, criterion = 'entropy', random_state = 0)

classifier.fit(X_train, y_train)

pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, pred)

print("accuracy: " + str(accuracy * 100) + "%")

pickle.dump(classifier, open('model.pickle', 'wb'))