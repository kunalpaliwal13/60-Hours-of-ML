class Linear_Regression:
  def __init__(self, learning_rate, iteration_num):
     self.learning_rate= learning_rate
     self.iteration_num = iteration_num

  def fit(self,X, Y):

    #number of training examples n number of features

    self.m, self.n = X.shape #rows n columns 
    self.w= np.zeros(self.n)
    self.b= 0
    self.X= X
    self.Y= Y

    #implementing gradient descent 

    for i in range(self.iteration_num):
      self.update_weights()
  
  def update_weights(self):

    Y_prediction= self.predict(self.X)

    #calculate gradient

    dw= -(2* (self.X.T).dot(self.Y-Y_prediction))/ self.m

    db = -2*np.sum(self.Y- Y_prediction)/self.m

    #updating wieghts

    self.w= self.w- self.learning_rate*dw
    self.b= self.b- self.learning_rate*db
  
  def predict(self,X):
    return X.dot(self.w)+ self.b