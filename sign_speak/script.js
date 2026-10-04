/* =========================================================
   SIGNSPEAK - FRONTEND JAVASCRIPT
   ========================================================= */

document.addEventListener("DOMContentLoaded", () => {
    initNavigation();
    initTranslator();
    initDictionary();
    initHistory();
    initLearning();
    initModal();
});


/* =========================================================
   NAVIGATION
   ========================================================= */

function initNavigation() {

    const navLinks = document.querySelectorAll(".nav-links a");

    navLinks.forEach(link => {

        link.addEventListener("click", () => {

            navLinks.forEach(item => {
                item.classList.remove("active");
            });

            link.classList.add("active");
        });

    });
}


/* =========================================================
   SIGN LANGUAGE DATA
   ========================================================= */

const signs = [

    // Greetings
    { name: "Hello", emoji: "👋", category: "Greetings" },
    { name: "Goodbye", emoji: "👋", category: "Greetings" },
    { name: "Thank You", emoji: "🙏", category: "Greetings" },
    { name: "Please", emoji: "🙌", category: "Greetings" },
    { name: "Sorry", emoji: "😔", category: "Greetings" },
    { name: "Welcome", emoji: "🤗", category: "Greetings" },

    // Alphabet
    { name: "A", emoji: "✊", category: "Alphabet" },
    { name: "B", emoji: "🖐️", category: "Alphabet" },
    { name: "C", emoji: "🤏", category: "Alphabet" },
    { name: "D", emoji: "👌", category: "Alphabet" },
    { name: "E", emoji: "🤏", category: "Alphabet" },
    { name: "F", emoji: "🤙", category: "Alphabet" },
    { name: "G", emoji: "👉", category: "Alphabet" },
    { name: "H", emoji: "✌️", category: "Alphabet" },
    { name: "I", emoji: "🤟", category: "Alphabet" },
    { name: "J", emoji: "🤙", category: "Alphabet" },
    { name: "K", emoji: "✌️", category: "Alphabet" },
    { name: "L", emoji: "👆", category: "Alphabet" },
    { name: "M", emoji: "✊", category: "Alphabet" },
    { name: "N", emoji: "✊", category: "Alphabet" },
    { name: "O", emoji: "👌", category: "Alphabet" },
    { name: "P", emoji: "👇", category: "Alphabet" },
    { name: "Q", emoji: "👇", category: "Alphabet" },
    { name: "R", emoji: "🤞", category: "Alphabet" },
    { name: "S", emoji: "✊", category: "Alphabet" },
    { name: "T", emoji: "✊", category: "Alphabet" },
    { name: "U", emoji: "✌️", category: "Alphabet" },
    { name: "V", emoji: "✌️", category: "Alphabet" },
    { name: "W", emoji: "🖐️", category: "Alphabet" },
    { name: "X", emoji: "☝️", category: "Alphabet" },
    { name: "Y", emoji: "🤙", category: "Alphabet" },
    { name: "Z", emoji: "👉", category: "Alphabet" },

    // Numbers
    { name: "1", emoji: "☝️", category: "Numbers" },
    { name: "2", emoji: "✌️", category: "Numbers" },
    { name: "3", emoji: "🤟", category: "Numbers" },
    { name: "4", emoji: "🖐️", category: "Numbers" },
    { name: "5", emoji: "🖐️", category: "Numbers" },
    { name: "6", emoji: "🤙", category: "Numbers" },
    { name: "7", emoji: "🤞", category: "Numbers" },
    { name: "8", emoji: "🤏", category: "Numbers" },
    { name: "9", emoji: "👌", category: "Numbers" },
    { name: "10", emoji: "👍", category: "Numbers" },

    // Phrases
    { name: "I Love You", emoji: "🤟", category: "Phrases" },
    { name: "How Are You", emoji: "🤷", category: "Phrases" },
    { name: "Nice to Meet You", emoji: "🤝", category: "Phrases" },
    { name: "What Is Your Name", emoji: "❓", category: "Phrases" },
    { name: "My Name Is", emoji: "👤", category: "Phrases" },
    { name: "See You Later", emoji: "👀", category: "Phrases" },
    { name: "Help", emoji: "🆘", category: "Phrases" },
    { name: "No", emoji: "🚫", category: "Phrases" },
    { name: "Yes", emoji: "✅", category: "Phrases" },
    { name: "Friend", emoji: "🧑‍🤝‍🧑", category: "Phrases" },
    { name: "Family", emoji: "👨‍👩‍👧", category: "Phrases" },
    { name: "Water", emoji: "💧", category: "Phrases" },
    { name: "Eat", emoji: "🍽️", category: "Phrases" },
    { name: "Drink", emoji: "🥤", category: "Phrases" },
    { name: "Home", emoji: "🏠", category: "Phrases" },

    // Emotions
    { name: "Happy", emoji: "🙂", category: "Emotions" },
    { name: "Sad", emoji: "😢", category: "Emotions" },
    { name: "Angry", emoji: "😠", category: "Emotions" },
    { name: "Scared", emoji: "😨", category: "Emotions" },
    { name: "Excited", emoji: "😃", category: "Emotions" },
    { name: "Love", emoji: "❤️", category: "Emotions" },
    { name: "Tired", emoji: "😴", category: "Emotions" },
    { name: "Confused", emoji: "😕", category: "Emotions" },

    // Common words
    { name: "Who", emoji: "🙋", category: "Common Words" },
    { name: "Where", emoji: "📍", category: "Common Words" },
    { name: "When", emoji: "⏰", category: "Common Words" },
    { name: "Why", emoji: "🤷", category: "Common Words" },
    { name: "How", emoji: "🔄", category: "Common Words" },
    { name: "More", emoji: "➕", category: "Common Words" },
    { name: "Stop", emoji: "✋", category: "Common Words" },
    { name: "Go", emoji: "👉", category: "Common Words" },
    { name: "Good", emoji: "👍", category: "Common Words" },
    { name: "Bad", emoji: "👎", category: "Common Words" },
    { name: "Learn", emoji: "📚", category: "Common Words" },
    { name: "Understand", emoji: "💡", category: "Common Words" },
    { name: "Work", emoji: "💼", category: "Common Words" },
    { name: "Play", emoji: "🎮", category: "Common Words" },
    { name: "Time", emoji: "⏰", category: "Common Words" },
    { name: "Day", emoji: "☀️", category: "Common Words" },
    { name: "Night", emoji: "🌙", category: "Common Words" },
    { name: "Today", emoji: "📅", category: "Common Words" },
    { name: "Tomorrow", emoji: "🌅", category: "Common Words" },
    { name: "Yesterday", emoji: "📅", category: "Common Words" }
];


