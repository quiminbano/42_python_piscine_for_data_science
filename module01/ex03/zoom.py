from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plot


def main():
    try:
        image = ft_load("animal.jpeg")
        if image.size == 0:
            raise AssertionError("Error processing the image")
        print(image)
        grayscale = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
        grayscale = grayscale.astype(int)
        grayscale = grayscale.reshape(image.shape[0], image.shape[1], 1)
        grayscale = grayscale[100:500, 449:849]
        shape0 = grayscale.shape[0]
        shape1 = grayscale.shape[1]
        shape2 = grayscale.shape[2]
        print("The new shape after slicing: ", end="")
        print(f"({shape0}, {shape1}, {shape2}) or ({shape0}, {shape1})")
        print(grayscale)
        plot.imshow(grayscale, 'gray')
        plot.xlabel('X')
        plot.ylabel('Y')
        plot.title('Racoon')
        plot.show()

    except AssertionError as e:
        print(e)


if __name__ == '__main__':
    main()
