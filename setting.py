import configparser
import cv2


def nothing(x):
    pass


class Setting(object):
    @staticmethod
    def setting_init():
        path = r'E:\VSCodeProjects\demo\conf.init'
        config = configparser.ConfigParser()
        config.read(path)
        DefectNum_cam0 = config.getint("init", "defectNum_cam0")
        DefectNum_cam1 = config.getint("init", "defectNum_cam1")
        Cam0_queue = config.getint("init", "cam0_queue")
        Cam1_queue = config.getint("init", "cam1_queue")
        cam_delay = config.getfloat("init", "cam_delay")*100
        switchon_delay = config.getfloat("init", "switchon_delay")*100
        switchoff_delay = config.getfloat("init", "switchoff_delay")*100
        cam_delay = int(cam_delay)
        switchon_delay = int(switchon_delay)
        switchoff_delay = int(switchoff_delay)

        cv2.namedWindow("Parameter_setting")
        cv2.createTrackbar("DefectNum_cam0", "Parameter_setting", DefectNum_cam0, 10, nothing)
        cv2.createTrackbar("DefectNum_cam1", "Parameter_setting", DefectNum_cam1, 10, nothing)
        cv2.createTrackbar("Cam0_queue", "Parameter_setting", Cam0_queue, 10, nothing)
        cv2.createTrackbar("Cam1_queue", "Parameter_setting", Cam1_queue, 10, nothing)
        cv2.createTrackbar("cam_delay", "Parameter_setting", cam_delay, 100, nothing)
        cv2.createTrackbar("switchon_delay", "Parameter_setting", switchon_delay, 100, nothing)
        cv2.createTrackbar("switchoff_delay", "Parameter_setting", switchoff_delay, 100, nothing)
        while True:
            DefectNum_cam0 = cv2.getTrackbarPos("DefectNum_cam0", "Parameter_setting")
            DefectNum_cam1 = cv2.getTrackbarPos("DefectNum_cam1", "Parameter_setting")
            Cam0_queue = cv2.getTrackbarPos("Cam0_queue", "Parameter_setting")
            Cam1_queue = cv2.getTrackbarPos("Cam1_queue", "Parameter_setting")
            cam_delay = cv2.getTrackbarPos("cam_delay", "Parameter_setting")
            switchon_delay = cv2.getTrackbarPos("switchon_delay", "Parameter_setting")
            switchoff_delay = cv2.getTrackbarPos("switchoff_delay", "Parameter_setting")

            config.set("init", "DefectNum_cam1", str(DefectNum_cam1))
            config.set("init", "DefectNum_cam0", str(DefectNum_cam0))
            config.set("init", "Cam0_queue", str(Cam0_queue))
            config.set("init", "Cam1_queue", str(Cam1_queue))
            config.set("init", "cam_delay", str(cam_delay/100))
            config.set("init", "switchon_delay", str(switchon_delay/100))
            config.set("init", "switchoff_delay", str(switchoff_delay/100))

            config.write(open('conf.init', 'w'))

            cv2.waitKey(1)
        cv2.destroyAllWindows()
