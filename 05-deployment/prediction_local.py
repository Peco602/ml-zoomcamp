import pickle

# Model and DictVectorizer loading
model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)

# Test data processing
client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}
X_test = dv.transform([client])

# Prediction
probability = model.predict_proba(X_test)[0, 1]

print(probability)