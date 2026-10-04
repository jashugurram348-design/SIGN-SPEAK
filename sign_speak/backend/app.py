from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# =========================================================
# SIGN DATA
# =========================================================

SIGNS = [
    # Greetings
    {"name": "Hello", "emoji": "👋", "category": "Greetings"},
    {"name": "Goodbye", "emoji": "👋", "category": "Greetings"},
    {"name": "Thank You", "emoji": "🙏", "category": "Greetings"},
    {"name": "Please", "emoji": "🙌", "category": "Greetings"},
    {"name": "Sorry", "emoji": "😔", "category": "Greetings"},
    {"name": "Welcome", "emoji": "🤗", "category": "Greetings"},

    # Alphabet
    {"name": "A", "emoji": "✊", "category": "Alphabet"},
    {"name": "B", "emoji": "🖐️", "category": "Alphabet"},
    {"name": "C", "emoji": "🤏", "category": "Alphabet"},
    {"name": "D", "emoji": "👌", "category": "Alphabet"},
    {"name": "E", "emoji": "✊", "category": "Alphabet"},
    {"name": "F", "emoji": "🤙", "category": "Alphabet"},
    {"name": "G", "emoji": "👉", "category": "Alphabet"},
    {"name": "H", "emoji": "✌️", "category": "Alphabet"},
    {"name": "I", "emoji": "🤟", "category": "Alphabet"},
    {"name": "J", "emoji": "🤙", "category": "Alphabet"},
    {"name": "K", "emoji": "✌️", "category": "Alphabet"},
    {"name": "L", "emoji": "☝️", "category": "Alphabet"},
    {"name": "M", "emoji": "✊", "category": "Alphabet"},
    {"name": "N", "emoji": "✊", "category": "Alphabet"},
    {"name": "O", "emoji": "👌", "category": "Alphabet"},
    {"name": "P", "emoji": "👇", "category": "Alphabet"},
    {"name": "Q", "emoji": "👇", "category": "Alphabet"},
    {"name": "R", "emoji": "🤞", "category": "Alphabet"},
    {"name": "S", "emoji": "✊", "category": "Alphabet"},
    {"name": "T", "emoji": "✊", "category": "Alphabet"},
    {"name": "U", "emoji": "✌️", "category": "Alphabet"},
    {"name": "V", "emoji": "✌️", "category": "Alphabet"},
    {"name": "W", "emoji": "🖐️", "category": "Alphabet"},
    {"name": "X", "emoji": "☝️", "category": "Alphabet"},
    {"name": "Y", "emoji": "🤙", "category": "Alphabet"},
    {"name": "Z", "emoji": "👉", "category": "Alphabet"},

    # Numbers
    {"name": "1", "emoji": "☝️", "category": "Numbers"},
    {"name": "2", "emoji": "✌️", "category": "Numbers"},
    {"name": "3", "emoji": "🤟", "category": "Numbers"},
    {"name": "4", "emoji": "🖐️", "category": "Numbers"},
    {"name": "5", "emoji": "🖐️", "category": "Numbers"},
    {"name": "6", "emoji": "🤙", "category": "Numbers"},
    {"name": "7", "emoji": "🤞", "category": "Numbers"},
    {"name": "8", "emoji": "🤏", "category": "Numbers"},
    {"name": "9", "emoji": "👌", "category": "Numbers"},
    {"name": "10", "emoji": "👍", "category": "Numbers"},

    # Phrases
    {"name": "I Love You", "emoji": "🤟", "category": "Phrases"},
    {"name": "How Are You", "emoji": "🤷", "category": "Phrases"},
    {"name": "Nice to Meet You", "emoji": "🤝", "category": "Phrases"},
    {"name": "What Is Your Name", "emoji": "❓", "category": "Phrases"},
    {"name": "My Name Is", "emoji": "👤", "category": "Phrases"},
    {"name": "See You Later", "emoji": "👀", "category": "Phrases"},
    {"name": "Help", "emoji": "🆘", "category": "Phrases"},
    {"name": "No", "emoji": "🚫", "category": "Phrases"},
    {"name": "Yes", "emoji": "✅", "category": "Phrases"},
    {"name": "Friend", "emoji": "🧑‍🤝‍🧑", "category": "Phrases"},
    {"name": "Family", "emoji": "👨‍👩‍👧", "category": "Phrases"},
    {"name": "Water", "emoji": "💧", "category": "Phrases"},
    {"name": "Eat", "emoji": "🍽️", "category": "Phrases"},
    {"name": "Drink", "emoji": "🥤", "category": "Phrases"},
    {"name": "Home", "emoji": "🏠", "category": "Phrases"},

    # Emotions
    {"name": "Happy", "emoji": "🙂", "category": "Emotions"},
    {"name": "Sad", "emoji": "😢", "category": "Emotions"},
    {"name": "Angry", "emoji": "😠", "category": "Emotions"},
    {"name": "Scared", "emoji": "😨", "category": "Emotions"},
    {"name": "Excited", "emoji": "😃", "category": "Emotions"},
    {"name": "Love", "emoji": "❤️", "category": "Emotions"},
    {"name": "Tired", "emoji": "😴", "category": "Emotions"},
    {"name": "Confused", "emoji": "😕", "category": "Emotions"},

    # Common words
    {"name": "Who", "emoji": "🙋", "category": "Common Words"},
    {"name": "Where", "emoji": "📍", "category": "Common Words"},
    {"name": "When", "emoji": "⏰", "category": "Common Words"},
    {"name": "Why", "emoji": "🤷", "category": "Common Words"},
    {"name": "How", "emoji": "🔄", "category": "Common Words"},
    {"name": "More", "emoji": "➕", "category": "Common Words"},
    {"name": "Stop", "emoji": "✋", "category": "Common Words"},
    {"name": "Go", "emoji": "👉", "category": "Common Words"},
    {"name": "Good", "emoji": "👍", "category": "Common Words"},
    {"name": "Bad", "emoji": "👎", "category": "Common Words"},
    {"name": "Learn", "emoji": "📚", "category": "Common Words"},
    {"name": "Understand", "emoji": "💡", "category": "Common Words"},
    {"name": "Work", "emoji": "💼", "category": "Common Words"},
    {"name": "Play", "emoji": "🎮", "category": "Common Words"},
    {"name": "Time", "emoji": "⏰", "category": "Common Words"},
    {"name": "Day", "emoji": "☀️", "category": "Common Words"},
    {"name": "Night", "emoji": "🌙", "category": "Common Words"},
    {"name": "Today", "emoji": "📅", "category": "Common Words"},
    {"name": "Tomorrow", "emoji": "🌅", "category": "Common Words"},
    {"name": "Yesterday", "emoji": "📅", "category": "Common Words"}
]


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


