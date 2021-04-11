import random, math

def generate(data):

    a = random.randint(100, 200)
    ans = "{0:b}".format(a)
    data["params"]["a"] = a
    data["correct_answers"]["b"] = ans

    # Create the link for the source code
    import os
    path_name = "https://github.com/PrairieLearn/pl-demo-course/tree/master/questions" + os.getcwd().split("questions",1)[1]
    data["params"]["path_name"] =  path_name

    return data