/* =========================================================
   TRANSLATOR
   ========================================================= */

function initTranslator() {

    const textArea = document.querySelector(".text-area");

    const translateButton =
        document.querySelector(".translate-btn");

    const output =
        document.querySelector(".sign-output");

    if (!textArea || !translateButton || !output) {
        return;
    }

    translateButton.addEventListener("click", () => {

        const text = textArea.value.trim();

        if (!text) {

            output.innerHTML = `
                <div>
                    <div style="font-size:35px;">✋</div>
                    <p>Please enter some text to translate.</p>
                </div>
            `;

            return;
        }

        translateText(text, output);

        saveHistory(text);

    });


    /* Quick phrase buttons */

    const quickButtons =
        document.querySelectorAll(".quick-btn");

    quickButtons.forEach(button => {

        button.addEventListener("click", () => {

            textArea.value = button.textContent.trim();

            translateButton.click();

        });

    });


    /* Swap button */

    const swapButton =
        document.querySelector(".swap-btn");

    const toggleButtons =
        document.querySelectorAll(".toggle-btn");

    if (swapButton) {

        swapButton.addEventListener("click", () => {

            toggleButtons.forEach(button => {
                button.classList.toggle("active");
            });

            const currentText = textArea.value;

            if (currentText) {
                translateText(currentText, output);
            }

        });

    }

}


/* =========================================================
   TEXT → SIGN TRANSLATION
   ========================================================= */

