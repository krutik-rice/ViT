### SigLIP - 400m parameters improvement over clip by openai.
### Softmax loss (entire imageset) is replaced by sigma loss (individual pairs)
### Clips work with dot products of image and text. (Higher dot product means better matching)
### Loss funciton is what gives the dot product meaning. (Higher vs lower)
### Layman terms - CLip compares all rows and columns, so we match the text and image 

 from PIL import Image
