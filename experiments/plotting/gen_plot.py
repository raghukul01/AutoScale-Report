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

#fig5
# Different queries on a cluster of 6 nodes
# X = [10, 100, 1000, 10000, 100000, 1000000]
# Y = [1.05, 8.86, 77.09, 874.78, 8052.35, 91247.44]

# fig6
# variation of response time with the number of nodes in cluster
# Number of queries kept fixed - 10^5 queries
# X = [1, 2, 3, 4, 5]
# Y = [7681.32, 7735.65, 7553.48, 7783.68, 7868.42]

#fig7
# variation of down time in different cluster configs
# number of keys stored in system is 10^5
# X = [2, 3, 4, 5, 6]
# Y = [3289.17, 2336.22, 1401.345, 1218.66, 991.40]


#fig8
# variation of number of keys, varying number of nodes also.

# plt.plot(X, Y, label='cluster')
# plt.xscale('log')

x1 = [1, 1.1]
y1 = [9581.98, 68284.44]

x2 = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
y2 = [9489.88, 10223.69, 11295.78, 13280.35, 14054.00, 14698.6, 78593.78]

x3 = [1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3]
y3 = [14690.53, 15579.69, 16842.89, 17425.28, 18263.41, 19195.42, 101342.3]

x4 = [2.3, 2.4]
y4 = [19753.17, 21329.86]

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)


plt.ylabel('avg. time (ms)')
plt.xlabel('number of queries (x * 10^5)')
plt.suptitle('Varying queries and number of nodes', fontsize=16)
# plt.legend(loc='upper left')
# plt.xticks([0.12, 0.14, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.40, 0.44, 0.48])

for i in range(len(x1)):
    coordinates = '('+str(x1[i]) +', '+str(y1[i])+')'
    plt.scatter(x1[i], y1[i], c="r",marker='o')
for i in range(len(x2)):
    coordinates = '('+str(x2[i]) +', '+str(y2[i])+')'
    plt.scatter(x2[i], y2[i], c="r",marker='x')
for i in range(len(x3)):
    coordinates = '('+str(x3[i]) +', '+str(y3[i])+')'
    plt.scatter(x3[i], y3[i], c="r",marker='*')
for i in range(len(x4)):
    coordinates = '('+str(x4[i]) +', '+str(y4[i])+')'
    plt.scatter(x4[i], y4[i], c="r",marker='+')





# plt.show()
plt.savefig('fig.eps', format='eps' , bbox_inches='tight')
