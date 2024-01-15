# About Activation Functions

## Sigmoid Function
- prone to vanishing gradient
- time consuming operations
- suitable for binary classification
- inefficient weight updation(not zero centric)

<image src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/a6f6914b-2ca5-4717-9a87-2327d3172ccd" height="200px" alt="sigmoid function">


## Tanh Function
- efficient weight updation (zero centric)
- prone to vanishing gradient (for deep deep NN)
- timely complex


<image src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/0eb7ce66-a1bc-4bd1-9428-3e2ed894495e" height="200px" alt="tanh function">



## Relu Function
- if(relu output =0){weight updates} else {dead neouron}
- not prone to vanishing gradient (good for deep NN) ⭐
- fast calculation
- not zero centric(inefficient weight updation)

<image src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/b36964c4-37d8-4ee0-abd0-d715b2b2b768" height="200px" alt="relu function">


## Leaky Relu
- Advantages of Relu
- Removes dead Relu problem
- not zero centric

<image src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/87e22e37-fb6b-45bb-97fb-601f9835d634" height="200px" alt="Leaky relu function">


## Exponential Relu
- No dead Relu issue
- zero centric
- computationally more expensive(exponent)

<image src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/43a0f968-5067-49c0-9630-358cc5bd2091" height="200px" alt=" Exponential relu function">

# Where to use which functions

For binary classifications, use Relu, PRelu, Elu for hidden layers and sigmoid foe output.<br>
For multiclass, use Relu or a modificationa in the hidden layers and SOftmax for output layer.

<image src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/83aca1e6-cd2b-4676-bd8e-8e0eab8c4642" height="200px" alt="ANN Classification">


For regression, use Relu for hidden layer and linear activation for output layer.

<image src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/76f49cd3-01c1-4a54-ac9d-d432997eb709" height="200px" alt="ANN Classification">














