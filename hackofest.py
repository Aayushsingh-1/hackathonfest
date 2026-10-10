


from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# 1. Initialize and train your model on startup
manual_rows = [
    ["USR101", 3, 15, 1, "Desktop", 3, "fashion"],  
    ["USR102", 0, 1, 0, "Mobile", 0, "watches"],  
    ["USR103", 6, 110, 3, "Mobile", 4, "phone"],  
    ["USR104", 5, 120, 1, "Desktop", 2, "fashion"],  
    ["USR105", 2, 8, 0, "Desktop", 1, "phones"],  
    ["USR106", 5, 100, 0, "Mobile", 0, "fashion"],  
    ["USR107", 4, 30, 2, "Mobile", 3, "watches"],
    ["USR108", 10, 19, 0, "Mobile", 0, "watches"],
    ["USR109", 12, 20, 0, "Desktop", 0, "Fashion"],
    ["USR110", 0, 2, 0, "Mobile", 0, "fashion"],     
    ["USR111", 1, 5, 1, "Desktop", 0, "watches"],    
    ["USR112", 0, 14, 0, "Mobile", 0, "phones"],
]
categories = [
    "User_ID", "Items_Added", "Minutes_Spent", 
    "Used_Discount", "Device_Type", "Made_Purchase", "Product_type"
]

df = pd.DataFrame(manual_rows, columns=categories)

X = pd.DataFrame()
X['conversion_rate'] = df['Made_Purchase'].div(df['Items_Added']).fillna(0)
X['items_abandoned'] = df['Items_Added'] - df['Made_Purchase']
X['time_spent_mins'] = df['Minutes_Spent']
X['discount_applied'] = df['Used_Discount']

def determine_if_person_stays(row):
    if row['Made_Purchase'] > 0:
        return 1
    elif row['Minutes_Spent'] >= 15 and row['Items_Added'] > 0:
        return 1
    else:
        return 0

df['will_stay'] = df.apply(determine_if_person_stays, axis=1)
Y = df['will_stay']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.25, random_state=42, stratify=Y
)
model = RandomForestClassifier(max_depth=None, class_weight="balanced", random_state=42)
model.fit(X_train, Y_train)

# 2. Define Routes
@app.route('/')
def home():
    # Renders your HTML frontend from the 'templates' folder
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    lookup_type = data.get("type")
    
    if lookup_type == "user_id":
        target_user = data.get("user_id").strip()
        user_index = df[df['User_ID'].str.upper() == target_user.upper()].index
        
        if len(user_index) > 0:
            specific_user_features = X.loc[user_index]
            prediction = model.predict(specific_user_features)[0]
            user_data = df.loc[user_index[0]].to_dict()
            return jsonify({
                "success": True, 
                "prediction": int(prediction),
                "user_data": user_data
            })
        else:
            return jsonify({"success": False, "error": "User ID not found in database records."})
            
    elif lookup_type == "custom":
        # Handle custom manual sliders/inputs from the frontend
        items = float(data.get("items_added", 0))
        minutes = float(data.get("minutes_spent", 0))
        discount = float(data.get("used_discount", 0))
        purchases = float(data.get("made_purchase", 0))
        
        conv_rate = purchases / items if items > 0 else 0.0
        abandoned = items - purchases
        
        custom_df = pd.DataFrame([{
            'conversion_rate': conv_rate,
            'items_abandoned': abandoned,
            'time_spent_mins': minutes,
            'discount_applied': discount
        }])
        
        prediction = model.predict(custom_df)[0]
        return jsonify({"success": True, "prediction": int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)








    





    

    


