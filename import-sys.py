import sys
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import plotly

print(sys.version)

a = np.zeros(4)
print(a)
z = np.ones(10)
print(z)
print(z.shape)
z = np.empty(5)
z = np.linspace(2, 10, 5)
print(z)
z = np.array([10,20])
print(z)

np.random.seed(0)
z1 = np.random.randint(10000, size=1000000000)

np.sort(z1)

from skimage import io
photo = io.imread('~/Downloads/Create-a-virtual-library-COVER.jpg')

print(photo.shape)
plt.imshow(photo)

plt.imshow(photo)
print(np.min(photo))