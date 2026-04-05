import pandas as pd

# STEP 1: load dataset properly
df = pd.read_csv("UNSW-NB15_1.csv", header=None)

# STEP 2: assign proper column names
df.columns = [f"feature_{i}" for i in range(df.shape[1])]

# STEP 3: drop IP columns
df = df.drop(columns=["feature_0", "feature_2"])

# STEP 4: convert to numeric
df = df.apply(pd.to_numeric, errors='coerce')

# STEP 5: fill missing values
df = df.fillna(0)

# STEP 6: split features and target
target_column = df.columns[-1]

X = df.drop(columns=[target_column])
y = df[target_column]

print("Feature shape:", X.shape)
print("Target shape:", y.shape)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# split into train & test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# create model
model = RandomForestClassifier(class_weight='balanced')

# train model
model.fit(X_train, y_train)

# predict
y_pred = model.predict(X_test)

# accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClass distribution:")
print(y.value_counts())
from sklearn.metrics import classification_report, confusion_matrix

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
import pandas as pd

importance = model.feature_importances_
feature_names = X.columns

imp_df = pd.DataFrame({
    'feature': feature_names,
    'importance': importance
}).sort_values(by='importance', ascending=False)

print("\nTop 10 Important Features:")
print(imp_df.head(10))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
from sklearn.metrics import roc_auc_score

y_prob = model.predict_proba(X_test)[:, 1]
print("ROC-AUC:", roc_auc_score(y_test, y_prob))