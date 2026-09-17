import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(
    page_title="A Special Surprise ❤️",
    page_icon="❤️",
    layout="centered"
)

# -----------------------------
# FILE PATHS
# -----------------------------

song_path = "assets/jo tum mereho.mpeg"
photo1_path = "assets/charitha1.jpg"
photo2_path = "assets/charitha2.jpg"


# -----------------------------
# CHECK FILES
# -----------------------------

for file_path in [song_path, photo1_path, photo2_path]:
    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}")
        st.stop()


# -----------------------------
# BASE64
# -----------------------------

with open(song_path, "rb") as f:
    song_base64 = base64.b64encode(f.read()).decode()

with open(photo1_path, "rb") as f:
    photo1_base64 = base64.b64encode(f.read()).decode()

with open(photo2_path, "rb") as f:
    photo2_base64 = base64.b64encode(f.read()).decode()


# -----------------------------
# HTML
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

    font-family: Arial, Helvetica, sans-serif;

    background:
        radial-gradient(
            circle at top,
            #35104f 0%,
            #16091f 45%,
            #08050c 100%
        );

    color: white;

    min-height: 100vh;

    overflow-x: hidden;
}}


/* MAIN */

.container {{
    min-height: 100vh;

    display: flex;

    justify-content: center;

    align-items: center;

    padding: 30px 15px;
}}

.card {{
    width: 100%;

    max-width: 850px;

    padding: 55px 30px;

    text-align: center;

    border-radius: 35px;

    background: rgba(255,255,255,0.08);

    border: 1px solid rgba(255,255,255,0.20);

    box-shadow:
        0 25px 70px rgba(0,0,0,0.55),
        0 0 50px rgba(255,60,190,0.18);

    backdrop-filter: blur(15px);

    position: relative;

    z-index: 2;
}}


/* OPENING */

.opening {{
    animation: cardAppear 1.2s ease;
}}

.opening h1 {{
    font-size: clamp(32px, 7vw, 55px);

    margin-bottom: 15px;

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #ff9de2,
            #ffffff
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}}

.opening p {{
    font-size: 18px;

    line-height: 1.7;

    opacity: 0.85;

    margin-bottom: 35px;
}}

