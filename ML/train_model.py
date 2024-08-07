import pandas as pd # type: ignore
from sklearn.model_selection import train_test_split # type: ignore

from sklearn.ensemble import RandomForestClassifier # type: ignore
from sklearn.preprocessing import StandardScaler # type: ignore
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score # type: ignore
import pickle
import io
import numpy as np # type: ignore


from google.colab import files # type: ignore


uploaded = files.upload()


import pandas as pd # type: ignore

data = pd.read_csv(io.BytesIO(uploaded['birth_data.csv']))

data.head()

# Map risk levels to binary target variable (e.g., 0 for 'low', 1 for 'medium' and 'high')
data['RiskLevel'] = data['RiskLevel'].map({'low': 0, 'medium': 1, 'high': 1})


from sklearn.preprocessing import LabelEncoder # type: ignore

# Create a LabelEncoder object
label_encoder = LabelEncoder()

# Fit the encoder to the 'RiskLevel' column and transform it
data['RiskLevel_Encoded'] = label_encoder.fit_transform(data['RiskLevel'])


# Define features and target variable
# Select specific columns for features
X = data[['Age', 'SystolicBP', 'DiastolicBP', 'BS', 'BodyTemp', 'HeartRate']]
# Now use the encoded column as your target variable
y = data['RiskLevel_Encoded']


# Split the data (using the new y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model (using the encoded y_train)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)


# Print evaluation metrics
print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')

# Save the model to a file
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print('Model training completed. Model saved as model.pkl')
