# 🚀 Setup Guide - Lane Detection System

Quick setup instructions to get the project running on your machine.

## Prerequisites

- **Python 3.8+** installed ([Download Python](https://www.python.org/downloads/))
- **Git** installed ([Download Git](https://git-scm.com/))
- **ffmpeg** (required for video processing)

## Install FFmpeg

### Windows
```bash
# Using Chocolatey
choco install ffmpeg

# Or download from: https://ffmpeg.org/download.html
```

### macOS
```bash
brew install ffmpeg
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

## Installation Steps

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/lane-detection-system.git
cd CV-LAB-MID
```

### Step 2: Create Virtual Environment

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Upgrade pip
```bash
pip install --upgrade pip setuptools wheel
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install moviepy==1.0.3 opencv-python pillow imageio imageio-ffmpeg numpy
```

### Step 5: Verify Installation
```bash
# Test imports
python -c "from lane_functions import process_image; print('✓ Lane functions OK')"
python -c "from moviepy.editor import VideoFileClip; print('✓ MoviePy OK')"
python -c "import cv2; print('✓ OpenCV OK')"
```

## Running the Project

### Option 1: GUI Application (Recommended for Users)
```bash
python main.py
```

**What you'll see:**
- 🏠 Home tab with project information
- ⚙️ Processing tab showing 5 step visualization
- 🖼️ Load Image button to process images
- 🎬 Process Video button to process videos
- 📊 Information panel with live logs

### Option 2: Jupyter Notebook (Recommended for Learning)
```bash
jupyter notebook Lane_Detection.ipynb
```

**Benefits:**
- Step-by-step learning
- Experiment with parameters
- Visualize intermediate results
- Educational approach

### Option 3: Command Line Usage
```python
from lane_functions import process_image, process_image_with_steps
import cv2

# Load and process image
img = cv2.imread('test_images/solidWhiteRight.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Get all steps
steps = process_image_with_steps(img_rgb)
print(steps.keys())  # original, grayscale, canny, hough, final

# Or just final result
result = process_image(img_rgb)
```

## 📂 Project Structure

```
lane-detection-system/
├── README.md                      ← Read this first!
├── SETUP.md                       ← You are here
├── requirements.txt               ← Dependencies
├── .gitignore                     ← Git ignore rules
│
├── main.py                        ← RUN THIS (GUI App)
├── lane_functions.py              ← Core algorithms
├── Lane_Detection.ipynb           ← Jupyter notebook
│
├── test_images/                   ← Sample images
│   ├── solidWhiteRight.jpg
│   ├── solidYellowLeft.jpg
│   └── challenge.jpg
│
├── test_videos/                   ← Sample videos
│   ├── solidWhiteRight.mp4
│   ├── solidYellowLeft.mp4
│   └── challenge.mp4
│
├── test_images_output/            ← Processed images (auto-created)
└── test_videos_output/            ← Processed videos (auto-created)
```

## 🎯 First Steps

### For GUI Users:
1. Run: `python main.py`
2. Click "🏠 Home" tab to learn about lane detection
3. Click "🖼️ Load Image" to process a sample image
4. View all 5 processing steps in "⚙️ Processing" tab
5. Click "🔍 Maximize" to see each step in detail

### For Jupyter Users:
1. Run: `jupyter notebook Lane_Detection.ipynb`
2. Follow the cells in order
3. Run code to see results
4. Modify parameters and experiment
5. Learn the algorithms step-by-step

### For Python Developers:
1. Import from `lane_functions.py`
2. Use `process_image()` for simple processing
3. Use `process_image_with_steps()` for detailed steps
4. Integrate into your own projects

## 🔧 Troubleshooting

### Error: `ModuleNotFoundError: No module named 'moviepy'`
```bash
# Reinstall moviepy
pip install moviepy==1.0.3 --no-cache-dir
```

### Error: `No module named 'cv2'`
```bash
# Install OpenCV
pip install opencv-python
```

### Error: `FileNotFoundError: ffmpeg`
```bash
# Install ffmpeg (see "Install FFmpeg" section above)
```

### GUI doesn't open
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows

# Then run again
python main.py
```

### Video playback is slow
- Use a shorter video
- Reduce video resolution
- Close other applications

## 💡 Tips

1. **Keep test files organized** - Store images/videos in `test_images/` and `test_videos/`

2. **Use the Information Panel** - Check the left panel for processing logs

3. **Try sample videos first** - Start with `solidWhiteRight.mp4` before complex videos

4. **Experiment with parameters** - Edit `lane_functions.py` to tune detection sensitivity

5. **Save outputs** - Processed files are automatically saved to output folders

## 📊 Understanding the Output

### For Images:
- **Input**: Original image file
- **Output**: Image with red lane lines detected
- **Saved to**: `test_images_output/`

### For Videos:
- **Input**: Video file
- **Processing**: Lane detection applied to every frame
- **Output**: Video with lane detection overlay
- **Saved to**: `test_videos_output/`

## 🤝 Customization

### Change Detection Parameters

Edit `lane_functions.py` in `process_image_with_steps()`:

```python
# Canny edge detection thresholds
edges = canny(blur, 50, 150)  # Lower = more edges detected

# Hough line parameters
line_image = hough_lines(masked_edges, 
    rho=2,              # Distance resolution
    theta=np.pi/180,    # Angle resolution  
    threshold=50,       # Votes needed to detect line
    min_line_len=40,    # Minimum line length
    max_line_gap=100)   # Maximum gap allowed
```

### Change GUI Colors

Edit `main.py` color definitions:

```python
self.bg_dark = "#0a0e27"        # Background
self.accent_cyan = "#00d4ff"    # Highlights
self.accent_pink = "#ff006e"    # Buttons
```

## ✅ Verification Checklist

- [ ] Python 3.8+ installed
- [ ] Git cloned repository
- [ ] Virtual environment created and activated
- [ ] `pip install -r requirements.txt` completed
- [ ] FFmpeg installed
- [ ] `python main.py` runs without errors
- [ ] Can load sample image
- [ ] Can process sample video
- [ ] All processing steps visible

## 📚 Next Steps

1. **Read README.md** - Full documentation
2. **Run GUI** - Interactive exploration
3. **Try Jupyter Notebook** - Learn concepts
4. **Modify parameters** - Experiment with settings
5. **Use in your project** - Import and integrate functions

## 🆘 Getting Help

1. Check the **Troubleshooting** section above
2. Review the **Information Panel** in the GUI
3. Check **Lane_Detection.ipynb** for examples
4. Create an issue on GitHub
5. Read **README.md** for more details

## 🚀 You're All Set!

Everything is configured. Now:

```bash
# Activate virtual environment
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows

# Run the application
python main.py
```

**Happy Lane Detecting! 🛣️✨**
