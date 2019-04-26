import matplotlib.pyplot as plt

# fig1
# X = [10,100,1000,10000, 100000, 1000000]
# Y = [1.49, 8.82, 91.52, 931.95, 9345.92, 94298.60]

# fig2
# X = [10, 100, 1000, 10000, 100000]
# Y = [1.05, 8.26, 82.60, 876.74, 165157.64]


#fig3
'''
X = 10, y = 152916.05
X = 12, y = 10512.89
X = 20, y = 8854.58
'''
# X = [8, 10, 11,  12, 14, 16]
# Y = [325716.10, 152916.05, 69699.66, 10512.89, 8961.22, 8653.20]

#fig4
'''
X = 0.16, y = 49739.76
X = 0.2, y = 23595.67
X = 0.24, y = 14041.67
X = 0.28, y = 10144.72
X = 0.32, y = 9315.19

'''
# X = [0.16, 0.20, 0.24, 0.28, 0.32, 0.36, 0.40]
# Y = [49739.76, 23595.67, 14041.67, 10144.72, 9315.19, 9010.58, 8982.42]

plt.plot(X, Y)

# plt.xscale('log')

plt.ylabel('response time (ms)')
plt.xlabel('number of queries (set) - logarithmic scale')
plt.suptitle('Single redis instance, with no memory/cpu restriction', fontsize=16)

# plt.xticks([0.12, 0.14, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.40, 0.44, 0.48])

for i in range(len(X)):
    coordinates = '('+str(X[i]) +', '+str(Y[i])+')'
    plt.text(X[i], Y[i], coordinates, fontsize=9)
    plt.scatter(X[i], Y[i], c="r",marker='o')


# plt.show()
plt.savefig('fig.eps', format='eps' , bbox_inches='tight')
