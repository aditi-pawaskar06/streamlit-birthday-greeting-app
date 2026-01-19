# 🎉 Birthday Greeting Web App

A personalized birthday greeting web application built with Python and Streamlit. Create custom birthday messages, photo galleries, voice greetings, and downloadable e-cards!

## ✨ Features

- **🎨 Customizable Names**: Enter the birthday person's name and your name in the sidebar
- **💬 Birthday Message Editor**: Write and preview personalized birthday messages
- **📸 Photo Gallery**: Display your favorite photos in a beautiful 2-column grid layout
- **🎤 Voice Message Generator**: Convert text to speech and generate audio birthday greetings
- **🎂 E-Card Creator**: Design and download custom birthday e-cards with:
  - Multiple background color themes
  - Customizable dimensions
  - Option to include photos
  - Adjustable text and styling
- **🔒 Optional Password Protection**: Protect your greeting with a password (optional feature)
- **📱 Mobile Responsive**: Works great on both desktop and mobile devices

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone this repository** (or download the ZIP file):
```bash
git clone <your-repo-url>
cd birthday-greeting-app
```

2. **Install required packages**:
```bash
pip install -r requirements.txt
```

3. **Add your photos** (optional):
   - Create an `images` folder in the project directory if it doesn't exist
   - Add your photos (PNG, JPG, or JPEG format)
   - Photos will automatically display in the gallery

4. **Run the application**:
```bash
streamlit run app.py
```

5. **Open your browser**:
   - The app should automatically open at `http://localhost:8501`
   - If not, navigate to that URL manually

## 🌐 Deploy to Streamlit Cloud (Free Hosting!)

You can deploy this app for free on Streamlit Community Cloud and share it with anyone via a public URL!

### Deployment Steps:

1. **Push your code to GitHub**:
   - Create a new GitHub repository
   - Push your code (make sure to remove personal photos first!)
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io/)
   - Sign in with your GitHub account
   - Click **"New app"**
   - Select your repository, branch (main), and main file path (`app.py`)
   - Click **"Deploy"**!

3. **Your app will be live** at: `https://<your-app-name>.streamlit.app`

4. **Add photos after deployment** (optional):
   - You can still add the `images/` folder to your repo
   - Or users can fork and add their own photos

### Important Notes for Deployment:
- Remove any personal/private photos before pushing to GitHub
- The free tier has resource limits (sufficient for this app)
- The app will sleep after inactivity but wakes up quickly when accessed
- You can make the repo private and still deploy (requires Streamlit Cloud authentication)

## 📝 How to Use

### 1. Customize Names
- Open the **sidebar** (click the arrow in the top-left if collapsed)
- Enter the birthday person's name
- Enter your name
- All messages will automatically update!

### 2. Write Your Message
- Edit the birthday message in the text area
- Preview appears below in a success box
- The message updates in real-time

### 3. Add Photos
- Place photos in the `images/` folder
- Supported formats: PNG, JPG, JPEG
- Photos display automatically in a 2-column grid
- Images are sorted alphabetically by filename

### 4. Generate Voice Message
- Edit the voice message text (or use the default)
- Click **"Generate Voice Message 🎤"**
- Listen to the generated audio
- Optionally upload your own voice recording

### 5. Create E-Card
- Customize the headline and subtext
- Adjust card dimensions with sliders
- Choose a background color theme
- Optionally include a photo from your gallery
- Click **"Create e-card"** to generate
- Download the PNG file

## 🎨 Customization Options

### Enable Password Protection
1. Open `app.py` in a text editor
2. Find the configuration section (lines 11-15)
3. Uncomment the password protection code:
```python
APP_PASSWORD = "yourpassword"  # Set your password
pwd = st.text_input("Enter the password to open this app:", type="password")
if pwd != APP_PASSWORD:
    st.stop()
```
4. Change `"yourpassword"` to your desired password
5. Save and restart the app

### Customize Default Values
You can modify default values in `app.py`:
- **Default names**: Change `value="Alex"` and `value="Friend"` in sidebar inputs
- **Default messages**: Edit the text in `value=` parameters
- **E-card colors**: Add more options to the `bg_map` dictionary
- **Image folder**: Change `IMAGES_FOLDER = "images"` to a different path

## 📦 Project Structure

```
birthday-greeting-app/
│
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── images/               # Folder for photos (create this)
│   └── (your photos here)
└── birthday_voice.mp3    # Generated voice file (auto-created)
```

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)**: Web app framework
- **[gTTS](https://gtts.readthedocs.io/)**: Google Text-to-Speech for voice generation
- **[Pillow (PIL)](https://pillow.readthedocs.io/)**: Image processing for e-cards
- **Python**: Core programming language

## 📋 Requirements

See `requirements.txt` for specific versions:
- streamlit
- Pillow
- gTTS
- imageio

## 🎯 Tips

- **For best photo display**: Use landscape-oriented images (horizontal)
- **E-card fonts**: The app uses Arial by default. If not available, it falls back to a system font
- **Voice generation**: Requires internet connection for gTTS to work
- **File names**: Photos display in alphabetical order based on filename

## 🐛 Troubleshooting

**Voice generation not working?**
- Ensure you have an internet connection
- Check if gTTS is properly installed: `pip install gTTS --upgrade`

**Images not showing?**
- Verify images are in the `images/` folder
- Check file extensions (must be .png, .jpg, or .jpeg)
- Try refreshing the page

**E-card fonts look wrong?**
- The app uses Arial font by default
- If Arial isn't available, it uses the system default
- On some systems, this might look different

## 📄 License

This project is open source and available for personal and educational use.

## 🤝 Contributing

Feel free to fork this project and customize it for your needs! If you make improvements, consider sharing them back with the community.

## 💡 Ideas for Enhancement

- Add more e-card templates and themes
- Support for multiple languages
- Video message upload
- Birthday countdown timer
- Share via email or social media
- Multiple photo upload interface
- Animated e-cards (GIF support)

---

**Made with ❤️ using Python and Streamlit**

Enjoy creating personalized birthday greetings! 🎂🎈
