#First Model From Scratch:)
import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self):
        self.w=np.random.randn()
        self.b=np.random.randn()
        self.MSE=None
        self.y_hat=None
        self.loss_container=[]
    def predict(self, x):
        y=self.w * x + self.b
        return y
    def fit(self,x,y,epochs=4000, learning_rate=0.01 ):
        for epoch in range(epochs):       
          loss=self.loss(x,y)
          self.loss_container.append(loss)
          gr_w,gr_b=self.gradient(x,y)
          self.w-=learning_rate * gr_w
          self.b-=learning_rate * gr_b
        self.y_hat=self.predict(x)
        self.MSE=self.loss(x,y)  

    def loss(self,x,y):
        n=len(x)
        y_hat=self.predict(x)
        error= y - y_hat
        MSE=(1/n)*np.sum((error)**2)
        return MSE  
    def gradient(self,x,y):
         n=len(x)
         y_hat=self.predict(x)
         error= y - y_hat
         gr_w=-(2/n)*np.sum(error * x)
         gr_b=(-2/n) * np.sum(error)
         return gr_w , gr_b
x1= np.array([1,2,3,4,5])
y1= np.array([1,2,3,4,5])
Linear_Reg=LinearRegression()
Linear_Reg.fit(x1,y1)
plt.title("Fit a Regression Line to your samples")
plt.xlabel("x")
plt.ylabel("y")

plt.scatter(x1,y1,color="red")
plt.plot(x1,Linear_Reg.y_hat,color="black")
plt.show()
