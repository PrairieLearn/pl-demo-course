import random

def generate(data):

    x = random.choice([0,1])
    y = random.choice([0,1])
    z = random.choice([0,1])

    data["params"]["x"] = x
    data["params"]["y"] = y
    data["params"]["z"] = z

    F = ((not y) and z) or x

    data["correct_answers"]["F"] = F

    # Create the link for the source code
    import os
    path_name = "https://github.com/PrairieLearn/pl-demo-course/tree/master/questions" + os.getcwd().split("questions",1)[1]
    data["params"]["path_name"] =  path_name
