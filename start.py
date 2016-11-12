"""
high level support for doing this and that.
"""

knob_weight = 0.5
input = 0.5

goal_prediction = 0.8 

step_amount = 0.001

for iteration in range(50):
    prediction = input *knob_weight
    # error = (goal_prediction-prediction) ** 2 
    error = (goal_prediction - (input * knob_weight)) ** 2

    direction_and_amount = (goal_prediction - prediction) * input

    knob_weight = knob_weight + direction_and_amount

    print("Iteration: " + str(iteration) + " Error: " + str(error) + " Prediction: " + str(prediction))

  