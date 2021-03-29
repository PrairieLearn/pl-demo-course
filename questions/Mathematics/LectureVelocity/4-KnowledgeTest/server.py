import random
import numpy as np
import matplotlib.pyplot as plt
import io
import matplotlib as ml
ml.rcParams['text.usetex'] = True
plt.rcParams.update({'font.size': 14})

def create_dict_xy_coord(p):
    return '{"x": ' + str(p[0]) + ',"y": ' + str(p[1]) + '}'

def f(x,a,b,c):
    return -a*x**2 + b*x + c

def df(x,a,b):
    return -2*a*x + b


def generate(data):

    # equation coefficients
    a = random.choice([9,10,11,12])
    b = random.choice([10,11,12,13])
    c = random.randint(28,35)
    data["params"]["a"] = a
    data["params"]["b"] = b
    data["params"]["c"] = c

    # interval and given points
    t0 = random.choice([0.125,0.25,0.375,0.5])
    t1 = random.choice([1.125,1.25,1.375,1.5,1.625,1.75])
    t2 = random.choice([0.625,0.75,0.875,1.0])
    data["params"]["t0"] = t0
    data["params"]["t1"] = t1
    data["params"]["t2"] = t2
    # corresponding function values
    ft0 = round(f(t0,a,b,c),1)
    ft1 = round(f(t1,a,b,c),1)
    data["params"]["ft0"] = ft0
    data["params"]["ft1"] = ft1

    # find slope of secant
    data["correct_answers"]["va"] = (ft1-ft0) / (t1-t0)
    # find tangent slope
    data["correct_answers"]["vi"] = df(t2,a,b)

    # origin
    V0 = [60,345]
    data["params"]["V_origin"] = create_dict_xy_coord(V0)
    p0 = [200*t0, 10*(ft0-10)]
    p1 = [200*t1, 10*(ft1-10)]
    data["params"]["line"] = '[' + create_dict_xy_coord(p0) + ',' + create_dict_xy_coord(p1) + ']'

    # checkbox
    sign = random.choice(["positive", "negative"])
    data["params"]["sign"] = sign
    tmax = b/(2*a)
    points = np.arange(0.125, 2.1, 0.125)
    dic = []
    if sign == "positive":
        tag1 = 'false'
        tag2 = 'true'
    else:
        tag1 = 'true'
        tag2 = 'false'

    for i,p in enumerate(points):
        if p > 1.3*tmax:
            dic.append({'tag': tag1, 'ans': str(p)})
        elif p < 0.7*tmax:
            dic.append({'tag': tag2, 'ans': str(p)})

    data['params']['t_options'] = dic

## The function 'file(data)' is used to generate the figure dynamically,
## given data defined in the 'generate' function
def file(data):

    if data['filename']=='figure1.png':
        #clear
        a0 = 0
        b0 = 2
        x = np.linspace(a0, b0)
        a = data['params']['a']
        b = data['params']['b']
        c = data['params']['c']

        fig = plt.figure()
        ax = fig.add_subplot(111)

        major_ticks = np.arange(0, 2.1, 0.25)
        minor_ticks = np.arange(0, 2.1, 0.125)
        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)

        plt.plot(x,f(x,a,b,c),linewidth=3.0)
        plt.xlim(a0,b0)
        plt.ylim(10,40)
        plt.xlabel(r"$t$", fontsize=20)
        plt.ylabel(r"$s(t)$", fontsize=20)


    # Save the figure and return it as a buffer
    buf = io.BytesIO()
    plt.savefig(buf,format='png',transparent=True)
    return buf
