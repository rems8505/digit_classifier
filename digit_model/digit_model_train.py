# digit_model/digit_model_train_model.py
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the digits dataset
digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

# Train a Logistic Regression model
#model = LogisticRegression(max_iter=10000)
#model.fit(X_train, y_train)

# Train a model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)


# Save the trained model to a file
#with open("digit_model/digits_model.pkl", "wb") as f:
#   pickle.dump(clf, f)


# Save the model
joblib.dump(clf, 'digit_model/digits_model.pkl')


# Evaluate
preds = clf.predict(X_test)


print("✅ Model trained and saved to 'digit_model/digits_model.pkl'")