from matplotlib import pyplot as plt


def check_filtered_frames(images, filter):
    titles = ['Original Image', filter + ' X', filter + ' Y', filter + ' XY combined using OR ']
    plt.figure(figsize=(13, 5))
    for i in range(4):
        plt.subplot(2, 2, i + 1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.tight_layout()
    plt.show()
