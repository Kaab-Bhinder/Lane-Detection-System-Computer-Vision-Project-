# 🛣️ Lane Detection System

A comprehensive computer vision project for detecting lane markings on roads using OpenCV, ideal for autonomous vehicles and driver assistance systems.

## 📋 Overview

This project implements an advanced lane detection system that processes both **images** and **videos** using classical computer vision techniques. It features a modern GUI application with real-time video playback and multi-step visualization of the detection pipeline.

## ✨ Features

- 🖼️ **Image Processing** - Load and process images with complete pipeline visualization
- 🎬 **Video Processing** - Process entire video files with lane detection applied to every frame
- 🎮 **Interactive GUI** - Modern dark-themed interface with Tkinter
- 📺 **Video Player** - Built-in video player with play/pause/seek controls
- 🔍 **Multi-Step Visualization** - See all 5 processing steps: Original → Grayscale → Canny → Hough → Final
- 💾 **Auto-Save** - Automatically saves processed images and videos
- 📊 **Live Information Panel** - Real-time processing logs and updates
- 🎨 **Professional Colors** - Dark modern theme with professional color scheme

## 🛠️ Tech Stack

- **Python 3.8+**
- **OpenCV** - Image processing
- **MoviePy** - Video processing
- **Pillow (PIL)** - Image display
- **Tkinter** - GUI framework
- **NumPy** - Numerical operations

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/lane-detection-system.git
cd CV-LAB-MID
```

### Step 2: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install moviepy pillow opencv-python imageio imageio-ffmpeg numpy
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

## 🚀 Quick Start

### Running the GUI Application
```bash
./venv/bin/python main.py
```

Or on Windows:
```bash
venv\Scripts\python main.py
```

## 📁 Project Structure

```
CV-LAB-MID/
├── main.py                      # Main GUI application (run this!)
├── lane_functions.py            # Core lane detection functions
├── Lane_Detection.ipynb         # Jupyter notebook for analysis
├── test_images/                 # Sample images for testing
│   ├── solidWhiteRight.jpg
│   ├── solidYellowLeft.jpg
│   └── challenge.jpg
├── test_videos/                 # Sample videos for testing
│   ├── solidWhiteRight.mp4
│   ├── solidYellowLeft.mp4
│   └── challenge.mp4
├── test_images_output/          # Output folder for processed images
├── test_videos_output/          # Output folder for processed videos
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 🎯 Usage Guide

### Method 1: GUI Application (Recommended)
```bash
./venv/bin/python main.py
```

**Features:**
- 🏠 **Home Tab** - Learn about lane detection concepts
- ⚙️ **Processing Tab** - View all 5 processing steps
- 🖼️ **Load Image** - Process individual images
- 🎬 **Process Video** - Process video files with real-time player
- 🔍 **Maximize** - View each processing step in full screen
- 📊 **Information Panel** - Live processing updates

### Method 2: Jupyter Notebook
```bash
jupyter notebook Lane_Detection.ipynb
```

Great for:
- Learning the concepts step-by-step
- Experimenting with parameters
- Analyzing results in detail
- Educational purposes

### Method 3: Python Script
```bash
from lane_functions import process_image, process_image_with_steps
import cv2

# Load image
img = cv2.imread('test_images/solidWhiteRight.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Get all processing steps
steps = process_image_with_steps(img_rgb)
# steps contains: original, grayscale, canny, hough, final

# Or just get final result
result = process_image(img_rgb)
```

## 🧠 Lane Detection Pipeline

The system uses 6 key computer vision techniques:

### 1. **Grayscale Conversion**
- Converts RGB to single-channel grayscale
- Reduces data while preserving intensity
- Improves processing speed

### 2. **Gaussian Blur**
- Smooths image to reduce noise
- Removes small details and artifacts
- Prepares image for edge detection

### 3. **Canny Edge Detection**
- Identifies edges where intensity changes abruptly
- Uses gradient calculations (Sobel operators)
- Detects lane boundaries and road markings

### 4. **Region of Interest (ROI)**
- Focuses on relevant area (center of road)
- Removes sky, trees, and distractions
- Improves accuracy and processing speed

### 5. **Hough Line Transform**
- Detects straight lines in edge images
- Converts point coordinates to line parameters (ρ, θ)
- Robust to gaps and broken lines
- Efficient line detection in images

### 6. **Image Overlay**
- Combines detected lanes with original image
- Red lane lines overlaid on original
- Final result shows clear lane detection

## 📊 Processing Steps Visualization

When you load an image, you see:

```
Original Image
    ↓
Grayscale Conversion
    ↓
Gaussian Blur
    ↓
Canny Edge Detection
    ↓
Region of Interest Masking
    ↓
Hough Line Transform
    ↓
Image Overlay
    ↓
Final Result
```

## 🎮 GUI Features Explained

