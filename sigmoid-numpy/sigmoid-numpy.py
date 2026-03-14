import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    s = np.asarray(x, dtype = float)
    ans = (1/(1+ np.exp(-s)))
    return ans