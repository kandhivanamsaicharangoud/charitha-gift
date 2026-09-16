import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Special Surprise ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background: #0b0014;
    color: white;
    overflow: hidden;
}

.page {
    width: 100%;
    height: 100vh;
    min-height: 650px;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    background:
        radial-gradient(circle at 50% 40%, #5b0b70 0%, #21002f 35%, #08000d 80%);
}

.hearts {
    position: absolute;
    inset: 0;
    overflow: hidden;
    pointer-events: none;
}

.heart {
    position: absolute;
    bottom: -50px;
    font-size: 25px;
    animation: floatUp linear infinite;
    opacity: 0.8;
}

.heart:nth-child(1) { left: 8%; animation-duration: 7s; }
.heart:nth-child(2) { left: 20%; animation-duration: 10s; }
.heart:nth-child(3) { left: 35%; animation-duration: 8s; }
.heart:nth-child(4) { left: 50%; animation-duration: 12s; }
.heart:nth-child(5) { left: 65%; animation-duration: 9s; }
.heart:nth-child(6) { left: 80%; animation-duration: 11s; }
.heart:nth-child(7) { left: 92%; animation-duration: 7s; }

@keyframes floatUp {
    0% {
        transform: translateY(0) scale(0.7) rotate(0deg);
        opacity: 0;
    }
    20% { opacity: 1; }
    100% {
        transform: translateY(-110vh) scale(1.3) rotate(360deg);
        opacity: 0;
    }
}

.card {
    position: relative;
    z-index: 5;
    width: min(90%, 650px);
    padding: 55px 30px;
    text-align: center;
    border-radius: 30px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.18);
    backdrop-filter: blur(15px);
    box-shadow: 0 0 50px rgba(255,0,150,0.25);
}

.small {
    font-size: 17px;
    letter-spacing: 3px;
    color: #ffc6ed;
    margin-bottom: 20px;
}

h1 {
    font-size: clamp(40px, 8vw, 75px);
    margin-bottom: 15px;
    background: linear-gradient(90deg, #fff, #ff8bdc, #fff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 2s infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 10px #ff42bd; }
    to { text-shadow: 0 0 35px #ff42bd; }
}

.name {
    font-size: clamp(35px, 7vw, 65px);
    color: #ff80d5;
    font-weight: bold;
    margin: 15px 0;
}

.message {
    font-size: 18px;
    line-height: 1.7;
    color: #f8dff1;
    margin: 20px auto;
    max-width: 500px;
}

.open-btn {
    margin-top: 20px;
    padding: 16px 35px;
    border: none;
    border-radius: 50px;
    background: linear-gradient(90deg, #ff299c, #a900ff);
    color: white;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 0 25px rgba(255,0,170,0.5);
    transition: 0.3s;
}

.open-btn:hover {
    transform: scale(1.08);
}

.hidden {
    display: none;
}

.reveal {
    animation: reveal 1.5s ease forwards;
}

@keyframes reveal {
    from {
        opacity: 0;
        transform: translateY(30px) scale(0.9);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.photo-placeholder {
    width: 230px;
    height: 230px;
    margin: 20px auto;
    border-radius: 50%;
    border: 5px solid #ff76d0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 70px;
    box-shadow: 0 0 40px rgba(255,50,190,0.6);
    background: rgba(255,255,255,0.08);
}

.footer {
    margin-top: 25px;
    font-size: 13px;
    color: #c9a8c4;
}
</style>
</head>

<body>

<div class="page">

    <div class="hearts">
        <div class="heart">❤️</div>
        <div class="heart">💖</div>
        <div class="heart">💕</div>
        <div class="heart">❤️</div>
        <div class="heart">💗</div>
        <div class="heart">💞</div>
        <div class="heart">❤️</div>
    </div>

    <div class="card">

        <div id="opening">
            <div class="small">A SPECIAL SURPRISE</div>

            <h1>For You ❤️</h1>

            <p class="message">
                Someone has created something special
                just for you...
            </p>

            <button class="open-btn" onclick="openGift()">
                Open My Surprise 💌
            </button>
        </div>


        <div id="surprise" class="hidden">

            <div class="small">THIS ONE IS FOR</div>

            <div class="name">Charitha ❤️</div>

            <div class="photo-placeholder">
                📸
            </div>

            <p class="message">
                Your special photo will appear here.
                <br><br>
                And this is only the beginning...
                ✨
            </p>

            <div style="font-size:45px;">
                🌹 💖 🌹
            </div>

            <div class="footer">
                Made with ❤️ specially for Charitha
            </div>

        </div>

    </div>

</div>


<script>

function openGift() {

    document.getElementById("opening").style.display = "none";

    const surprise = document.getElementById("surprise");

    surprise.classList.remove("hidden");
    surprise.classList.add("reveal");

}

</script>

</body>
</html>
"""

components.html(html_code, height=750, scrolling=False)