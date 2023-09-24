import numpy as np
import matplotlib.pyplot as plt
X = np.array([1,2,3,4,5])
Y = np.array([1,4,9,16,25])
plt.plot(X,Y,label="hoge",marker="o",linestyle="None")
plt.xlabel("$X$ [piyo]")
plt.ylabel("$Y$ [fuga]")
plt.legend()
plt.ylim(-10,40)
plt.savefig("./figure/fig.png")