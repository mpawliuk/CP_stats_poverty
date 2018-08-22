from scipy import stats
import numpy as np
import matplotlib.pyplot as plt  # For plotting

# Extract data from data.txt
f = open("data.txt","r")
data = [line.split() for line in f]
x = np.array([int(line[0]) for line in data])
y = np.array([float(line[1]) for line in data])

# Compute the stats stuff
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
plt.plot(x, y, 'r.-')

# Year range
start = 2010
end = 2030
x = np.array(range(start,end+1,5))

# Plot the line of best fit +- Standard Dev 
plt.plot(x, slope*x+intercept, 'b.-') # Line of best fit.
plt.plot(x, slope*x+intercept + std_err, 'g.-') # Upper bound for standard deviation
plt.plot(x, slope*x+intercept - std_err, 'g.-') # Lower bound for standard deviation
plt.savefig('regr_line.png')

# Printing in Markdown
print('{} | Value'.format('Quantity'.ljust(16)))
print('{} | {}'.format(''.rjust(16,'-'), ''.rjust(16,'-')))
print('{} | {:.3f}x+{:.3f}'.format('Line of best fit'.rjust(16), slope, intercept))
print('{} | {:.3f}'.format('r value'.ljust(16), r_value))
print('{} | {:.3f}'.format('p value'.ljust(16), p_value))
print('{} | {:.3f}'.format('Standard rrror'.ljust(16), std_err))

f.close()