function translateText(text, output) {

    const words = text
        .toLowerCase()
        .replace(/[.,!?]/g, "")
        .split(/\s+/);

    const result = [];

    words.forEach(word => {

        const sign = signs.find(
            item =>
                item.name.toLowerCase() === word
        );

        if (sign) {

            result.push(`
                <div class="translated-sign">
                    <div style="font-size:45px;">
                        ${sign.emoji}
                    </div>

                    <strong>
                        ${sign.name}
                    </strong>

                    <small style="
                        display:block;
                        color:#5985ed;
                        margin-top:5px;
                    ">
                        ${sign.category}
                    </small>
                </div>
            `);

        } else {

            result.push(`
                <div class="translated-sign">
                    <div style="
                        font-size:18px;
                        color:#7f9cff;
                    ">
                        ${word}
                    </div>
                </div>
            `);

        }

    });

    output.innerHTML = `
        <div style="
            display:flex;
            flex-wrap:wrap;
            gap:20px;
            justify-content:center;
            align-items:center;
            padding:20px;
        ">
            ${result.join("")}
        </div>
    `;

}


/* =========================================================
   DICTIONARY
   ========================================================= */

function initDictionary() {

    const dictionaryGrid =
        document.querySelector(".dictionary-grid");

    if (!dictionaryGrid) {
        return;
    }

    renderDictionary(signs);


    /* Search */

    const searchInput =
        document.querySelector(".search-box input");

    if (searchInput) {

        searchInput.addEventListener("input", () => {

            const query =
                searchInput.value.toLowerCase().trim();

            const filtered = signs.filter(sign =>
                sign.name
                    .toLowerCase()
                    .includes(query)
            );

            renderDictionary(filtered);

        });

    }


    /* Category buttons */

    const categoryButtons =
        document.querySelectorAll(".category-btn");

    categoryButtons.forEach(button => {

        button.addEventListener("click", () => {

            categoryButtons.forEach(btn => {
                btn.classList.remove("active");
            });

            button.classList.add("active");

            const category =
                button.textContent.trim();

            if (
                category === "All Signs" ||
                category === "All"
            ) {

                renderDictionary(signs);

                return;
            }

            const filtered =
                signs.filter(sign =>
                    sign.category
                        .toLowerCase()
                        .includes(category.toLowerCase())
                );

            renderDictionary(filtered);

        });

    });

}


/* =========================================================
   RENDER DICTIONARY
   ========================================================= */

function renderDictionary(data) {

    const grid =
        document.querySelector(".dictionary-grid");

    if (!grid) {
        return;
    }

    grid.innerHTML = "";

    data.forEach(sign => {

        const card =
            document.createElement("div");

        card.className = "dictionary-card";

        card.innerHTML = `
            <div class="emoji">
                ${sign.emoji}
            </div>

            <h3>
                ${sign.name}
            </h3>

            <span>
                ${sign.category}
            </span>
        `;

        card.addEventListener("click", () => {
            showSignDetails(sign);
        });

        grid.appendChild(card);

    });


    /* Count */

    const countElement =
        document.querySelector(".sign-count");

    if (countElement) {

        countElement.textContent =
            `${data.length} signs found`;

    }

}


/* =========================================================
   SIGN DETAILS
   ========================================================= */

function showSignDetails(sign) {

    const modal =
        document.querySelector(".modal");

    if (!modal) {
        return;
    }

    const modalContent =
        modal.querySelector(".modal-content");

    if (!modalContent) {
        return;
    }

    modalContent.innerHTML = `
        <button class="modal-close">&times;</button>

        <div style="text-align:center;">

            <div style="
                font-size:80px;
                margin-bottom:15px;
            ">
                ${sign.emoji}
            </div>

            <h2>
                ${sign.name}
            </h2>

            <p style="
                color:#6f91ff;
                margin-top:10px;
            ">
                ${sign.category}
            </p>

            <p style="
                color:#9db1ff;
                margin-top:20px;
                line-height:1.6;
            ">
                Learn the ${sign.name} sign in
                American Sign Language.
            </p>

        </div>
    `;

    modal.classList.add("active");

    const close =
        modal.querySelector(".modal-close");

    if (close) {

        close.addEventListener("click", () => {
            modal.classList.remove("active");
        });

    }

}


/* =========================================================
   HISTORY
   ========================================================= */

