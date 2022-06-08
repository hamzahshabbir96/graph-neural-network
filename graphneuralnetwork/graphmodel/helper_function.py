import numpy as np
def leaky_relu_act(x):
       
        out = np.maximum(x,0.01*x)
        return out