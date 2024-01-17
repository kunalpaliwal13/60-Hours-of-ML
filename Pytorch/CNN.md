# Convolution Neural Network
   <img src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/590c3ce1-0ff4-4346-a0dc-c002012dd0c3" height ="250px" alt =""/>
  

- RGB v/s greyscale image

  <img src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/098c23e0-f429-4700-8ddd-6b92460d3589" height ="200px" alt =""/>
  <img src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/f7f3fcb1-a6e4-4773-be02-ea8b8beb8354" height ="200px" alt =""/>

  
- Working of CNN mathematically
  
  As we can see the size of the image is reduced, so we generally apply padding, which is adding a layer of piels around our image. This is used to avoid information loss.

  output size = img size - kernel size +1
  
  <img src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/b2ffd207-4044-4869-99da-b7c0fedc89a6" height ="200px" alt =""/>

- Max Pooling, Mean Pooling, Mean Pooling
  
  Suppose a 2x2 matrix(pooling layer) is applied onto a 3x3 matrix, and takes out the maximum value(max affecting feature) and gives us an output layer.
  This is called maxpooling layer, simimlarly there is min pooling and mean pooling
  
  <img src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/f3628ff5-f3d8-49a8-908b-81db8e27027a" height ="200px" alt =""/>

- Flattened Layer

  When the output of a CNN is derived, it is passed as an input layer for an ANN and that's how our CNN model works.

  <img src = "https://github.com/kunalpaliwal13/60-Hours-of-ML/assets/143526414/80612769-1ce5-48e8-b82b-0bf17631f882" height ="200px" alt =""/>