function saveHistory(text) {

    let history =
        JSON.parse(
            localStorage.getItem("signSpeakHistory")
        ) || [];

    const item = {
        text: text,
        date: new Date().toLocaleString()
    };

    history.unshift(item);

    /* Keep latest 20 */

    history = history.slice(0, 20);

    localStorage.setItem(
        "signSpeakHistory",
        JSON.stringify(history)
    );

}


function initHistory() {

    const historyContainer =
        document.querySelector(".history-container");

    if (!historyContainer) {
        return;
    }

    const history =
        JSON.parse(
            localStorage.getItem("signSpeakHistory")
        ) || [];

    if (history.length === 0) {
        return;
    }

    historyContainer.innerHTML = `
        <div style="
            width:min(900px,100%);
            margin:auto;
        ">

            <h2 style="
                margin-bottom:25px;
                color:white;
            ">
                Recent Translations
            </h2>

            <div id="history-list"></div>

            <button
                id="clear-history"
                class="btn btn-outline"
                style="margin-top:25px;"
            >
                Clear History
            </button>

        </div>
    `;

    const list =
        document.querySelector("#history-list");

    history.forEach(item => {

        const historyCard =
            document.createElement("div");

        historyCard.style.cssText = `
            display:flex;
            justify-content:space-between;
            align-items:center;
            gap:20px;
            padding:18px;
            margin-bottom:12px;
            border:1px solid rgba(30,80,255,.5);
            border-radius:12px;
            background:#080d61;
        `;

        historyCard.innerHTML = `
            <strong>
                ${escapeHTML(item.text)}
            </strong>

            <span style="
                color:#6d8eea;
                font-size:12px;
            ">
                ${item.date}
            </span>
        `;

        list.appendChild(historyCard);

    });


    const clearButton =
        document.querySelector("#clear-history");

    clearButton.addEventListener("click", () => {

        localStorage.removeItem(
            "signSpeakHistory"
        );

        location.reload();

    });

}


/* =========================================================
   LEARNING SYSTEM
   ========================================================= */

function initLearning() {

    const lessonItems =
        document.querySelectorAll(".lesson-item");

    if (!lessonItems.length) {
        return;
    }

    let completed =
        JSON.parse(
            localStorage.getItem("signSpeakLessons")
        ) || [];

    lessonItems.forEach((item, index) => {

        const circle =
            item.querySelector(".lesson-circle");

        if (!circle) {
            return;
        }

        if (completed.includes(index)) {
            markLessonComplete(item);
        }

        item.style.cursor = "pointer";

        item.addEventListener("click", () => {

            if (completed.includes(index)) {

                completed =
                    completed.filter(
                        value => value !== index
                    );

                markLessonIncomplete(item);

            } else {

                completed.push(index);

                markLessonComplete(item);

            }

            localStorage.setItem(
                "signSpeakLessons",
                JSON.stringify(completed)
            );

            updateProgress();

        });

    });

    updateProgress();

}


/* =========================================================
   COMPLETE LESSON
   ========================================================= */

function markLessonComplete(item) {

    const circle =
        item.querySelector(".lesson-circle");

    if (circle) {

        circle.style.background =
            "linear-gradient(135deg,#08dcff,#087dff)";

        circle.style.boxShadow =
            "0 0 15px rgba(0,210,255,.5)";

        circle.innerHTML = "✓";

        circle.style.display = "grid";
        circle.style.placeItems = "center";
        circle.style.color = "#031449";
        circle.style.fontWeight = "900";

    }

    item.style.color = "#08d8ff";

}


function markLessonIncomplete(item) {

    const circle =
        item.querySelector(".lesson-circle");

    if (circle) {

        circle.style.background =
            "transparent";

        circle.style.boxShadow =
            "0 0 8px rgba(0,180,255,.3)";

        circle.innerHTML = "";

    }

    item.style.color = "#e3e9ff";

}


/* =========================================================
   UPDATE LEARNING PROGRESS
   ========================================================= */

