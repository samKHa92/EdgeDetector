import cv2


def generate_frames_with_circles():
    x = 130
    y = 50
    color = (0, 0, 255)
    radius = 10
    thickness = 2
    for i in range(1, 11):
        path = 'resources/starting_resources/frames/frame' + str(i) + '.jpeg'
        image = cv2.imread(path)
        center_coordinates = (x, y)
        image = cv2.circle(image, center_coordinates, radius, color, thickness)
        cv2.imwrite('resources/generated_resources/frames/generated_frame' + str(i) + '.jpeg', image)
        x += 48
        y += 36
        radius += 3
        if i % 4 == 0:
            thickness += 1

    for i in range(11, 17):
        path = 'resources/starting_resources/frames/frame' + str(i) + '.jpeg'
        image = cv2.imread(path)
        center_coordinates = (x, y)
        image = cv2.circle(image, center_coordinates, radius, color, thickness)
        cv2.imwrite('resources/generated_resources/frames/generated_frame' + str(i) + '.jpeg', image)
        x += 70
        y -= 50
        radius -= 4
        if i % 3 == 0:
            thickness -= 1

    for i in range(16, 17):
        path = 'resources/starting_resources/frames/frame' + str(i) + '.jpeg'
        image = cv2.imread(path)
        center_coordinates = (x, y)
        image = cv2.circle(image, center_coordinates, radius, color, thickness)
        cv2.imwrite('resources/generated_resources/frames/generated_frame' + str(i) + '.jpeg', image)
        x += 70
        y -= 30
        radius -= 4
        if i % 3 == 0:
            thickness -= 1

    for i in range(17, 21):
        path = 'resources/starting_resources/frames/frame' + str(i) + '.jpeg'
        image = cv2.imread(path)
        center_coordinates = (x, y)
        image = cv2.circle(image, center_coordinates, radius, color, thickness)
        cv2.imwrite('resources/generated_resources/frames/generated_frame' + str(i) + '.jpeg', image)
        x += 15
        y -= 10
        radius -= 1
        if i % 3 == 0:
            thickness -= 1


def generate_video_from_frames(frames_path, video_path, frame_indicator):
    frames = []
    for i in range(1, 21):
        frames.append(frames_path + '/' + frame_indicator + '_frame' + str(i) + '.jpeg')
    video = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'mp4v'), 5, (1280, 335))
    for filename in frames:
        img = cv2.imread(filename)
        video.write(img)
    video.release()


def generate_frames_from_video(video_path, frames_path='resources/generated_resources/frames'):
    video = cv2.VideoCapture(video_path)
    success, image = video.read()
    count = 1
    while success:
        cv2.imwrite(frames_path + '/generated_frame' + str(count) + '.jpeg', image)  # save frame as JPEG file
        success, image = video.read()
        count += 1
