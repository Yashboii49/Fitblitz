import pandas as pd
from sklearn.linear_model import LinearRegression
from .models import WorkoutSet

def predict_next_weight(user, exercise_id, target_reps=10):
    """
    Predicts the weight a user should lift for a specific exercise
    based on their historical progression.
    """
    # 1. Fetch historical data for this user and exercise
    sets = WorkoutSet.objects.filter(
        workout__user=user, 
        exercise_id=exercise_id
    ).order_by('workout__date')
    
    # We need a minimum amount of data to make a prediction
    if sets.count() < 3:
        return {"error": "Not enough data. Keep lifting for a few more sessions!"}

    # 2. Convert database records to a Pandas DataFrame
    df = pd.DataFrame(list(sets.values('workout__date', 'weight', 'reps')))
    
    # Create a feature indicating progression over time (Session 1, 2, 3...)
    df['session_num'] = range(1, len(df) + 1)

    # 3. Define Features (X) and Target (y)
    # We use the session number and the reps performed to predict the weight capacity
    X = df[['session_num', 'reps']]
    y = df['weight']

    # 4. Train a simple Linear Regression model
    model = LinearRegression()
    model.fit(X, y)

    # 5. Make the prediction for the NEXT session
    next_session_num = len(df) + 1
    
    # Predict the weight based on the user wanting to hit 'target_reps'
    predicted_weight = model.predict([[next_session_num, target_reps]])

    return {
        "exercise_id": exercise_id,
        "suggested_reps": target_reps,
        "suggested_weight": round(predicted_weight[0], 2) # Round to 2 decimal places
    }