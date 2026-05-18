# Quick Start Guide 🚀

## 30-Second Setup

```bash
# 1. Clone
git clone https://github.com/yourusername/lane-detection-system.git
cd CV-LAB-MID

# 2. Setup
python3 -m venv venv
source venv/bin/activate  # Linux/macOS or venv\Scripts\activate on Windows
pip install -r requirements.txt

# 3. Run
python main.py
```

## What You Get

| Component | Purpose | How to Use |
|-----------|---------|-----------|
| **main.py** | GUI App | `python main.py` |
| **P1.ipynb** | Jupyter Notebook | `jupyter notebook P1.ipynb` |
| **lane_functions.py** | Core Functions | `from lane_functions import process_image` |

## Features

✅ **Image Processing** - Load images → See all 5 detection steps
✅ **Video Processing** - Process videos → Built-in player with controls  
✅ **Interactive GUI** - Dark theme, professional design
✅ **Multi-Step Visualization** - Original → Grayscale → Canny → Hough → Final
✅ **Auto-Save** - Saves processed images and videos automatically
✅ **Real-time Player** - Play/Pause/Seek video controls

## File Overview

```
📁 CV-LAB-MID/
├─ 📄 README.md              Full documentation
├─ 📄 SETUP.md               Detailed setup instructions  
├─ 📄 requirements.txt       Python packages needed
├─ 🐍 main.py                GUI application (RUN THIS!)
├─ 🐍 lane_functions.py      Core algorithms
├─ 📓 P1.ipynb               Jupyter notebook
├─ 📁 test_images/           Sample images
├─ 📁 test_videos/           Sample videos
└─ 📁 test_*_output/         Processed results (auto-created)
```

## Ready to Use? Choose Your Path:

### 👤 User - I want to use the GUI
```bash
python main.py
# Click "Load Image" or "Process Video"
# Click "Maximize" to see each step
```

### 🎓 Student - I want to learn
```bash
jupyter notebook P1.ipynb
# Follow the cells to understand the algorithm
# Experiment with parameters
```

### 💻 Developer - I want to integrate
```python
from lane_functions import process_image, process_image_with_steps
import cv2

img = cv2.imread('image.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
result = process_image(img_rgb)
```

## Need Help?

1. **Installation issues?** → See `SETUP.md`
2. **Want full docs?** → See `README.md`
3. **Learning the concepts?** → Open `P1.ipynb`
4. **Getting started?** → You're reading it! 👈

## System Requirements

- Python 3.8+
- 500MB disk space
- FFmpeg (for video processing)

## Key Concepts

The system detects lane markings using:

1. **Grayscale** - Convert to single channel
2. **Blur** - Reduce noise
3. **Canny** - Detect edges
4. **ROI** - Focus on road area
5. **Hough** - Find lines
6. **Overlay** - Show results

That's it! 6 simple steps to detect lanes. 🛣️

---

**All set? Run `python main.py` and start detecting lanes! 🎉**
