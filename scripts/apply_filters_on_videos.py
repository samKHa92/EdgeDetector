import scripts.apply_filters_on_frames
import scripts.resource_generation


def sobel_filter_video(video_path):
    scripts.resource_generation.generate_frames_from_video(video_path)
    for i in range(1, 21):
        frame = 'resources/generated_resources/frames/generated_frame' + str(i) + '.jpeg'
        scripts.apply_filters_on_frames.sobel_filter_frame(frame, i)
    scripts.resource_generation.generate_video_from_frames('resources/filtered_resources/frames/sobel/combined/',
                                                           'resources/filtered_resources/videos/sobel/combined.mp4',
                                                           'filtered')
    scripts.resource_generation.generate_video_from_frames('resources/filtered_resources/frames/sobel/vertical/',
                                                           'resources/filtered_resources/videos/sobel/vertical.mp4',
                                                           'filtered')
    scripts.resource_generation.generate_video_from_frames('resources/filtered_resources/frames/sobel/horizontal/',
                                                           'resources/filtered_resources/videos/sobel/horizontal.mp4',
                                                           'filtered')

def scharr_filter_video(video_path):
    scripts.resource_generation.generate_frames_from_video(video_path)
    for i in range(1, 21):
        frame = 'resources/generated_resources/frames/generated_frame' + str(i) + '.jpeg'
        scripts.apply_filters_on_frames.scharr_filter_frame(frame, i)
    scripts.resource_generation.generate_video_from_frames('resources/filtered_resources/frames/scharr/combined/',
                                                           'resources/filtered_resources/videos/scharr/combined.mp4',
                                                           'filtered')
    scripts.resource_generation.generate_video_from_frames('resources/filtered_resources/frames/scharr/vertical/',
                                                           'resources/filtered_resources/videos/scharr/vertical.mp4',
                                                           'filtered')
    scripts.resource_generation.generate_video_from_frames('resources/filtered_resources/frames/scharr/horizontal/',
                                                           'resources/filtered_resources/videos/scharr/horizontal.mp4',
                                                           'filtered')
