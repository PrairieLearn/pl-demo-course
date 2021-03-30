def generate(data):
    data["params"]["names_from_user"] = [
        {"name": "power_iteration", "description": r"function that performs power iteration", "type": r"function"},
        {"name": "G", "description": r"markov matrix G", "type": r"2d numpy array"},
        {"name": "xstar2", "description": r"probability of winning and losing", "type": r"1d numpy array"},
        {"name": "M2", "description": r"markov matrix M2", "type": r"2d numpy array"},
        {"name": "M3", "description": r"markov matrix M3", "type": r"2d numpy array"}
    ]
    data["params"]["names_for_user"] = [
    ]
