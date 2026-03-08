import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from taipy.gui import Gui

# Example training dataset
data = pd.DataFrame({
    "amount":[50,2000,15,5000,100,3000,20,7000],
    "time":[10,23,14,2,16,1,11,3],
    "location_change":[0,1,0,1,0,1,0,1],
    "fraud":[0,1,0,1,0,1,0,1]
})

X = data[["amount","time","location_change"]]
y = data["fraud"]

# Train model
model = RandomForestClassifier()
model.fit(X,y)

amount = 0
time = 0
location_change = 0
result = ""

def detect(state):
    prediction = model.predict([[state.amount,state.time,state.location_change]])
    
    if prediction[0] == 1:
        state.result = "⚠ Potential Fraud Transaction"
    else:
        state.result = "✓ Legitimate Transaction"

page = """
# Credit Card Fraud Detection System

Enter Transaction Details

Amount:
<|{amount}|input|type=number|>

Transaction Hour (0-23):
<|{time}|input|type=number|>

Location Change (0 = No, 1 = Yes):
<|{location_change}|input|type=number|>

<|Detect Fraud|button|on_action=detect|>

## Result
<|{result}|text|>
"""

Gui(page).run()