#Second Model From Scratch:)
import numpy as np
import matplotlib.pyplot as plt
class LogisticRegression:

    def __init__(self):
        self.weight=np.random.rand()
        self.bias= 0
        self.loss=None
        self.prediction=None
        self.loss_histories=[]
    def predict_linear(self,x):  
         z =self.weight * x + self.bias
         return z
    
    def sigmoid(self,z):
        y = 1/(1+np.exp(-z))
        return y
    
    def predict(self,x):
       z = self.predict_linear(x)
       p = self.sigmoid(z)
       return p 
    
    def compute_loss(self,x,y):
        p = self.predict(x)
        eps = 1e-15
        p = np.clip(p, eps, 1 - eps)
        BCE= -np.mean(y * np.log(p) + (1-y) * np.log(1 - p))
        return BCE
    

    def grad(self,x,y):
        n = len (x)
        p =self.predict(x)
        error= p - y 
        dw=(1/n)* np.sum(error * x)
        db=(1/n)* np.sum(error)
        return dw,db

    def fit(self,x,y,epochs=4000,learning_rate=0.01):
        
        for epoch in range(epochs):
            loss=self.compute_loss(x,y)
            self.loss_histories.append(loss)
            gradient_w,gradient_b=self.grad(x,y)
            self.weight-= learning_rate * gradient_w
            self.bias-= learning_rate * gradient_b
        self.prediction=self.predict(x)
        self.loss= self.compute_loss(x,y)
        
x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]).reshape(-1,1)
y = np.array([0,0,0,0,0,0,0,0,1,1,1,1,1,1,1]).reshape(-1,1)
LR = LogisticRegression()
LR.fit(x,y)
predictions = LR.predict(x)

plt.title("Logistic Regression")
plt.xlabel("x")
plt.ylabel("y")
plt.scatter(x,y,color="blue",label = "Training data")
boundary = - LR.bias / LR.weight
plt.axvline(x=boundary, color="red" , linestyle="--" , label="decision boundary")
plt.legend()
plt.plot(x , predictions ,color="darkblue" )
plt.figure()
plt.plot(LR.loss_histories)
plt.ylabel("Binary Cross Entropy")
plt.show()          
