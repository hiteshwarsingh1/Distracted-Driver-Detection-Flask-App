import numpy as np
import pickle
from skimage.feature import hog
from skimage.io import imread
from skimage.transform import resize


def get_res(val):
    if val==0:
        return "Safe Driving"
    else:
        return "Driver is Distracted"

def get_hog(images, name='hog', save=False):
    result = np.array([hog(img, block_norm='L2',orientations=9, pixels_per_cell=(8, 8), cells_per_block=(3, 3)) for img in images])
    return result

def detect(path):
    Xv=[]
    img = imread(path)
    new_img = resize(img, (64, 128))
    Xv.append(new_img)
    Xv=np.array(Xv)

    hog_input = get_hog(Xv, name='hog_train', save=True)

    pca_reload = pickle.load(open("pca_dump.pkl",'rb'))
    norm_reload = pickle.load(open("Norm_dump.pkl",'rb'))
    model = pickle.load(open("model_pca_dump.pkl",'rb'))

    norm_hog_input = norm_reload.transform(hog_input)
    pca_norm_hog_train = pca_reload.transform(norm_hog_input)
    driver_pred = model.predict(pca_norm_hog_train)

    res = get_res(driver_pred[0])
    return res