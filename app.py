
import streamlit as st  # 1️⃣ import the streamlit library
import io
import os
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont

# --- simple password gate (optional) ---
# set a password here, tell Darsh the password separately
APP_PASSWORD = "mine"  # change this to something you choose

pwd = st.text_input("Enter the password to open this app:", type="password")
if pwd != APP_PASSWORD:
    st.stop()
# ---------------------------------------

HIS_NAME = "Darsh"
ME = "Aditi"
IMAGES_FOLDER = "images"
VOICE_FILE = "birthday_voice.mp3"

# Page Settings
st.set_page_config(
    page_title=f"Happy Birthday {HIS_NAME}!",  
    layout="centered"
)

# Header
st.title(f"Happy Birthday {HIS_NAME}! 🎉")  
st.write(
    f"This is a small web app i built just for you using Python. "
    f"I'm still learning, but I wanted to make something personal and special for you. 💙 — {ME}"
)

st.write("---")

st.header("My birthday message to you")
message = st.text_area(
    "Write your message here: ",
    value=f"Happy Birthday {HIS_NAME}! 🥳\n\nI’m really proud of the person you are, and even more proud to have you in my life.\nI miss you — a little extra today. — {ME}",
    height = 150,
)

st.subheader("Preview of what he'll read:")
st.success(message)
st.write("And yes… you definitely owe me a big hug for this 😌💙")

# Gallerly of images
st.write("---")
st.header("Some memories with you 💙")

images = []

# check if folder exists
if os.path.isdir(IMAGES_FOLDER):
    for filename in sorted(os.listdir(IMAGES_FOLDER)):
        if filename.lower().endswith((".png",".jpg",".jpeg")):
            images.append(os.path.join(IMAGES_FOLDER, filename))

if images:
    st.image(images, width=300, caption=[os.path.basename(img) for img in images])
else:
    st.info("Add some pictures into the 'images' folder to show them here.")

# Generate voice message
st.write("---")
default_tts_text = (
    f"Happy Birthday {HIS_NAME}! Even from miles away, you’re the part of my day that feels warm and steady. I hope today gives you the happiness, comfort, and love you truly deserve. "
    f"I miss you, and "
    f"I’m proud of you — more than you know. - {ME}"
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

# st.write("Or, if you recorded your own voice, you can upload it here:")

# uploaded = st.file_uploader("Upload a voice file (mp3/wav/m4a)", type=["mp3", "wav", "m4a"])
# if uploaded is not None:
#     st.success("Got your file! Playing it:")
#     st.audio(uploaded.read())

# E-CARD Generator
st.write("---")
st.header("Create and download a Birthday E-Card 🎂")


# User inputs for the card
card_headline = st.text_input("Card headline", value=f"Happy Birthday, {HIS_NAME}!")
card_subtext = st.text_input("Card subtext", value=f"With all my love, Aditi, {ME}")
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

    st.image(buf, caption="E-card preview", use_column_width=True)
    st.download_button("Download e-card (PNG)", data=buf, file_name="ecard.png", mime="image/png")

    

# little interaction
st.write("---") 
st.header("A little interaction part for you🎈")

feeling = st.selectbox(
    "How are you feeling while making this?",
    ["excited", "shy", "nervous but happy", "super proud of myself"]
)

st.write(f"Right now, {ME} is feeling **{feeling}** while learning Python for you 💻.")