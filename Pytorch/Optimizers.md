# Optimizers
- Gradient descent

### Grdaient Descent
- same with ML
- as it doesn't take data in batches, so batch size is entire dataset
- not good for large datasets

### Stochastic Gradient Descent
- various iterations in each epoch for every data point
- Convergence is slow and very noisy
<img src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/0f9a8eb7-71ea-4e74-9685-8493baa457cc" height = "250p" alt= " ">
<img src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/d45373b0-758d-44fd-bdd4-4a1e3323b952" height = "200p" alt= " ">




### Mini Batch SGD
- Makes baches in every iteration in an epoch 
- Convergence is better but it still has noise
- Time complexity is better

<img src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/eb0dee27-9ab4-4b6a-b8bb-d49e02499b4e" height = "250p" alt= " ">
<img src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/1e779e50-0970-4399-99c4-bd6be92f62f3" height = "250p" alt= " ">


### Mini Batch SGD with momentum
- Smoothens the entire process
- Brings in the concept of exponential weighted average
- Time complexity is better as noise is reduced


<img src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/d945aacb-04c6-478f-94da-3b34faae7102" height = "250p" alt= " ">

### Adaptive Gradient Descent (Adagrad)
- The gradient descent starts with a certain learning rate, and slowens down when approaching global minima
- Overtime, th elarning rate might become insignificant and weights might stop updating. 

<img src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/d5e9e93d-a52e-4955-9774-01ccb10444d1" height = "250p" alt= " ">


### Adadelta and RAMSPROP
- here we're trying to control the time dependent term from becoming zero, but in both of the process, we missed out the smoothening process

<img src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/9d3aceca-5d26-43c4-ae08-89d3d504cb68" height = "250p" alt= " ">

### Adam Optimizer
- here we have adaptive learning rate, and we use momentum as well
- There are various variations of this optimizer as well


<img src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/7134d99b-1d4b-4513-8f3c-068dd3ce94a2" height = "250p" alt= " ">
<img src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/48a62581-b55e-46c6-b784-24cf50af5319" height = "250p" alt= " ">




