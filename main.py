from lane_functions import process_image, process_image_with_steps
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os
from moviepy.editor import VideoFileClip
import threading

# Ensure output folders exist
os.makedirs("test_images_output", exist_ok=True)
os.makedirs("test_videos_output", exist_ok=True)

class LaneDetectionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🛣️ Lane Detection System")
        self.root.geometry("1600x900")
        # Dark modern background
        self.root.config(bg="#0a0e27")
        
        # Color scheme
        self.bg_dark = "#0a0e27"
        self.bg_panel = "#16213e"
        self.accent_cyan = "#00d4ff"
        self.accent_pink = "#ff006e"
        self.accent_purple = "#8338ec"
        self.text_light = "#ffffff"
        
        # Set style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background=self.bg_dark)
        style.configure('Title.TLabel', font=('Helvetica', 24, 'bold'), background=self.bg_dark, 
                       foreground=self.accent_cyan)
        style.configure('Header.TLabel', font=('Helvetica', 12, 'bold'), background=self.bg_dark, 
                       foreground=self.accent_cyan)
        style.configure('TNotebook', background=self.bg_dark)
        style.configure('TNotebook.Tab', background=self.bg_panel, foreground=self.accent_cyan)
        style.map('TNotebook.Tab', background=[("selected", self.accent_cyan)], 
                 foreground=[("selected", self.bg_dark)])
        
        # Main frame
        main_frame = tk.Frame(root, bg=self.bg_dark, padx=15, pady=15)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title with separator
        title_label = tk.Label(main_frame, text="🛣️ Lane Detection System", 
                              font=('Helvetica', 24, 'bold'), bg=self.bg_dark, 
                              fg=self.accent_cyan)
        title_label.pack(pady=(0, 10))
        
        sep1 = tk.Frame(main_frame, bg=self.accent_cyan, height=2)
        sep1.pack(fill=tk.X, pady=(0, 15))
        
        # Content frame
        content_frame = tk.Frame(main_frame, bg=self.bg_dark)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # ========== LEFT PANEL ==========
        left_panel = tk.Frame(content_frame, bg=self.bg_panel, relief=tk.SUNKEN, bd=2)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10))
        
        # Control title
        control_title = tk.Label(left_panel, text="📋 Controls", font=('Helvetica', 12, 'bold'), 
                                bg=self.bg_panel, fg=self.accent_cyan)
        control_title.pack(pady=10, padx=10)
        
        sep2 = tk.Frame(left_panel, bg=self.accent_cyan, height=1)
        sep2.pack(fill=tk.X, padx=10, pady=5)
        
        # Image button
        self.btn_image = tk.Button(left_panel, text="🖼️ Load Image", command=self.load_image,
                                   font=('Helvetica', 11, 'bold'), bg=self.accent_cyan, 
                                   fg=self.bg_panel, padx=15, pady=12, cursor='hand2', 
                                   relief=tk.RAISED, bd=2, activebackground='#00ffff',
                                   activeforeground=self.bg_panel)
        self.btn_image.pack(pady=15, padx=15, fill=tk.X)
        
        # Video button
        self.btn_video = tk.Button(left_panel, text="🎬 Process Video", command=self.load_video,
                                   font=('Helvetica', 11, 'bold'), bg=self.accent_pink, 
                                   fg=self.text_light, padx=15, pady=12, cursor='hand2', 
                                   relief=tk.RAISED, bd=2, activebackground='#ff4081',
                                   activeforeground=self.text_light)
        self.btn_video.pack(pady=10, padx=15, fill=tk.X)
        
        # Info section
        sep3 = tk.Frame(left_panel, bg=self.accent_cyan, height=1)
        sep3.pack(fill=tk.X, padx=10, pady=10)
        
        info_title = tk.Label(left_panel, text="ℹ️ Information", font=('Helvetica', 12, 'bold'), 
                             bg=self.bg_panel, fg=self.accent_cyan)
        info_title.pack(pady=10, padx=10)
        
        info_frame = tk.Frame(left_panel, bg=self.bg_dark, relief=tk.SUNKEN, bd=1)
        info_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.info_text = tk.Text(info_frame, height=25, width=28, font=('Courier', 8),
                                bg=self.bg_dark, fg=self.accent_cyan, relief=tk.FLAT, bd=0, 
                                wrap=tk.WORD, insertbackground=self.accent_cyan)
        self.info_text.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(info_frame, orient=tk.VERTICAL, command=self.info_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.info_text.config(yscrollcommand=scrollbar.set, state=tk.DISABLED)
        self.add_info("Ready to process images or videos.")
        
        # ========== RIGHT PANEL ==========
        right_panel = tk.Frame(content_frame, bg=self.bg_panel, relief=tk.SUNKEN, bd=2)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Create notebook tabs
        self.notebook = ttk.Notebook(right_panel)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # ========== HOME TAB ==========
        home_tab = tk.Frame(self.notebook, bg=self.bg_panel)
        self.notebook.add(home_tab, text="🏠 Home")
        
        home_scroll = tk.Canvas(home_tab, bg=self.bg_panel, highlightthickness=0)
        home_scroll.pack(fill=tk.BOTH, expand=True)
        
        home_frame = tk.Frame(home_scroll, bg=self.bg_panel)
        home_scroll.create_window(0, 0, window=home_frame, anchor='nw', width=900)
        
        title_home = tk.Label(home_frame, text="🛣️ Lane Detection System", 
                             font=('Helvetica', 20, 'bold'), bg=self.bg_panel, fg=self.accent_cyan)
        title_home.pack(pady=20)
        
        intro_text = """
Lane Detection is a critical computer vision application used in autonomous 
vehicles, driver assistance systems, and road analysis. This system identifies 
lane markings on roads to help vehicles navigate safely.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 CONCEPTS USED:

1️⃣ GRAYSCALE CONVERSION
   • Converts RGB image to single channel
   • Reduces data while preserving intensity information
   • Faster processing and lower memory usage

2️⃣ GAUSSIAN BLUR
   • Smooths the image to reduce noise
   • Prepares image for edge detection
   • Removes small details and artifacts

3️⃣ CANNY EDGE DETECTION
   • Identifies edges where intensity changes abruptly
   • Uses gradient calculations
   • Detects lane boundaries and road markings

4️⃣ REGION OF INTEREST (ROI)
   • Focuses on the relevant area (center of road)
   • Removes sky, trees, and other irrelevant regions
   • Improves accuracy and speed

5️⃣ HOUGH LINE TRANSFORM
   • Detects straight lines in edge images
   • Converts points to line parameters (ρ, θ)
   • Robust to gaps and broken lines

6️⃣ IMAGE OVERLAY
   • Combines detected lanes with original image
   • Shows final lane marking detection
   • Visualizes results clearly

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📷 USAGE:

• Click "Load Image" to process and see all 5 steps
• Click "Process Video" to process videos
• Click "Maximize" to view in full screen
• Check the log panel for updates

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """
        
        intro_label = tk.Label(home_frame, text=intro_text, font=('Courier', 9), 
                              bg=self.bg_panel, fg=self.accent_cyan, justify=tk.LEFT)
        intro_label.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        # ========== PROCESSING TAB ==========
        processing_tab = tk.Frame(self.notebook, bg=self.bg_panel)
        self.notebook.add(processing_tab, text="⚙️ Processing")
        
        display_title = tk.Label(processing_tab, text="📺 Processing Steps", 
                                font=('Helvetica', 12, 'bold'), bg=self.bg_panel, fg=self.accent_cyan)
        display_title.pack(pady=10)
        
        sep_display = tk.Frame(processing_tab, bg=self.accent_cyan, height=1)
        sep_display.pack(fill=tk.X)
        
        grid_frame = tk.Frame(processing_tab, bg=self.bg_panel)
        grid_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.image_labels = {}
        self.photo_images = {}
        
        # ===== TOP ROW =====
        top_row = tk.Frame(grid_frame, bg=self.bg_panel)
        top_row.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        steps_top = [
            ('Original', 'original', '#2c3e50'),  # Dark slate
            ('Grayscale', 'grayscale', '#34495e'),  # Steel blue
            ('Canny Edges', 'canny', '#7f8c8d')  # Asbestos
        ]
        
        for step_name, step_key, color in steps_top:
            self._create_step_frame(top_row, step_name, step_key, color)
        
        # ===== BOTTOM ROW =====
        bottom_row = tk.Frame(grid_frame, bg=self.bg_panel)
        bottom_row.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        steps_bottom = [
            ('Hough Lines', 'hough', '#4a6fa5'),  # Slate
            ('Final Result', 'final', '#1a5490')  # Navy blue
        ]
        
        for step_name, step_key, color in steps_bottom:
            self._create_step_frame(bottom_row, step_name, step_key, color)
        
        # Progress bar
        self.progress = ttk.Progressbar(processing_tab, mode='indeterminate')
        self.progress.pack(padx=10, pady=5, fill=tk.X)
        
        # Status bar
        status_frame = tk.Frame(main_frame, bg=self.bg_dark)
        status_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.status_label = tk.Label(status_frame, text="✓ Ready", relief=tk.SUNKEN, 
                                    bg=self.bg_panel, fg=self.accent_cyan, font=('Courier', 9))
        self.status_label.pack(fill=tk.X)
        
        # Initialize variables
        self.current_file = None
        self.video_result_window = None
        self.is_playing = False
        self.current_video_path = None
        self.current_frame_index = 0
        self.total_frames = 0
        self.video_cap = None
        self.fps = 0
        
        # Display placeholder images
        self.show_placeholder_images()
    
    def _create_step_frame(self, parent, step_name, step_key, color):
        """Helper to create a step display frame"""
        frame = tk.Frame(parent, bg=color, relief=tk.SUNKEN, bd=2)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=3, pady=3)
        
        label_title = tk.Label(frame, text=step_name, font=('Helvetica', 9, 'bold'), 
                              bg=color, fg='#ffffff')
        label_title.pack(pady=3)
        
        img_button_frame = tk.Frame(frame, bg=self.bg_panel)
        img_button_frame.pack(padx=3, pady=2, fill=tk.BOTH, expand=True)
        
        img_label = tk.Label(img_button_frame, bg='#000000', text='', width=200, height=150, cursor='hand2')
        img_label.pack(fill=tk.BOTH, expand=True)
        img_label.bind('<Button-1>', lambda e, key=step_key: self.maximize_image(key))
        
        max_btn = tk.Button(frame, text='🔍 Maximize', font=('Helvetica', 7), bg=color, fg='#ffffff',
                           command=lambda key=step_key: self.maximize_image(key), relief=tk.RAISED, bd=1,
                           activebackground='#ffffff', activeforeground=color)
        max_btn.pack(pady=2, padx=3, fill=tk.X)
        
        self.image_labels[step_key] = img_label
        self.photo_images[step_key] = None
    
    def add_info(self, message):
        """Add message to info panel"""
        self.info_text.config(state=tk.NORMAL)
        self.info_text.insert(tk.END, f"• {message}\n")
        self.info_text.see(tk.END)
        self.info_text.config(state=tk.DISABLED)
    
    def update_status(self, message):
        """Update status bar"""
        self.status_label.config(text=message)
        self.root.update()
    
    def show_placeholder_images(self):
        """Display placeholder images"""
        placeholder_images = {
            'original': (np.ones((300, 400, 3), dtype=np.uint8) * 40, "Waiting for image...", (50, 150)),
            'grayscale': (np.ones((300, 400), dtype=np.uint8) * 40, "Grayscale", (120, 150)),
            'canny': (np.ones((300, 400), dtype=np.uint8) * 40, "Canny Edges", (110, 150)),
            'hough': (np.ones((300, 400, 3), dtype=np.uint8) * 40, "Hough Lines", (110, 150)),
            'final': (np.ones((300, 400, 3), dtype=np.uint8) * 40, "Final Result", (100, 150)),
        }
        
        for step_key, (img, text, pos) in placeholder_images.items():
            img_copy = img.copy()
            if len(img_copy.shape) == 2:
                img_copy = cv2.cvtColor(img_copy, cv2.COLOR_GRAY2RGB)
            cv2.putText(img_copy, text, pos, cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 100, 100), 2)
            self.display_image_at_step(step_key, img_copy)
    
    def load_image(self):
        """Load and process image"""
        path = filedialog.askopenfilename(
            title="Select an image",
            filetypes=[("Image files", "*.jpg *.png *.jpeg"), ("All files", "*.*")]
        )
        if not path:
            return
        
        try:
            self.update_status("⏳ Processing image...")
            self.progress.start()
            self.root.update()
            
            img = cv2.imread(path)
            if img is None:
                raise ValueError("Could not read image")
            
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            steps = process_image_with_steps(img_rgb)
            
            save_path = os.path.join("test_images_output", os.path.basename(path))
            cv2.imwrite(save_path, cv2.cvtColor(steps['final'], cv2.COLOR_RGB2BGR))
            
            self.display_all_steps(steps)
            self.notebook.select(1)
            
            self.progress.stop()
            filename = os.path.basename(path)
            self.add_info(f"Image processed: {filename}")
            self.update_status(f"✓ Image saved to test_images_output/{filename}")
            messagebox.showinfo("Success", f"Image saved to:\n{save_path}")
            
        except Exception as e:
            self.progress.stop()
            self.update_status("✗ Error processing image")
            self.add_info(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Failed to process image:\n{str(e)}")
    
    def load_video(self):
        """Load video for processing"""
        path = filedialog.askopenfilename(
            title="Select a video",
            filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv"), ("All files", "*.*")]
        )
        if not path:
            return
        
        thread = threading.Thread(target=self._process_video, args=(path,))
        thread.daemon = True
        thread.start()
    
    def _process_video(self, path):
        """Process video in background"""
        try:
            self.update_status("⏳ Processing video (this may take a while)...")
            self.progress.start()
            
            filename = os.path.basename(path)
            self.add_info(f"Video processing started: {filename}")
            
            clip = VideoFileClip(path)
            output_path = os.path.join("test_videos_output", filename)
            white_clip = clip.fl_image(process_image)
            white_clip.write_videofile(output_path, audio=False, verbose=False, logger=None)
            clip.close()
            
            self.progress.stop()
            self.add_info(f"Video processed successfully: {filename}")
            self.update_status(f"✓ Video saved to test_videos_output/{filename}")
            
            self.show_video_player(output_path, filename)
            messagebox.showinfo("Success", f"Video saved to:\n{output_path}\n\nNow playing in the video player!")
            
        except Exception as e:
            self.progress.stop()
            self.update_status("✗ Error processing video")
            self.add_info(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Failed to process video:\n{str(e)}")
    
    def display_all_steps(self, steps_dict):
        """Display all processing steps"""
        for step_name in ['original', 'grayscale', 'canny', 'hough', 'final']:
            self.display_image_at_step(step_name, steps_dict[step_name])
    
    def display_image_at_step(self, step_name, img_array):
        """Display image for specific step"""
        h, w = img_array.shape[:2]
        max_width, max_height = 280, 200
        
        if w > max_width or h > max_height:
            scale = min(max_width / w, max_height / h)
            new_w, new_h = int(w * scale), int(h * scale)
            img_array = cv2.resize(img_array, (new_w, new_h))
        
        img_pil = Image.fromarray(img_array)
        photo = ImageTk.PhotoImage(img_pil)
        
        self.image_labels[step_name].config(image=photo, text="")
        self.photo_images[step_name] = photo
    
    def maximize_image(self, step_name):
        """Open maximized image view in full tab"""
        if self.photo_images[step_name] is None:
            messagebox.showinfo("Info", "No image data available. Please load an image first.")
            return
        
        # Create new window
        max_window = tk.Toplevel(self.root)
        max_window.title(f"🔍 {step_name.upper()} - Full View")
        max_window.geometry("1200x900")
        max_window.config(bg=self.bg_dark)
        
        # Title bar
        title_frame = tk.Frame(max_window, bg=self.bg_panel, height=50)
        title_frame.pack(fill=tk.X, padx=0, pady=0)
        
        title_label = tk.Label(title_frame, text=f"📺 {step_name.upper()}", 
                              font=('Helvetica', 16, 'bold'), bg=self.bg_panel, fg=self.accent_cyan)
        title_label.pack(pady=10)
        
        # Separator
        sep = tk.Frame(max_window, bg=self.accent_cyan, height=2)
        sep.pack(fill=tk.X)
        
        # Full image display area
        img_frame = tk.Frame(max_window, bg='#000000', relief=tk.SUNKEN, bd=2)
        img_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        img_label = self.image_labels[step_name]
        large_img_label = tk.Label(img_frame, image=img_label.cget('image'), bg='#000000')
        large_img_label.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Button frame
        btn_frame = tk.Frame(max_window, bg=self.bg_panel)
        btn_frame.pack(fill=tk.X, padx=15, pady=15)
        
        close_btn = tk.Button(btn_frame, text="✕ Close", command=max_window.destroy,
                             font=('Helvetica', 11, 'bold'), bg='#e74c3c', fg='white', 
                             padx=30, pady=10, relief=tk.RAISED, bd=2,
                             activebackground='#c0392b', activeforeground='white')
        close_btn.pack(side=tk.RIGHT)
    
    def show_video_player(self, video_path, filename):
        """Show video player window"""
        if self.video_result_window is None or not self.video_result_window.winfo_exists():
            self.video_result_window = tk.Toplevel(self.root)
            self.video_result_window.title(f"🎬 Video Player - {filename}")
            self.video_result_window.geometry("900x750")
            self.video_result_window.config(bg=self.bg_dark)
            
            title_label = tk.Label(self.video_result_window, text=f"Playing: {filename}", 
                                  font=('Helvetica', 12, 'bold'), bg=self.bg_panel, fg=self.accent_cyan)
            title_label.pack(pady=10)
            
            self.video_display_label = tk.Label(self.video_result_window, bg='#000000', relief=tk.SUNKEN, bd=2)
            self.video_display_label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
            
            controls_frame = tk.Frame(self.video_result_window, bg=self.bg_panel)
            controls_frame.pack(fill=tk.X, padx=10, pady=10)
            
            self.video_slider = ttk.Scale(controls_frame, from_=0, to=100, orient=tk.HORIZONTAL)
            self.video_slider.pack(fill=tk.X, pady=5)
            self.video_slider.bind("<Button-1>", self.on_slider_click)
            
            self.time_label = tk.Label(controls_frame, text="00:00 / 00:00", font=('Courier', 9), 
                                      bg=self.bg_panel, fg=self.accent_cyan)
            self.time_label.pack()
            
            buttons_frame = tk.Frame(controls_frame, bg=self.bg_panel)
            buttons_frame.pack(pady=10)
            
            play_btn = tk.Button(buttons_frame, text="▶ Play", command=self.play_video,
                                font=('Helvetica', 10, 'bold'), bg='#4CAF50', fg='white', padx=15, pady=8)
            play_btn.pack(side=tk.LEFT, padx=5)
            
            pause_btn = tk.Button(buttons_frame, text="⏸ Pause", command=self.pause_video,
                                 font=('Helvetica', 10, 'bold'), bg='#FF9800', fg='white', padx=15, pady=8)
            pause_btn.pack(side=tk.LEFT, padx=5)
            
            stop_btn = tk.Button(buttons_frame, text="⏹ Stop", command=self.stop_video,
                                font=('Helvetica', 10, 'bold'), bg='#f44336', fg='white', padx=15, pady=8)
            stop_btn.pack(side=tk.LEFT, padx=5)
            
            self.current_video_path = video_path
            self.video_cap = cv2.VideoCapture(video_path)
            self.total_frames = int(self.video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
            self.fps = self.video_cap.get(cv2.CAP_PROP_FPS)
            self.current_frame_index = 0
            self.is_playing = False
            
            self.video_slider.config(to=self.total_frames)
            self.display_video_frame()
    
    def display_video_frame(self):
        """Display current video frame"""
        if self.video_cap is None or self.video_display_label is None:
            return
        
        try:
            self.video_cap.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame_index)
            ret, frame = self.video_cap.read()
            
            if ret and frame is not None:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img_pil = Image.fromarray(frame_rgb)
                
                label_width = self.video_display_label.winfo_width()
                label_height = self.video_display_label.winfo_height()
                
                if label_width < 50 or label_height < 50:
                    label_width, label_height = 880, 650
                
                img_pil.thumbnail((label_width - 10, label_height - 10), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img_pil)
                
                self.video_display_label.config(image=photo)
                self.video_display_label.image = photo
                
                if self.fps > 0:
                    total_seconds = int(self.total_frames / self.fps)
                    current_seconds = int(self.current_frame_index / self.fps)
                    minutes, seconds = divmod(current_seconds, 60)
                    total_minutes, total_secs = divmod(total_seconds, 60)
                    self.time_label.config(text=f"{minutes:02d}:{seconds:02d} / {total_minutes:02d}:{total_secs:02d}")
                
                self.video_slider.set(self.current_frame_index)
                self.root.update_idletasks()
        except Exception as e:
            print(f"Error displaying frame: {e}")
    
    def play_video(self):
        """Play video"""
        if self.video_cap is None or self.video_result_window is None:
            return
        
        self.is_playing = True
        self.play_next_frame()
    
    def play_next_frame(self):
        """Play next frame"""
        if not self.is_playing or self.video_cap is None or self.video_result_window is None:
            return
        
        try:
            if self.current_frame_index < self.total_frames - 1:
                self.current_frame_index += 1
                self.display_video_frame()
                delay = max(1, int(1000 / self.fps)) if self.fps > 0 else 33
                if self.video_result_window.winfo_exists():
                    self.video_result_window.after(delay, self.play_next_frame)
            else:
                self.is_playing = False
        except Exception as e:
            self.is_playing = False
            print(f"Error playing video: {e}")
    
    def pause_video(self):
        """Pause video"""
        self.is_playing = False
    
    def stop_video(self):
        """Stop video"""
        self.is_playing = False
        self.current_frame_index = 0
        self.display_video_frame()
    
    def on_slider_click(self, event):
        """Handle slider click"""
        if self.video_cap is None or self.total_frames == 0:
            return
        
        self.is_playing = False
        try:
            slider_width = self.video_slider.winfo_width()
            if slider_width > 1:
                click_pos = event.x
                self.current_frame_index = int((click_pos / slider_width) * self.total_frames)
                self.current_frame_index = max(0, min(self.current_frame_index, self.total_frames - 1))
                self.display_video_frame()
        except Exception as e:
            print(f"Error seeking video: {e}")

import numpy as np

if __name__ == "__main__":
    root = tk.Tk()
    app = LaneDetectionGUI(root)
    root.mainloop()
