import cv2

# 打开视频捕获设备
cap = cv2.VideoCapture(0)

# 检查相机是否成功打开
if not cap.isOpened():
    print("无法打开相机")
    exit()

# 设置相机参数
# 设置分辨率为640x480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 设置帧率为120fps
# 注意：实际可设置的帧率可能受到摄像头硬件和驱动的限制
cap.set(cv2.CAP_PROP_FPS, 120)

# 设置相机输出格式为'MJPG'
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

try:
    while True:
        # 从相机捕获一帧
        ret, frame = cap.read()
        if not ret:
            print("无法读取帧")
            break

        # 显示帧
        cv2.imshow('Frame', frame)

        # 按 'q' 键退出循环
        if cv2.waitKey(1) == ord('q'):
            break
finally:
    # 释放相机设备
    cap.release()
    # 关闭所有OpenCV窗口
    cv2.destroyAllWindows()
