import matplotlib.pyplot as plt 
fig, axs = plt.subplots(2,2)
axs[0,0]
fig, axs = plt.subplots(2,2, sharex='all') # all subplots share the X axis
fig, axs = plt.subplots(2,2, sharex='col') # only subplots in the same column share X
fig, axs = plt.subplots(2,2, sharey='row') # only subplots in the same row share Y 