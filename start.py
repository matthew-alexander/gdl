"""
high level support for doing this and that.
"""

knob_weight = 0.5
input = 0.5

goal_prediction = 0.8 

step_amount = 0.001

for iteration in range(1102):
    prediction = input *knob_weight
    error = (prediction - goal_prediction) ** 2 

    print("Iteration: " + str(iteration) + " Error: " + str(error) + " Prediction: " + str(prediction))

    up_prediction = input * (knob_weight + step_amount)
    up_error = (goal_prediction - up_prediction) ** 2

    down_predicition = input * (knob_weight - step_amount)
    down_error = (goal_prediction - down_predicition) ** 2

    if(down_error< up_error):
        knob_weight = knob_weight - step_amount
    
    if(down_error > up_error):
        knob_weight = knob_weight + step_amount