function updateProgress() {

    const items =
        document.querySelectorAll(".lesson-item");

    if (!items.length) {
        return;
    }

    let completed = 0;

    items.forEach(item => {

        const circle =
            item.querySelector(".lesson-circle");

        if (
            circle &&
            circle.innerHTML.trim() === "✓"
        ) {
            completed++;
        }

    });

    const total = items.length;

    const percentage =
        total === 0
            ? 0
            : Math.round(
                (completed / total) * 100
            );


    /* Main progress */

    const progressFill =
        document.querySelector(".progress-fill");

    if (progressFill) {
        progressFill.style.width =
            `${percentage}%`;
    }


    /* Percentage text */

    const percent =
        document.querySelector(
            ".progress-header span:last-child"
        );

    if (percent) {
        percent.textContent =
            `${percentage}%`;
    }


    /* Completed text */

    const progressText =
        document.querySelector(".progress-text");

    if (progressText) {

        progressText.textContent =
            `${completed} of ${total} topics completed`;

    }


    /* Lesson percentages */

    document
        .querySelectorAll(".lesson-percent")
        .forEach(element => {

            element.textContent =
                percentage + "%";

        });

}


/* =========================================================
   MODAL
   ========================================================= */

function initModal() {

    const modal =
        document.querySelector(".modal");

    if (!modal) {
        return;
    }

    modal.addEventListener("click", event => {

        if (event.target === modal) {
            modal.classList.remove("active");
        }

    });


    document.addEventListener("keydown", event => {

        if (event.key === "Escape") {
            modal.classList.remove("active");
        }

    });

}


/* =========================================================
   TEXT TO SPEECH
   ========================================================= */

function speakText(text) {

    if (!("speechSynthesis" in window)) {

        alert(
            "Text-to-speech is not supported in this browser."
        );

        return;
    }

    window.speechSynthesis.cancel();

    const speech =
        new SpeechSynthesisUtterance(text);

    speech.lang = "en-US";

    speech.rate = 0.9;

    speech.pitch = 1;

    window.speechSynthesis.speak(speech);

}


/* =========================================================
   ADD VOICE BUTTON FUNCTIONALITY
   ========================================================= */

document.addEventListener("click", event => {

    const voiceButton =
        event.target.closest(".voice-btn");

    if (!voiceButton) {
        return;
    }

    const textArea =
        document.querySelector(".text-area");

    if (textArea && textArea.value.trim()) {

        speakText(
            textArea.value.trim()
        );

    }

});


/* =========================================================
   CAMERA ACCESS
   ========================================================= */

async function startCamera(videoElement) {

    if (!videoElement) {
        return;
    }

    try {

        const stream =
            await navigator.mediaDevices.getUserMedia({
                video: true
            });

        videoElement.srcObject = stream;

        videoElement.play();

    } catch (error) {

        console.error(
            "Camera access error:",
            error
        );

        alert(
            "Camera access was denied or is unavailable."
        );

    }

}


/* =========================================================
   STOP CAMERA
   ========================================================= */

function stopCamera(videoElement) {

    if (
        !videoElement ||
        !videoElement.srcObject
    ) {
        return;
    }

    const tracks =
        videoElement.srcObject.getTracks();

    tracks.forEach(track => {
        track.stop();
    });

    videoElement.srcObject = null;

}


/* =========================================================
   HTML SECURITY HELPER
   ========================================================= */

function escapeHTML(value) {

    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");

}


/* =========================================================
   DEMO REAL-TIME DETECTION
   ========================================================= */

function startDetection() {

    const detectionText =
        document.querySelector(
            ".detection-text"
        );

    if (!detectionText) {
        return;
    }

    detectionText.textContent =
        "Camera is ready for sign detection.";

}


/* =========================================================
   PAGE LOAD ANIMATION
   ========================================================= */

document.addEventListener("DOMContentLoaded", () => {

    const elements =
        document.querySelectorAll(
            ".feature-card, .dictionary-card, .lesson-card"
        );

    elements.forEach((element, index) => {

        element.style.opacity = "0";

        element.style.transform =
            "translateY(15px)";

        setTimeout(() => {

            element.style.transition =
                "opacity .5s ease, transform .5s ease";

            element.style.opacity = "1";

            element.style.transform =
                "translateY(0)";

        }, index * 30);

    });

});