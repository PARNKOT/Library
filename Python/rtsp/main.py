import time

import cv2

login = "admin"
password = "Pa$$w0rd"
ip_addr = "10.1.1.16"

rtsp_uri = f"rtsp://{login}:{password}@{ip_addr}/Streaming/Channels/101?transportmode=unicast&profile=Profile_1"
# rtsp_uri = f"rtsp://{login}:{password}@{ip_addr}/Streaming/Channels/101"
# rtsp://admin:Pa$$w0rd@10.1.1.16/Streaming/Channels/101?transportmode=unicast&profile=Profile_1

fps = 15


def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width, height)

    return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)


if __name__ == "__main__":
    video_stream = cv2.VideoCapture(rtsp_uri)

    bgs_method = cv2.bgsegm.createBackgroundSubtractorGSOC()

    while video_stream.isOpened():
        ret, frame = video_stream.read()
        if ret:
            frame = rescale_frame(frame, 0.5)

            foreground_mask = bgs_method.apply(frame)
            background_img = bgs_method.getBackgroundImage()

            cv2.imshow("frame", frame)
            cv2.imshow("foreground", foreground_mask)
            cv2.imshow("background", background_img)

            if cv2.waitKey(0) & 0xFF == ord('q'):
                break
            #time.sleep(1/fps)

    video_stream.release()
    cv2.destroyAllWindows()