# =========================================================
# DICTIONARY PAGE
# =========================================================

@app.route("/dictionary")
def dictionary():
    return render_template(
        "dictionary.html",
        signs=SIGNS
    )


# =========================================================
# HISTORY PAGE
# =========================================================

@app.route("/history")
def history():
    return render_template("history.html")


# =========================================================
# LEARN PAGE
# =========================================================

@app.route("/learn")
def learn():
    return render_template("learn.html")


# =========================================================
# API - GET ALL SIGNS
# =========================================================

@app.route("/api/signs", methods=["GET"])
def get_signs():

    return jsonify({
        "success": True,
        "count": len(SIGNS),
        "signs": SIGNS
    })


# =========================================================
# API - SEARCH SIGNS
# =========================================================

@app.route("/api/signs/search", methods=["GET"])
def search_signs():

    query = request.args.get("q", "").lower().strip()

    if not query:
        return jsonify({
            "success": True,
            "count": len(SIGNS),
            "signs": SIGNS
        })

    results = [
        sign for sign in SIGNS
        if query in sign["name"].lower()
        or query in sign["category"].lower()
    ]

    return jsonify({
        "success": True,
        "count": len(results),
        "signs": results
    })


# =========================================================
# API - CATEGORY FILTER
# =========================================================

@app.route("/api/signs/category/<category>")
def signs_by_category(category):

    results = [
        sign for sign in SIGNS
        if sign["category"].lower() == category.lower()
    ]

    return jsonify({
        "success": True,
        "category": category,
        "count": len(results),
        "signs": results
    })


# =========================================================
# API - TRANSLATE TEXT TO SIGN
# =========================================================

@app.route("/api/translate", methods=["POST"])
def translate():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "No data received."
        }), 400

    text = data.get("text", "").strip()

    if not text:
        return jsonify({
            "success": False,
            "message": "Please enter some text."
        }), 400

    words = (
        text.lower()
        .replace(",", "")
        .replace(".", "")
        .replace("!", "")
        .replace("?", "")
        .split()
    )

    translated = []

    for word in words:

        found = None

        for sign in SIGNS:

            if sign["name"].lower() == word:
                found = sign
                break

        if found:

            translated.append({
                "word": word,
                "sign": found
            })

        else:

            translated.append({
                "word": word,
                "sign": None
            })

    return jsonify({
        "success": True,
        "original_text": text,
        "translation": translated,
        "timestamp": datetime.now().isoformat()
    })


# =========================================================
# API - SIGN DETAILS
# =========================================================

@app.route("/api/sign/<name>")
def sign_details(name):

    for sign in SIGNS:

        if sign["name"].lower() == name.lower():

            return jsonify({
                "success": True,
                "sign": sign
            })

    return jsonify({
        "success": False,
        "message": "Sign not found."
    }), 404


# =========================================================
# HEALTH CHECK
# =========================================================

@app.route("/api/status")
def status():

    return jsonify({
        "status": "online",
        "application": "SignSpeak",
        "message": "SignSpeak backend is running."
    })


# =========================================================
# ERROR HANDLERS
# =========================================================

@app.errorhandler(404)
def page_not_found(error):

    return jsonify({
        "success": False,
        "error": "Page not found"
    }), 404


@app.errorhandler(500)
def server_error(error):

    return jsonify({
        "success": False,
        "error": "Internal server error"
    }), 500


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )