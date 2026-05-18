# lane_functions.py
import cv2
import numpy as np

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def canny(img, low_threshold, high_threshold):
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    if len(img.shape) > 2:
        channel_count = img.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    return cv2.bitwise_and(img, mask)

def draw_lines(img, lines, color=[255,0,0], thickness=2):
    if lines is None:
        return
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img, (x1,y1), (x2,y2), color, thickness)

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img

def weighted_img(img, initial_img, α=0.8, β=1., γ=0.):
    return cv2.addWeighted(initial_img, α, img, β, γ)

def process_image(image):
    gray = grayscale(image)
    blur = gaussian_blur(gray, 5)
    edges = canny(blur, 50, 150)

    imshape = image.shape
    vertices = np.array([[
        (0, imshape[0]),
        (imshape[1], imshape[0]),
        (imshape[1]//2, imshape[0]//2)
    ]], dtype=np.int32)

    masked_edges = region_of_interest(edges, vertices)
    line_image = hough_lines(masked_edges, rho=2, theta=np.pi/180, threshold=50, min_line_len=40, max_line_gap=100)
    result = weighted_img(line_image, image)
    return result

def process_image_with_steps(image):
    """Process image and return all intermediate steps for visualization"""
    original = image.copy()
    gray = grayscale(image)
    blur = gaussian_blur(gray, 5)
    edges = canny(blur, 50, 150)

    imshape = image.shape
    vertices = np.array([[
        (0, imshape[0]),
        (imshape[1], imshape[0]),
        (imshape[1]//2, imshape[0]//2)
    ]], dtype=np.int32)

    masked_edges = region_of_interest(edges, vertices)
    line_image = hough_lines(masked_edges, rho=2, theta=np.pi/180, threshold=50, min_line_len=40, max_line_gap=100)
    result = weighted_img(line_image, image)
    
    # Convert grayscale to RGB for consistent display
    gray_rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    
    return {
        'original': original,
        'grayscale': gray_rgb,
        'canny': edges_rgb,
        'hough': line_image,
        'final': result
    }
