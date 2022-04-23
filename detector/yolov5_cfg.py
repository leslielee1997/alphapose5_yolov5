from easydict import EasyDict as edict

cfg = edict()
cfg.CONFIG = 'f:/code/pose/AlphaPose/detector/yolov5/models/yolov5s.yaml'
cfg.WEIGHTS = 'f:/code/pose/AlphaPose/detector/yolov5/yolov5s.pt'
cfg.INP_DIM = 640
cfg.NMS_THRES =  0.6
cfg.CONFIDENCE = 0.1
cfg.NUM_CLASSES = 80
