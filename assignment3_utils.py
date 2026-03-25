import numpy as np

# This is specific to the Pong environment
def img_crop(img):
    # Remove score/top border and bottom margin
    return img[30:-12, :, :]

# General Atari preprocessing steps
def downsample(img):
    # Reduce image resolution by taking every second pixel
    return img[::2, ::2]

def transform_reward(reward):
    # Convert reward to its sign: -1, 0, or 1
    return np.sign(reward)

def to_grayscale(img):
    # Convert RGB image to grayscale by averaging color channels
    return np.mean(img, axis=2).astype(np.uint8)

def normalize_grayscale(img):
    # Correct normalization from [0, 255] to [-1, 1]
    return (img.astype(np.float32) / 127.5) - 1.0

def process_frame(img, image_shape):
    # Crop Pong-specific borders
    img = img_crop(img)

    # Downsample image by factor of 2
    img = downsample(img)

    # Convert to grayscale
    img = to_grayscale(img)

    # Normalize to [-1, 1]
    img = normalize_grayscale(img)

    # Reshape to (1, H, W, 1)
    return np.expand_dims(img.reshape(image_shape[0], image_shape[1], 1), axis=0)