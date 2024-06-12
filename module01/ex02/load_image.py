import numpy as np
from PIL import Image
from PIL import UnidentifiedImageError as Denied


def ft_load(path: str) -> np.ndarray:
    """This function prints the shape of an image and returns a list of lists
with the combination of RGB colors"""
    try:
        image = Image.open(path)
        if image.format != "JPEG":
            raise AssertionError("Incorrect image format")
        if image.mode != "RGB":
            raise AssertionError("The image is not in RGB")
        image_np = np.array(image)
        image.close()
        print(f"The shape of the image is: {image_np.shape}")
        return image_np
    except (ValueError, TypeError, FileNotFoundError, Denied,
            PermissionError, IsADirectoryError, AssertionError) as e:
        print(e)
        return np.array([])
