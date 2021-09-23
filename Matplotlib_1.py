import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2
# print(x)
#FUNCTION

plt.plot(x, y, 'r') # 'r' is the color red
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('String Title Here')
# plt.show()

# plt.subplot(nrows, ncols, plot_number)
plt.subplot(1,2,1)
plt.plot(x, y, 'r--') # More on color options later
plt.subplot(1,2,2)
plt.plot(y, x, 'g*-');
# plt.show()


#OBJECT

# Create Figure (empty canvas)
fig = plt.figure()

# Add set of axes to figure
axes = fig.add_axes([0.09,0.1,0.4,0.8]) # left, bottom, width, height (range 0 to 1)
axes2 = fig.add_axes([0.58,0.1,0.4,0.8])

# Plot on that set of axes
axes.plot(x,y,'g*--')
axes2.plot(y,x,'r--')
axes.set_xlabel('X Label')
axes.set_ylabel('Y label')
axes.set_title('Title')
axes2.set_xlabel('X Label')
axes2.set_ylabel('Y label')
axes2.set_title('Title')
# plt.show()

# subplot using object method
fig,axes = plt.subplots(nrows = 1, ncols = 2)

axes[0].plot(x,y)
axes[0].set_xlabel('x Label')
axes[1].plot(y,x)
axes[1].set_xlabel('X Label')
plt.tight_layout()
# plt.show()
