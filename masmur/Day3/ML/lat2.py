import numpy as np
from sklearn.linear_model import LinearRegression

#data acquasition
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1,1)) # tanggal
y = np.array([5, 20, 14, 32, 22, 38]) # harga saham

print(x.shape, y.shape)

# create model
model = LinearRegression() #life saver

#fit it
model.fit(x, y)


#get score
r_sq = model.score(x,y)
print('Koefisien Determinasi', r_sq) # tingkat keyakinan prediction y = mx


#predict
x1 = np.array([65, 75]).reshape((-1,1))
print('Prediksi', model.predict(x1))

