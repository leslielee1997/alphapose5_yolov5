# -----------------------------------------------------
# Copyright (c) Shanghai Jiao Tong University. All rights reserved.
# Written by Chao Xu (xuchao.19962007@sjtu.edu.cn)
# -----------------------------------------------------

"""API of detector"""
from abc import ABC, abstractmethod


def get_detector(opt=None, cfg=dict()):
    if opt.detector == 'yolo':
        from detector.yolo_api import YOLODetector as det
        from detector.yolo_cfg import cfg as default_cfg
        # return YOLODetector
    elif opt.detector == 'yolov5':
        from detector.yolov5_api import YOLOV5Detector as det
        from detector.yolov5_cfg import cfg as default_cfg
    elif opt.detector == 'tracker':
        from detector.tracker_api import Tracker as det
        from detector.tracker_cfg import cfg as default_cfg
        # return Tracker(cfg, opt)
    elif opt.detector.startswith('efficientdet_d'):
        from detector.effdet_api import EffDetDetector as det
        from detector.effdet_cfg import cfg as default_cfg
        # return EffDetDetector(cfg, opt)
    else:
        raise NotImplementedError

    final_cfg = default_cfg.copy()
    final_cfg.update(cfg)
    return det(final_cfg, opt)


class BaseDetector(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def image_preprocess(self, img_name):
        pass

    @abstractmethod
    def images_detection(self, imgs, orig_dim_list):
        pass

    @abstractmethod
    def detect_one_img(self, img_name):
        pass
