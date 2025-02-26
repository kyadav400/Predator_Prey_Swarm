
In this paper, we train two pretrained models Detectron2 and YOLOv5 with our own data-set for object detection. This project compares the performance of Detectron2 and YOLOv5 on a small data-set by checking training time, train-ing accuracy, classification accuracy, and classification speed.We found that for detectron2, the classification accuracy in my test data-set was 60 percent. It detects at least 6 out of 10 objects correctly with more than 90 percent of confidence match. The 60 percent classification accuracy is based on 10 test images. YOLOv5 is able to detect all 10 objects with theaccuracy of at least 50 percentage with less confidence than Detectron2. Between Detectron2 and YOLOv5, Detectron2has more accuracy with 110 training images with higher training time.

Detectron2 is a computer vision model zoo written in PyTorch by FAIR. For this project, I used the model Mask R-CNN(R50-FPN, 3x). Mask R-CNN extends Faster R-CNN to solve the instance segmentation tasks by adding a branch for predicting an object mask in parallel with the existing branch for bounding box recognition. 
Instanced segmentation is semantic segmentation in which each pixel is labeled
with what object instance of a class it belongs to as well as the class.

Architecture: Convolution Neural Network, RolAlign, Softmax, RPN, Dense Connections, ResNet

Maximum iteration:1800

Ir sched: 50

Backbone Layers: 50

Training Memory: 

Training Time: 12:50

Learning rate: 0.00025

Number of classes: 10

<img width="855" alt="Screen Shot 2022-03-25 at 11 42 42 PM" src="https://user-images.githubusercontent.com/97614990/160223459-18763bd9-343d-49de-b23b-9c05300d7cac.png">


The classification accuracy in my training dataset is pretty impressive. It’s 98%. 
The accuracy here is computed based on the number of instances detected in the dataset. In the validation dataset, the accuracy is 82%. Images below are the sample results of the validation.

![Validation1](https://user-images.githubusercontent.com/97614990/160222998-d5ed6e72-bfda-4086-808d-ad0e5eaf90fb.png)
![validation2](https://user-images.githubusercontent.com/97614990/160223000-6b4fccc6-8d2c-41fb-a487-78f618803484.png)

The classification accuracy in validation dataset is a little less as compared to the classification accuracy of training dataset because of several reasons. One reason could be less training and validating data. I trained the network with 110 images. Lighting conditions and angles at which images are captured also contributed to the accuracy. In my case, I have one black bag and one brown bag. And in low lighting conditions, the model sometimes fails to validate these objects. In my case, I used camera of Kinova Robotic arm and the position of camera is not in the great position thus the angles of pictures 
were not so good because the objects are inside the box. It was possible to get the full view of all the objects from the top view and from the side view some parts of object was missing. One way to improve the performance is by calibrating the camera and by filtering the noise.

<img width="416" alt="graph1" src="https://user-images.githubusercontent.com/97614990/160223503-01bd5d13-ef1c-49c4-b3c5-2d9f55f8d3cf.png">

<img width="416" alt="Screen Shot 2022-03-25 at 11 58 13 PM" src="https://user-images.githubusercontent.com/97614990/160223905-428e8d35-73ce-4529-b14f-74fadb5f469b.png">


For the test dataset, I used images of occluded objects captured at different angles in varying lighting conditions. I captured these images during Deliverable 2. I have 40 images in the test dataset. The difference between training+validation and test datasets is images in training+validation datasets were images of non occluded objects.

The classification accuracy in my test dataset is good. It’s 60%. It detects at least  6 out of 10 objects correctly with more than 90% of confidence match. The 60% classification accuracy is based on 10 test images. Images below are the generalized results.

![download (1)](https://user-images.githubusercontent.com/97614990/164941225-0aa6887c-847b-4762-a276-419f4c19905f.png)

![download (2)](https://user-images.githubusercontent.com/97614990/164941285-30033de7-61f7-4ea2-b0f7-8e08dec51111.png)

![download](https://user-images.githubusercontent.com/97614990/164941320-2ddc055c-c2ee-4ef6-aafe-22093ca0d937.png)


One reason my test set performed bad as compared to training and validation data set is labeling. I think I did not do a good job in labeling the training and validating datasets. Another reason could be the small size of the training dataset. I trained the model with just 110 images. This is called overfitting- when the model learns too much or memorizes the training data sets because of a small amount of training dara and does not perform well on unseen data.