### Home Tab
- Overview of the lane detection system
- Explanation of all 6 concepts
- Usage instructions

### Processing Tab
Shows 5 visualization boxes:
1. **Original** - Input image (Dark Slate)
2. **Grayscale** - Converted to single channel (Steel Blue)
3. **Canny Edges** - Detected edges (Asbestos)
4. **Hough Lines** - Detected lane lines (Slate)
5. **Final Result** - Result overlaid on original (Navy Blue)

Each box has a **Maximize** button to view full-screen.

### Video Player
- Play/Pause/Stop controls
- Seek slider with time display
- Frame-by-frame playback
- Real-time FPS adjustment

## 📝 Sample Test Cases

### Images
Place test images in `test_images/`:
```
test_images/
├── solidWhiteRight.jpg    # Simple highway scene
├── solidYellowLeft.jpg    # Road with yellow lines
└── challenge.jpg          # Complex road scenario
```

### Videos
Place test videos in `test_videos/`:
```
test_videos/
├── solidWhiteRight.mp4    # Highway video
├── solidYellowLeft.mp4    # Road video
└── challenge.mp4          # Complex video
```

## 📤 Output Files

### Processed Images
Saved to `test_images_output/`:
- Original filename with lane detection applied
- Format: Original image with red lane lines overlay

### Processed Videos
Saved to `test_videos_output/`:
- Lane detection applied to every frame
- Same format as input video
- Audio removed (processing only)

## ⚙️ Configuration

To adjust detection parameters, edit `lane_functions.py`:

```python
# In process_image_with_steps():

# Canny edge detection thresholds
edges = canny(blur, 50, 150)  # Adjust 50 and 150

# Gaussian blur kernel size
blur = gaussian_blur(gray, 5)  # Adjust kernel size

# Hough line transform parameters
line_image = hough_lines(masked_edges, 
    rho=2,              # Distance resolution
    theta=np.pi/180,    # Angle resolution
    threshold=50,       # Vote threshold
    min_line_len=40,    # Minimum line length
    max_line_gap=100)   # Maximum gap in line
```

## 🐛 Troubleshooting

### Error: `ModuleNotFoundError: No module named 'moviepy'`
```bash
pip install moviepy --no-cache-dir
```

### Error: `No module named 'cv2'`
```bash
pip install opencv-python
```

### GUI doesn't appear
Make sure you have a display:
```bash
# Linux only
export DISPLAY=:0
./venv/bin/python main.py
```

### Video playback is slow
Reduce video resolution or lower the FPS

## 📚 Files Description

| File | Purpose |
|------|---------|
| `main.py` | Main GUI application - **RUN THIS** |
| `lane_functions.py` | Core algorithms and processing functions |
| `Lane_Detection.ipynb` | Jupyter notebook for learning/experimentation |
| `requirements.txt` | Python package dependencies |

## 🔧 Development

### Running Tests
```bash
# Test image processing
python -c "from lane_functions import process_image; print('OK')"

# Test all imports
./venv/bin/python -c "from moviepy.editor import VideoFileClip; import cv2; print('All packages OK')"
```

### Project Statistics
- **Lines of Code**: 500+
- **Functions**: 15+
- **Processing Steps**: 6
- **Supported Formats**: JPG, PNG, MP4, AVI, MOV, MKV

## 📖 Educational Value

Great for learning:
- Computer vision fundamentals
- Image processing techniques
- GUI development with Tkinter
- Video processing with MoviePy
- Software design patterns
- Python best practices

## 🤝 Contributing

Feel free to:
- Add more detection algorithms
- Improve lane tracking accuracy
- Add more GUI features
- Optimize performance
- Add more test cases

## 📄 License

MIT License - Feel free to use for educational and commercial projects.

## 👨‍💻 Author

Created as a Computer Vision lab project demonstrating practical applications of image and video processing techniques.

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the documentation
3. Check the information panel in the GUI
4. Create an issue on GitHub

## 🌟 Key Achievements

✅ Full image and video processing pipeline
✅ Professional GUI with dark theme
✅ Real-time video player
✅ Multi-step visualization
✅ Auto-save functionality
✅ Comprehensive documentation
✅ Easy to use and modify
✅ Educational and production-ready

## 🚀 Future Enhancements

Potential improvements:
- [ ] Real-time camera feed processing
- [ ] Deep learning-based detection
- [ ] Multi-lane tracking
- [ ] Curved lane detection
- [ ] Performance metrics display
- [ ] GPU acceleration support
- [ ] WebUI interface
- [ ] REST API backend

## 📋 Quick Reference

```bash
# Setup
git clone <repo>
cd CV-LAB-MID
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run GUI
./venv/bin/python main.py

# Run Notebook
jupyter notebook Lane_Detection.ipynb

# Test
./venv/bin/python -c "from lane_functions import process_image; print('OK')"
```

---

**Happy Lane Detecting! 🛣️✨**
