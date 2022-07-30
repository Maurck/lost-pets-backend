from utils.utils import jsonify
from skimage.metrics import structural_similarity as compare_ssim
import cv2
import urllib.request
import numpy as np
import io
import PIL.Image as Image

class MatchFlow:

    def __call__(self, request):

        def isReferenceBigger(_nameReference, _nameBullet):
            reference = cv2.imread(_nameReference)
            width_reference = reference.shape[1]
            height_reference = reference.shape[0]
            indexReference = width_reference*height_reference

            bullet = cv2.imread(_nameBullet)
            width_bullet = bullet.shape[1]
            height_bullet = bullet.shape[0]
            indexBullet = width_bullet*height_bullet

            return indexReference > indexBullet

        def resize(original_route, dimensions_route, new_name):
            #ExtractNewDimensions
            img1 = cv2.imread(dimensions_route)
            new_width = img1.shape[1]
            new_height = img1.shape[0]
            dsize = (new_width, new_height)

            #Destiny
            img2 = cv2.imread(original_route)
            output = cv2.resize(img2, dsize)
            cv2.imwrite(new_name,output)

        def save_image(link,_newName):
            urllib.request.urlretrieve(link, _newName)

        def mse (imageA, imageB):
            err = np.sum((imageA.astype("float") - imageB.astype("float"))**2)
            err /= float(imageA.shape[0] * imageA.shape[1])
            return err

        # Flujo de IA
        link_reference = request.form["reference"]
        _bullet = request.files["img_from_user"]

        _nameReference = 'apis/ia/img/reference.jpg'
        _nameBullet = 'apis/ia/img/bullet.jpg'
        _nameRedim = 'apis/ia/img/redim.jpg'

        _bullet.save(_nameBullet)
        save_image(link_reference,_nameReference)

        if(isReferenceBigger(_nameReference, _nameBullet)):
            #resize de referencia
            resize(_nameReference,_nameBullet,_nameRedim)
            imageA = cv2.imread(_nameBullet) #What is not touched
        else:
            #resize de bullet
            resize(_nameBullet,_nameReference,_nameRedim)
            imageA = cv2.imread(_nameReference) #What is not touched

        imageB = cv2.imread(_nameRedim)

        # Convert gray scale
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        # compute the Structural Similarity Index (SSIM) between the two
        # images, ensuring that the difference image is returned
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")
        mseTarget = mse(grayA,grayB)
        return jsonify({"SSIM":format(score), "MSE":format(mseTarget)})

