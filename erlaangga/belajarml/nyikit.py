import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5,15,25,15,45,55]).reshape((-1,1)) #ditranslasi
y = np.array([5,20,14,32,22,38]) #output (predictor)

print(x.shape, y.shape)

model = LinearRegression()

# fit
model.fit(x,y)

r_sq = model.score(x,y)
print("Koefisien kartesian: ", r_sq) # tingkat keyakinan program