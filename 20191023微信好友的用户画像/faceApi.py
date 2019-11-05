import json
import TencentYoutuyun


class FaceAPI:

    def __init__(self):
        appid = '10109383'
        userId = '875974254'
        secretId = 'AKIDd3D8rKrzCAsKXXKn8E5i6EAsLYVCuoiP'
        secretKey = 'ZtwjGYbP1PYT9anmV3MRGrCKDuPffOr4'
        endPoint = TencentYoutuyun.conf.API_YOUTU_END_POINT
        self.youtu = TencentYoutuyun.YouTu(appid, secretId, secretKey, userId, endPoint)

    def detectFace(self, image):
        try:
            retocr = self.youtu.DetectFace(image)
            return len(retocr['face']) > 0
        except Exception as e:
            return False

    def extractTags(self, image):
        try:
            retocr = self.youtu.imagetag(image)
            return retocr['tags']
        except Exception as e:
            return None