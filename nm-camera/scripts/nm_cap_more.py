import cv2

# 相机的索引列表
camera_indices = [0]  # 【0，1，2，3】

# 创建一个字典来存储视频捕获对象
caps = {index: cv2.VideoCapture(index) for index in camera_indices}

# 设置每个相机的参数（如果需要）
for cap in caps.values():
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    # 如果需要设置特定的编码格式：
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    cap.set(cv2.CAP_PROP_FOURCC, fourcc)

try:
    while True:
        # 对于每个相机捕获帧并显示
        for index, cap in caps.items():
            ret, frame = cap.read()
            if ret:
                cv2.imshow(f'Camera {index}', frame)

        # 按下 'q' 键退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except Exception as e:
    print(f"发生错误：{e}")
finally:
    # 释放所有相机
    for cap in caps.values():
        cap.release()
    # 关闭所有OpenCV窗口
    cv2.destroyAllWindows()
