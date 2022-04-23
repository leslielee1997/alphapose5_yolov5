from easydict import EasyDict as edict

cfg = edict()
# yolov3
# cfg.CONFIG = 'detector/yolo/cfg/yolov3.cfg'
# cfg.WEIGHTS = 'detector/yolo/data/yolov3.weights'
# yolov3-spp
cfg.CONFIG = 'f:/code/pose/AlphaPose/detector/yolo/cfg/yolov3-spp.cfg'
cfg.WEIGHTS = 'f:/code/pose/AlphaPose/detector/yolo/data/yolov3-spp.weights'
#yolov3-tiny
# cfg.CONFIG = 'detector/yolo/cfg/yolov3-tiny.cfg'
# cfg.WEIGHTS = 'detector/yolo/data/yolov3-tiny.weights'
#检测网络的输入大小。inp_dim 应该是 32 的倍数。默认为 608。增加它可能会提高准确性。
cfg.INP_DIM = 608#608/320
#用于人体检测的 NMS 阈值。增加该值可以提高最终精度，但会降低速度。默认值为 0.6
cfg.NMS_THRES =  0.6
#人类检测的置信度阈值。降低该值可以提高最终精度，但会降低速度。默认值为 0.05
cfg.CONFIDENCE = 0.1
cfg.NUM_CLASSES = 80