@keyframes cardAppear {{

    from {{
        opacity: 0;
        transform: translateY(30px);
    }}

    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}


/* OPEN BUTTON */

.open-button {{
    border: none;

    padding: 16px 32px;

    border-radius: 50px;

    font-size: 18px;

    font-weight: bold;

    cursor: pointer;

    color: white;

    background:
        linear-gradient(
            135deg,
            #ff3cac,
            #784ba0
        );

    box-shadow:
        0 10px 30px rgba(255,60,190,0.35);

    transition: all 0.3s ease;
}}

.open-button:hover {{
    transform:
        translateY(-4px)
        scale(1.03);

    box-shadow:
        0 15px 40px
        rgba(255,60,190,0.55);
}}


/* HIDDEN */

.hidden {{
    display: none;
}}


/* SURPRISE */

.surprise-title {{
    margin-bottom: 10px;

    font-size: 18px;

    letter-spacing: 4px;

    opacity: 0.65;
}}

.name {{
    font-size:
        clamp(50px, 11vw, 85px);

    margin: 10px 0 15px;

    background:
        linear-gradient(
            90deg,
            #ff7bd5,
            #ffffff,
            #ff7bd5
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    animation:
        nameGlow
        2s
        ease-in-out
        infinite
        alternate;
}}

@keyframes nameGlow {{

    from {{
        filter:
            drop-shadow(
                0 0 5px
                rgba(255,80,200,0.3)
            );
    }}

    to {{
        filter:
            drop-shadow(
                0 0 25px
                rgba(255,80,200,0.8)
            );
    }}
}}

.subtitle {{
    font-size: 18px;

    opacity: 0.8;

    margin-bottom: 25px;
}}


/* PHOTOS */

.photos {{
    position: relative;

    width:
        min(300px, 85vw);

    height: 360px;

    margin: 40px auto;
}}

.photo {{
    position: absolute;

    top: 0;
    left: 0;

    width: 100%;
    height: 100%;

    object-fit: cover;

    padding: 7px;

    border-radius: 28px;

    border:
        1px solid
        rgba(255,255,255,0.4);

    background:
        rgba(255,255,255,0.12);

    box-shadow:
        0 20px 50px rgba(0,0,0,0.55),
        0 0 35px rgba(255,50,190,0.5);

    opacity: 0;

    animation:
        photoSlide
        8s infinite;
}}

.photo:nth-child(1) {{
    animation-delay: 0s;
}}

.photo:nth-child(2) {{
    animation-delay: 4s;
}}

@keyframes photoSlide {{

    0% {{
        opacity: 0;
        transform: scale(0.92);
    }}

    8% {{
        opacity: 1;
        transform: scale(1);
    }}

    42% {{
        opacity: 1;
        transform: scale(1.04);
    }}

    50% {{
        opacity: 0;
        transform: scale(1.08);
    }}

    100% {{
        opacity: 0;
    }}
}}


/* MUSIC BUTTON */

.music-button {{
    margin-top: 20px;

    border:
        1px solid
        rgba(255,255,255,0.25);

    padding: 12px 22px;

    border-radius: 30px;

    color: white;

    background:
        rgba(255,255,255,0.10);

    cursor: pointer;

    font-size: 15px;

    transition: 0.3s;
}}

.music-button:hover {{
    background:
        rgba(255,255,255,0.18);

    transform: scale(1.03);
}}


/* BIRTHDAY WISH */

.birthday-wish {{
    margin: 50px auto 30px;

    padding: 32px 24px;

    max-width: 700px;

    border-radius: 28px;

    background:
        rgba(255,255,255,0.10);

    border:
        1px solid
        rgba(255,255,255,0.25);

    box-shadow:
        0 15px 40px rgba(0,0,0,0.35),
        0 0 30px rgba(255,70,190,0.18);

    animation:
        wishAppear
        2s ease;
}}

.birthday-wish h2 {{
    font-size:
        clamp(28px, 6vw, 42px);

    margin-bottom: 20px;
}}

.birthday-wish p {{
    font-size: 18px;

    line-height: 1.7;

    opacity: 0.9;
}}

@keyframes wishAppear {{

    from {{
        opacity: 0;
        transform: translateY(35px);
    }}

    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

.from {{
    margin-top: 25px;

    font-size: 20px;

    font-weight: bold;

    opacity: 0.9;
}}


/* FINAL SCREEN */

.final-screen {{
    margin-top: 60px;

    padding: 45px 25px;

    border-radius: 30px;

    background:
        rgba(255,255,255,0.07);

    border:
        1px solid
        rgba(255,255,255,0.18);

    animation:
        finalReveal
        3s
        ease;
}}

.final-screen h2 {{
    font-size:
        clamp(30px, 7vw, 50px);

    margin-bottom: 20px;

    animation:
        finalGlow
        2s
        ease-in-out
        infinite
        alternate;
}}

.final-screen p {{
    font-size: 18px;

    line-height: 1.8;

    opacity: 0.85;
}}

.final-heart {{
    font-size: 55px;

    margin: 15px;

    animation:
        heartBeat
        1.5s
        infinite;
}}

@keyframes finalReveal {{

    from {{
        opacity: 0;
        transform: translateY(50px) scale(0.9);
    }}

    to {{
        opacity: 1;
        transform: translateY(0) scale(1);
    }}
}}

@keyframes finalGlow {{

    from {{
        filter:
            drop-shadow(
                0 0 5px
                rgba(255,70,190,0.3)
            );
    }}

    to {{
        filter:
            drop-shadow(
                0 0 30px
                rgba(255,70,190,0.9)
            );
    }}
}}

@keyframes heartBeat {{

    0%, 100% {{
        transform: scale(1);
    }}

    50% {{
        transform: scale(1.25);
    }}
}}


/* FOOTER */

.footer {{
    margin-top: 45px;

    font-size: 14px;

    opacity: 0.55;
}}


/* FLOATING HEARTS */

.heart {{
    position: fixed;

    bottom: -50px;

    font-size: 25px;

    pointer-events: none;

    z-index: 10;

    animation:
        floatHeart
        linear
        forwards;
}}

@keyframes floatHeart {{

    0% {{
        transform:
            translateY(0)
            rotate(0deg)
            scale(0.7);

        opacity: 0;
    }}

    10% {{
        opacity: 1;
    }}

    50% {{
        transform:
            translateY(-50vh)
            rotate(180deg)
            scale(1);
    }}

    100% {{
        transform:
            translateY(-115vh)
            rotate(360deg)
            scale(0.8);

        opacity: 0;
    }}
}}


/* CONFETTI */

.confetti {{
    position: fixed;

    top: -20px;

    width: 9px;

    height: 16px;

    pointer-events: none;

    z-index: 20;

    animation:
        confettiFall
        linear
        forwards;
}}

@keyframes confettiFall {{

    0% {{
        transform:
            translateY(-20px)
            rotate(0deg);

        opacity: 1;
    }}

    100% {{
        transform:
            translateY(110vh)
            rotate(720deg);

        opacity: 0;
    }}
}}


/* MOBILE */

@media (max-width: 600px) {{

    .card {{
        padding: 35px 18px;
    }}

    .photos {{
        width:
            min(260px, 85vw);

        height: 320px;
    }}

    .photo {{
        width: 100%;
        height: 100%;
    }}

    .birthday-wish {{
        padding: 25px 18px;
    }}

    .birthday-wish p {{
        font-size: 16px;
    }}

    .final-screen {{
        padding: 35px 18px;
    }}

}}

</style>

</head>


<body>


<div class="container">

<div class="card">


<!-- OPENING -->

<div id="opening" class="opening">

<h1>
A SPECIAL SURPRISE
</h1>

<p>
For You ❤️
<br><br>
Someone has created something special just for you...
</p>

<button
class="open-button"
onclick="openSurprise()"
>
💌 Open My Surprise
</button>

</div>


<!-- SURPRISE -->

<div id="surprise" class="hidden">


<div class="surprise-title">
THIS ONE IS FOR
</div>


<div class="name">
OYE ❤️
</div>


<div class="subtitle">
A little surprise, made especially for you.
</div>


<!-- PHOTOS -->

<div class="photos">

<img
class="photo"
src="data:image/jpeg;base64,{photo1_base64}"
>

<img
class="photo"
src="data:image/jpeg;base64,{photo2_base64}"
>

</div>


<!-- MUSIC -->

<audio
id="birthdaySong"
loop
>

<source
src="data:audio/mpeg;base64,{song_base64}"
type="audio/mpeg"
>

</audio>


<button
class="music-button"
onclick="toggleMusic()"
id="musicButton"
>
⏸️ Pause Music
</button>


<!-- BIRTHDAY WISH -->

<div class="birthday-wish">

<h2>
🎂 Happy Birthday, OYE! ❤️
</h2>

<p>
Wishing you lots of happiness,
smiles and beautiful moments. ✨
</p>

<p>
Have a wonderful birthday! 🥳💖
</p>

<div class="from">
— With love, Jagan ❤️
</div>

</div>


<!-- FINAL ENDING -->

<div class="final-screen">

<div class="final-heart">
❤️
</div>

<h2>
That's All For You, OYE! ✨
</h2>

<p>
Hope this little surprise
brought a smile to your face. 😊
</p>

<p>
Once again...
<br>
🎂 Happy Birthday! 🥳
</p>

<p>
Thank you for being a beautiful part
of these memories. ❤️
</p>

</div>


<div class="footer">
Made with ❤️ specially for OYE
<br><br>
— Jagan
</div>


</div>

</div>

</div>


<script>


/* OPEN SURPRISE */

function openSurprise() {{

    document.getElementById(
        "opening"
    ).style.display = "none";


    document.getElementById(
        "surprise"
    ).style.display = "block";


    const song =
        document.getElementById(
            "birthdaySong"
        );


    song.play().catch(
        function(error) {{

            console.log(
                "Autoplay was blocked:",
                error
            );

        }}
    );


    createConfetti();

    startHearts();

}}


/* MUSIC */

function toggleMusic() {{

    const song =
        document.getElementById(
            "birthdaySong"
        );

    const button =
        document.getElementById(
            "musicButton"
        );


    if (song.paused) {{

        song.play();

        button.innerHTML =
            "⏸️ Pause Music";

    }}

    else {{

        song.pause();

        button.innerHTML =
            "▶️ Play Music";

    }}

}}


/* HEARTS */

function startHearts() {{

    setInterval(
        createHeart,
        700
    );

}}


function createHeart() {{

    const heart =
        document.createElement(
            "div"
        );


    heart.className =
        "heart";


    const hearts = [
        "❤️",
        "💖",
        "💕",
        "💗",
        "💓",
        "💞"
    ];


    heart.innerHTML =
        hearts[
            Math.floor(
                Math.random() *
                hearts.length
            )
        ];


    heart.style.left =
        Math.random() * 100 + "vw";


    heart.style.fontSize =
        (18 + Math.random() * 20) + "px";


    heart.style.animationDuration =
        (5 + Math.random() * 4) + "s";


    document.body.appendChild(
        heart
    );


    setTimeout(
        function() {{
            heart.remove();
        }},
        10000
    );

}}


/* CONFETTI */

function createConfetti() {{

    for (
        let i = 0;
        i < 100;
        i++
    ) {{

        setTimeout(
            createConfettiPiece,
            i * 20
        );

    }}

}}


function createConfettiPiece() {{

    const piece =
        document.createElement(
            "div"
        );


    piece.className =
        "confetti";


    const confettiColors = [

        "#ff3cac",
        "#ffcc00",
        "#00e5ff",
        "#7cff00",
        "#ffffff",
        "#ff6b6b",
        "#b967ff"

    ];


    piece.style.background =
        confettiColors[
            Math.floor(
                Math.random() *
                confettiColors.length
            )
        ];


    piece.style.left =
        Math.random() * 100 + "vw";


    piece.style.width =
        (5 + Math.random() * 7) + "px";


    piece.style.height =
        (8 + Math.random() * 12) + "px";


    piece.style.animationDuration =
        (3 + Math.random() * 3) + "s";


    document.body.appendChild(
        piece
    );


    setTimeout(
        function() {{
            piece.remove();
        }},
        7000
    );

}}


</script>


</body>

</html>
"""


# -----------------------------
# DISPLAY
# -----------------------------

components.html(
    html_code,
    height=2000,
    scrolling=True
)
