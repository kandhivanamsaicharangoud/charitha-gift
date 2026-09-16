import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(
    page_title="A Special Surprise ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


def get_base64(path):
    with open(path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")


# -----------------------------
# FILE PATHS
# -----------------------------

photo1_path = "assets/charitha1.jpg"
photo2_path = "assets/charitha2.jpg"
song_path = "assets/jo tum mereho.mpeg"


# -----------------------------
# CHECK FILES
# -----------------------------

for file_path in [photo1_path, photo2_path, song_path]:
    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}")
        st.stop()


# -----------------------------
# CONVERT FILES TO BASE64
# -----------------------------

photo1 = get_base64(photo1_path)
photo2 = get_base64(photo2_path)
song = get_base64(song_path)


# -----------------------------
# HTML + CSS + JAVASCRIPT
# -----------------------------

html_code = f"""
<!DOCTYPE html>
<html>

<head>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>

* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    padding: 0;

    font-family: Arial, sans-serif;

    background:
        radial-gradient(circle at top left, #ff5fa2, transparent 35%),
        radial-gradient(circle at bottom right, #7b2cff, transparent 35%),
        linear-gradient(135deg, #14001f, #25002e, #080014);

    color: white;

    min-height: 100vh;
    overflow-x: hidden;
}}


/* MAIN PAGE */

.page {{
    min-height: 750px;

    display: flex;
    justify-content: center;
    align-items: center;

    padding: 30px 15px;

    position: relative;
}}


/* GLASS CARD */

.card {{
    width: min(900px, 95%);

    padding: 45px 30px;

    text-align: center;

    border-radius: 35px;

    background: rgba(255,255,255,0.10);

    border: 1px solid rgba(255,255,255,0.25);

    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);

    box-shadow:
        0 25px 70px rgba(0,0,0,0.55),
        0 0 45px rgba(255,70,180,0.25);

    position: relative;
    z-index: 2;
}}


/* SMALL TITLE */

.small {{
    font-size: 14px;

    letter-spacing: 5px;

    color: #ffd2eb;

    margin-bottom: 15px;
}}


/* OPENING TITLE */

h1 {{
    font-size: clamp(38px, 7vw, 65px);

    margin: 10px 0 20px;

    background: linear-gradient(90deg, #ffffff, #ffb6dc, #ffffff);

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation: titleGlow 2.5s infinite alternate;
}}

@keyframes titleGlow {{
    from {{
        filter: drop-shadow(0 0 5px rgba(255,120,200,0.3));
    }}

    to {{
        filter: drop-shadow(0 0 25px rgba(255,120,200,0.9));
    }}
}}


/* NAME */

.name {{
    font-size: clamp(42px, 8vw, 75px);

    font-weight: bold;

    margin: 15px 0 30px;

    background: linear-gradient(
        90deg,
        #ffffff,
        #ff9fd3,
        #ffffff
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    filter: drop-shadow(0 0 18px rgba(255,80,190,0.7));

    animation: nameAppear 1.2s ease;
}}

@keyframes nameAppear {{
    from {{
        opacity: 0;
        transform: scale(0.7);
    }}

    to {{
        opacity: 1;
        transform: scale(1);
    }}
}}


/* MESSAGE */

.message {{
    font-size: 18px;

    line-height: 1.7;

    color: #f9eaf4;

    margin: 20px auto;

    max-width: 650px;
}}


/* OPEN BUTTON */

.open-btn {{
    margin-top: 25px;

    padding: 16px 30px;

    border: none;

    border-radius: 50px;

    background: linear-gradient(
        135deg,
        #ff4fa3,
        #a93cff
    );

    color: white;

    font-size: 17px;

    font-weight: bold;

    cursor: pointer;

    box-shadow:
        0 10px 30px rgba(255,50,170,0.4);

    transition: 0.3s;
}}

.open-btn:hover {{
    transform: translateY(-4px) scale(1.04);

    box-shadow:
        0 15px 40px rgba(255,50,170,0.7);
}}


/* PHOTOS */

.photos {{
    display: flex;

    justify-content: center;

    align-items: center;

    gap: 28px;

    flex-wrap: wrap;

    margin: 35px auto;

    perspective: 1000px;
}}


/* PREMIUM PHOTO CARD */

.photo {{
    width: 220px;
    height: 270px;

    object-fit: cover;

    padding: 7px;

    border-radius: 28px;

    border: 1px solid rgba(255,255,255,0.35);

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.30),
            rgba(255,255,255,0.06)
        );

    box-shadow:
        0 15px 35px rgba(0,0,0,0.45),
        0 0 25px rgba(255,50,190,0.35);

    backdrop-filter: blur(12px);

    transition:
        transform 0.5s ease,
        box-shadow 0.5s ease;

    animation: photoReveal 1.2s ease both;
}}


/* SECOND PHOTO DELAY */

.photo:nth-child(2) {{
    animation-delay: 0.25s;
}}


/* PHOTO HOVER */

.photo:hover {{
    transform:
        translateY(-12px)
        scale(1.05)
        rotateY(4deg);

    box-shadow:
        0 20px 45px rgba(0,0,0,0.55),
        0 0 45px rgba(255,50,190,0.8);
}}


/* PHOTO REVEAL */

@keyframes photoReveal {{

    from {{
        opacity: 0;

        transform:
            translateY(50px)
            scale(0.8)
            rotateY(-10deg);
    }}

    to {{
        opacity: 1;

        transform:
            translateY(0)
            scale(1)
            rotateY(0);
    }}

}}


/* FLOATING PHOTO ANIMATION */

.photo {{
    animation:
        photoReveal 1.2s ease both,
        photoFloat 5s ease-in-out infinite;
}}

.photo:nth-child(2) {{
    animation-delay: 0.25s, 1.2s;
}}

@keyframes photoFloat {{

    0%, 100% {{
        transform: translateY(0);
    }}

    50% {{
        transform: translateY(-8px);
    }}

}}


/* HIDDEN */

.hidden {{
    display: none;
}}


/* SURPRISE REVEAL */

.reveal {{
    animation: revealScreen 1.2s ease;
}}

@keyframes revealScreen {{

    from {{
        opacity: 0;
        transform: translateY(30px);
    }}

    to {{
        opacity: 1;
        transform: translateY(0);
    }}

}}


/* FLOATING HEARTS */

.hearts {{
    position: fixed;

    inset: 0;

    pointer-events: none;

    overflow: hidden;

    z-index: 1;
}}

.heart {{
    position: absolute;

    bottom: -50px;

    font-size: 22px;

    animation: floatHeart linear infinite;

    opacity: 0.7;
}}

.heart:nth-child(1) {{
    left: 10%;
    animation-duration: 8s;
}}

.heart:nth-child(2) {{
    left: 25%;
    animation-duration: 11s;
}}

.heart:nth-child(3) {{
    left: 40%;
    animation-duration: 9s;
}}

.heart:nth-child(4) {{
    left: 55%;
    animation-duration: 12s;
}}

.heart:nth-child(5) {{
    left: 70%;
    animation-duration: 10s;
}}

.heart:nth-child(6) {{
    left: 82%;
    animation-duration: 8s;
}}

.heart:nth-child(7) {{
    left: 92%;
    animation-duration: 13s;
}}

@keyframes floatHeart {{

    0% {{
        transform:
            translateY(0)
            rotate(0deg);

        opacity: 0;
    }}

    15% {{
        opacity: 0.8;
    }}

    100% {{
        transform:
            translateY(-850px)
            rotate(360deg);

        opacity: 0;
    }}

}}


/* MUSIC BUTTON */

.music-btn {{
    margin-top: 20px;

    padding: 10px 18px;

    border-radius: 30px;

    border: 1px solid rgba(255,255,255,0.25);

    background: rgba(255,255,255,0.10);

    color: white;

    cursor: pointer;

    font-size: 14px;

    backdrop-filter: blur(10px);

    transition: 0.3s;
}}

.music-btn:hover {{
    background: rgba(255,255,255,0.20);

    transform: scale(1.05);
}}


/* FOOTER */

.footer {{
    margin-top: 25px;

    font-size: 13px;

    color: #e9cfe0;
}}


/* MOBILE */

@media (max-width: 600px) {{

    .card {{
        padding: 35px 18px;
    }}

    .photo {{
        width: 145px;
        height: 185px;
    }}

    .photos {{
        gap: 15px;
    }}

    .message {{
        font-size: 16px;
    }}

}}

</style>

</head>


<body>


<div class="page">


<!-- FLOATING HEARTS -->

<div class="hearts">

<div class="heart">❤️</div>
<div class="heart">💖</div>
<div class="heart">💕</div>
<div class="heart">💗</div>
<div class="heart">❤️</div>
<div class="heart">💞</div>
<div class="heart">💖</div>

</div>


<!-- MAIN CARD -->

<div class="card">


<!-- OPENING SCREEN -->

<div id="opening">

<div class="small">
A SPECIAL SURPRISE
</div>

<h1>
For You ❤️
</h1>

<p class="message">
Someone has created something special just for you...
</p>

<button
class="open-btn"
onclick="openGift()">

Open My Surprise 💌

</button>

</div>


<!-- SURPRISE SCREEN -->

<div id="surprise" class="hidden">


<div class="small">
THIS ONE IS FOR
</div>


<div class="name">
Charitha ❤️
</div>


<!-- PHOTOS -->

<div class="photos">

<img
src="data:image/jpeg;base64,{photo1}"
class="photo"
alt="Charitha Photo 1"
>

<img
src="data:image/jpeg;base64,{photo2}"
class="photo"
alt="Charitha Photo 2"
>

</div>


<!-- MESSAGE -->

<p class="message">

A little surprise, made especially for you.

<br>
<br>

And this is only the beginning... ✨

</p>


<div style="font-size:45px;">
🌹 💖 🌹
</div>


<!-- MUSIC CONTROL -->

<button
id="musicButton"
class="music-btn"
onclick="toggleMusic()">

🎵 Music On

</button>


<div class="footer">

Made with ❤️ specially for Charitha

</div>


</div>


</div>

</div>


<!-- MUSIC -->

<audio
id="bgMusic"
preload="auto"
loop>

<source
src="data:audio/mpeg;base64,{song}"
type="audio/mpeg">

</audio>


<script>


/* OPEN SURPRISE */

function openGift() {{

    document.getElementById("opening").style.display = "none";

    const surprise =
        document.getElementById("surprise");

    surprise.classList.remove("hidden");

    surprise.classList.add("reveal");


    /* START MUSIC AFTER BUTTON CLICK */

    const music =
        document.getElementById("bgMusic");

    music.volume = 0.55;

    music.play().then(() => {{

        document.getElementById("musicButton").innerHTML =
            "🎵 Music On";

    }}).catch(() => {{

        document.getElementById("musicButton").innerHTML =
            "🎵 Tap Music";

    }});

}}


/* MUSIC ON / OFF */

function toggleMusic() {{

    const music =
        document.getElementById("bgMusic");

    const button =
        document.getElementById("musicButton");


    if (music.paused) {{

        music.play().then(() => {{

            button.innerHTML =
                "🎵 Music On";

        }});

    }} else {{

        music.pause();

        button.innerHTML =
            "🔇 Music Off";

    }}

}}

</script>


</body>

</html>
"""


components.html(
    html_code,
    height=750,
    scrolling=False
)
