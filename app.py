
import streamlit as st  
import io
import os
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont

# --- Configuration ---
IMAGES_FOLDER = "images"
VOICE_FILE = "birthday_voice.mp3"

# Optional: Password protection (uncomment to enable)
# APP_PASSWORD = "yourpassword"  # Change this to your chosen password
# pwd = st.text_input("Enter the password to open this app:", type="password")
# if pwd != APP_PASSWORD:
#     st.stop()
# ----------------------

# Page Settings
st.set_page_config(
    page_title="Birthday Greeting App",  
    layout="centered"
)

# Sidebar for customization
st.sidebar.header("Customize Your Greeting 🎨")
recipient_name = st.sidebar.text_input("Birthday person's name:", value="Alex")
your_name = st.sidebar.text_input("Your name:", value="Friend")

# Header
st.title(f"Happy Birthday {recipient_name}! 🎉")  
st.write(
    f"A personalized birthday greeting web app built with Python and Streamlit. "
    f"Customize the message, add photos, generate voice greetings, and create e-cards! 💙"
)

st.write("---")

st.header("Birthday Message")
message = st.text_area(
    "Write your personalized message here:",
    value=f"Happy Birthday {recipient_name}! 🥳\n\nWishing you an amazing day filled with joy, laughter, and wonderful memories. You deserve all the happiness in the world!\n\nWith love,\n{your_name}",
    height = 150,
)

st.subheader("Message Preview:")
st.success(message)

# Gallery of images
st.write("---")
st.header("Photo Gallery 📸")

images = []

# check if folder exists
if os.path.isdir(IMAGES_FOLDER):
    for filename in sorted(os.listdir(IMAGES_FOLDER)):
        if filename.lower().endswith((".png",".jpg",".jpeg")):
            images.append(os.path.join(IMAGES_FOLDER, filename))

if images:
    for i in range(0, len(images), 2):
        col1, col2 = st.columns(2)
        with col1:
            st.image(images[i])
        if i + 1 < len(images):
            with col2:
                st.image(images[i + 1])
        st.write("")  # Add space between rows
else:
    st.info("Add some pictures into the 'images' folder to show them here.")

# Generate voice message
st.write("---")
st.header("Voice Message Generator 🎤")
default_tts_text = (
    f"Happy Birthday {recipient_name}! Wishing you a fantastic day filled with joy, laughter, and all the things that make you smile. "
    f"May this year bring you success, happiness, and wonderful memories. Have an amazing birthday! "
    f"From {your_name}."
)

tts_text = st.text_area(
    "Text to convert to voice:",
    value=default_tts_text,
    height=120,
)

if st.button("Generate Voice Message 🎤"):
    tts = gTTS(text=tts_text, lang='en')
    tts.save(VOICE_FILE)
    st.success("Voice message generated! Play it below 👇")

    # read and play yhe mp3
    with open(VOICE_FILE, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes)

st.write("Or, if you recorded your own voice, you can upload it here:")
uploaded = st.file_uploader("Upload a voice file (mp3/wav/m4a)", type=["mp3", "wav", "m4a"])
if uploaded is not None:
    st.success("Got your file! Playing it:")
    st.audio(uploaded.read())

# E-CARD Generator
st.write("---")
st.header("Create and download a Birthday E-Card 🎂")


# User inputs for the card
card_headline = st.text_input("Card headline", value=f"Happy Birthday, {recipient_name}!")
card_subtext = st.text_input("Card subtext", value=f"With love, {your_name}")
card_width = st.slider("Card width (px)", 400, 1200, 900)
card_height = st.slider("Card height (px)", 200, 900, 500)

# Background color presets
bg_choice = st.selectbox("Background color", ["Midnight Blue", "Soft Purple", "Light Cream", "Forest Green"])
bg_map = {
    "Midnight Blue": (30, 35, 60),
    "Soft Purple": (95, 78, 160),
    "Light Cream": (250, 245, 230),
    "Forest Green": (22, 80, 44),
}
bg_color = bg_map.get(bg_choice, (30, 35, 60))

# Option to include first image from images folder
include_photo = False
first_image_path = None
if os.path.isdir(IMAGES_FOLDER):
    img_files = [f for f in sorted(os.listdir(IMAGES_FOLDER)) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    if img_files:
        include_photo = st.checkbox(f"Include first photo from `{IMAGES_FOLDER}/` ({img_files[0]})", value=True)
        if include_photo:
            first_image_path = os.path.join(IMAGES_FOLDER, img_files[0])

# Choose font size (relative)
headline_size = int(card_height * 0.12)
subtext_size = int(card_height * 0.06)

# Create the card in memory when user clicks
if st.button("Create e-card"):
    # Create blank card
    card = Image.new("RGB", (card_width, card_height), bg_color)
    draw = ImageDraw.Draw(card)

    # Try to load a TTF font; fallback to default if not found
    try:
        font_head = ImageFont.truetype("arial.ttf", headline_size)
        font_sub = ImageFont.truetype("arial.ttf", subtext_size)
    except Exception:
        font_head = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    # Draw headline (centered)
    bbox = draw.textbbox((0, 0), card_headline, font=font_head)
    w_head = bbox[2] - bbox[0]
    h_head = bbox[3] - bbox[1]
    draw.text(((card_width - w_head) / 2 + 50, card_height * 0.30), card_headline, font=font_head, fill=(255, 230, 150))

    # Draw subtext (centered near bottom-right area)
    bbox2 = draw.textbbox((0, 0), card_subtext, font=font_sub)
    w_sub = bbox2[2] - bbox2[0]
    h_sub = bbox2[3] - bbox2[1]
    draw.text(((card_width - w_sub) / 2, card_height * 0.75), card_subtext, font=font_sub, fill=(240, 240, 240))

    # Optional: paste first photo as a rounded thumbnail (left side)
    if first_image_path:
        try:
            im0 = Image.open(first_image_path).convert("RGBA")
            # Resize keeping aspect ratio
            thumb_w = int(card_width * 0.28)
            im0.thumbnail((thumb_w, int(card_height * 0.5)))
            # Simple paste: place on left, vertically centered
            paste_x = int(card_width * 0.03)
            paste_y = int((card_height - im0.height) / 2)
            # If image has alpha, composite; otherwise paste directly
            if im0.mode == "RGBA":
                card.paste(im0, (paste_x, paste_y), im0)
            else:
                card.paste(im0, (paste_x, paste_y))
        except Exception as e:
            st.warning(f"Could not include image: {e}")

    # Convert to bytes and show + download
    buf = io.BytesIO()
    card.save(buf, format="PNG")
    buf.seek(0)

    st.image(buf, caption="E-card preview")
    st.download_button("Download e-card (PNG)", data=buf, file_name="ecard.png", mime="image/png")

    

# Fun interaction
st.write("---") 
st.header("How are you feeling? 🎈")

feeling = st.selectbox(
    "What's your mood while creating this?",
    ["Excited! 😄", "Happy and creative 🎨", "Thoughtful 💭", "Filled with love ❤️", "Super proud! 🌟"]
)

st.write(f"{your_name} is feeling **{feeling}** while creating this special greeting!")