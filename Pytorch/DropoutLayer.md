![image](https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/b03e145f-7e36-4a56-bfc2-7547fdfebae9)

For instance, if the hidden layers have 1000 neurons (nodes) and a dropout is applied with drop probability = 0.5, then 500 neurons would be randomly dropped in every iteration (batch).

Generally, for the input layers, the keep probability, i.e. 1- drop probability, is closer to 1, 0.8 being the best as suggested by the authors. For the hidden layers, the greater the
drop probability more sparse the model, where 0.5 is the most optimised keep probability, that states dropping 50% of the nodes.

In the overfitting problem, the model learns the statistical noise. To be precise, the main motive of training is to decrease the loss function, given all the units (neurons). So 
in overfitting, a unit may change in a way that fixes up the mistakes of the other units. This leads to complex co-adaptations, 
which in turn leads to the overfitting problem because this complex co-adaptation fails to generalise on the unseen dataset.

Now, if we use dropout, it prevents these units to fix up the mistake of other units, thus preventing co-adaptation, as in every iteration the presence of a unit is highly unreliable.
So by randomly dropping a few units (nodes), it forces the layers to take more or less responsibility for the input by taking a probabilistic approach.




