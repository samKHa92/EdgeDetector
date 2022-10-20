import scripts.resource_generation
import scripts.apply_filters_on_videos
import scripts.check_filters_on_frames

if __name__ == "__main__":
    scripts.resource_generation.generate_frames_with_circles()
    scripts.resource_generation.generate_video_from_frames('resources/generated_resources/frames',
                                                           'resources/generated_resources/videos/generated_circle.mp4',
                                                           'generated')

    scripts.apply_filters_on_videos.sobel_filter_video('resources/generated_resources/videos/generated_circle.mp4')
    scripts.apply_filters_on_videos.scharr_filter_video('resources/generated_resources/videos/generated_circle.mp4')

    # scripts.check_filters_on_frames.check_filtered_frames(scripts.apply_filters_on_frames.scharr_filter_frame(
    #     'resources/generated_resources/frames/generated_frame1.jpeg', 1),'Scharr')
    # scripts.check_filters_on_frames.check_filtered_frames(scripts.apply_filters_on_frames.sobel_filter_frame(
    #     'resources/generated_resources/frames/generated_frame1.jpeg', 1),'Sobel')
