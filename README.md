This is a image classifier to predict driver distraction while driving.<br>
For more information on Dataset and Download visit <a href="https://www.kaggle.com/c/state-farm-distracted-driver-detection" target="_blank">here</a>
This contain a notebook.ipynb file in which a model is being trained and saved. Also to run the flask app, please follow the below commands.
1. `virtualenv env` or `conda create -n env pyhton==3.7`
2. `source ./env/bin/activate` or `conda activate env`
3. `pip install -r requirement.txt`
4. `pip install -r requirement_flask.txt`
5. `flask --app driver run`

Note - uploaded images should be from same distribution as training images, other images might get predicted wrong prediction. this can be test images from the data downloaded

<img src="./imgs/img1.png">

