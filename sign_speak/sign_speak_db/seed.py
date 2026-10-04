# seed.py

from database import init_database, add_sign


# =========================================================
# INITIAL SIGN DATA
# =========================================================

SIGNS = [
    # -------------------------
    # Greetings
    # -------------------------
    {
        "name": "Hello",
        "category": "Greetings",
        "description": "A common greeting.",
        "image": "hello.png"
    },
    {
        "name": "Goodbye",
        "category": "Greetings",
        "description": "Used when leaving or saying goodbye.",
        "image": "goodbye.png"
    },
    {
        "name": "Thank You",
        "category": "Greetings",
        "description": "Used to express thanks.",
        "image": "thank-you.png"
    },
    {
        "name": "Please",
        "category": "Greetings",
        "description": "Used when making a polite request.",
        "image": "please.png"
    },
    {
        "name": "Sorry",
        "category": "Greetings",
        "description": "Used to express an apology.",
        "image": "sorry.png"
    },
    {
        "name": "Welcome",
        "category": "Greetings",
        "description": "Used to welcome someone.",
        "image": "welcome.png"
    },

    # -------------------------
    # Alphabet
    # -------------------------
    {
        "name": "A",
        "category": "Alphabet",
        "description": "Sign for the letter A.",
        "image": "a.png"
    },
    {
        "name": "B",
        "category": "Alphabet",
        "description": "Sign for the letter B.",
        "image": "b.png"
    },
    {
        "name": "C",
        "category": "Alphabet",
        "description": "Sign for the letter C.",
        "image": "c.png"
    },
    {
        "name": "D",
        "category": "Alphabet",
        "description": "Sign for the letter D.",
        "image": "d.png"
    },
    {
        "name": "E",
        "category": "Alphabet",
        "description": "Sign for the letter E.",
        "image": "e.png"
    },
    {
        "name": "F",
        "category": "Alphabet",
        "description": "Sign for the letter F.",
        "image": "f.png"
    },
    {
        "name": "G",
        "category": "Alphabet",
        "description": "Sign for the letter G.",
        "image": "g.png"
    },
    {
        "name": "H",
        "category": "Alphabet",
        "description": "Sign for the letter H.",
        "image": "h.png"
    },
    {
        "name": "I",
        "category": "Alphabet",
        "description": "Sign for the letter I.",
        "image": "i.png"
    },
    {
        "name": "J",
        "category": "Alphabet",
        "description": "Sign for the letter J.",
        "image": "j.png"
    },
    {
        "name": "K",
        "category": "Alphabet",
        "description": "Sign for the letter K.",
        "image": "k.png"
    },
    {
        "name": "L",
        "category": "Alphabet",
        "description": "Sign for the letter L.",
        "image": "l.png"
    },
    {
        "name": "M",
        "category": "Alphabet",
        "description": "Sign for the letter M.",
        "image": "m.png"
    },
    {
        "name": "N",
        "category": "Alphabet",
        "description": "Sign for the letter N.",
        "image": "n.png"
    },
    {
        "name": "O",
        "category": "Alphabet",
        "description": "Sign for the letter O.",
        "image": "o.png"
    },
    {
        "name": "P",
        "category": "Alphabet",
        "description": "Sign for the letter P.",
        "image": "p.png"
    },
    {
        "name": "Q",
        "category": "Alphabet",
        "description": "Sign for the letter Q.",
        "image": "q.png"
    },
    {
        "name": "R",
        "category": "Alphabet",
        "description": "Sign for the letter R.",
        "image": "r.png"
    },
    {
        "name": "S",
        "category": "Alphabet",
        "description": "Sign for the letter S.",
        "image": "s.png"
    },
    {
        "name": "T",
        "category": "Alphabet",
        "description": "Sign for the letter T.",
        "image": "t.png"
    },
    {
        "name": "U",
        "category": "Alphabet",
        "description": "Sign for the letter U.",
        "image": "u.png"
    },
    {
        "name": "V",
        "category": "Alphabet",
        "description": "Sign for the letter V.",
        "image": "v.png"
    },
    {
        "name": "W",
        "category": "Alphabet",
        "description": "Sign for the letter W.",
        "image": "w.png"
    },
    {
        "name": "X",
        "category": "Alphabet",
        "description": "Sign for the letter X.",
        "image": "x.png"
    },
    {
        "name": "Y",
        "category": "Alphabet",
        "description": "Sign for the letter Y.",
        "image": "y.png"
    },
    {
        "name": "Z",
        "category": "Alphabet",
        "description": "Sign for the letter Z.",
        "image": "z.png"
    },

    # -------------------------
    # Numbers
    # -------------------------
    {
        "name": "1",
        "category": "Numbers",
        "description": "Sign for number one.",
        "image": "1.png"
    },
    {
        "name": "2",
        "category": "Numbers",
        "description": "Sign for number two.",
        "image": "2.png"
    },
    {
        "name": "3",
        "category": "Numbers",
        "description": "Sign for number three.",
        "image": "3.png"
    },
    {
        "name": "4",
        "category": "Numbers",
        "description": "Sign for number four.",
        "image": "4.png"
    },
    {
        "name": "5",
        "category": "Numbers",
        "description": "Sign for number five.",
        "image": "5.png"
    },
    {
        "name": "6",
        "category": "Numbers",
        "description": "Sign for number six.",
        "image": "6.png"
    },
    {
        "name": "7",
        "category": "Numbers",
        "description": "Sign for number seven.",
        "image": "7.png"
    },
    {
        "name": "8",
        "category": "Numbers",
        "description": "Sign for number eight.",
        "image": "8.png"
    },
    {
        "name": "9",
        "category": "Numbers",
        "description": "Sign for number nine.",
        "image": "9.png"
    },
    {
        "name": "10",
        "category": "Numbers",
        "description": "Sign for number ten.",
        "image": "10.png"
    },

    # -------------------------
    # Common Phrases
    # -------------------------
    {
        "name": "How Are You",
        "category": "Phrases",
        "description": "A phrase used to ask about someone's well-being.",
        "image": "how-are-you.png"
    },
    {
        "name": "Nice to Meet You",
        "category": "Phrases",
        "description": "Used when meeting someone for the first time.",
        "image": "nice-to-meet-you.png"
    },
    {
        "name": "What Is Your Name",
        "category": "Phrases",
        "description": "Used to ask someone's name.",
        "image": "what-is-your-name.png"
    },
    {
        "name": "My Name Is",
        "category": "Phrases",
        "description": "Used when introducing yourself.",
        "image": "my-name-is.png"
    },
    {
        "name": "See You Later",
        "category": "Phrases",
        "description": "Used when saying goodbye temporarily.",
        "image": "see-you-later.png"
    },
    {
        "name": "Help",
        "category": "Phrases",
        "description": "Used to ask for assistance.",
        "image": "help.png"
    },
    {
        "name": "Yes",
        "category": "Phrases",
        "description": "Used to indicate agreement.",
        "image": "yes.png"
    },
    {
        "name": "No",
        "category": "Phrases",
        "description": "Used to indicate disagreement or refusal.",
        "image": "no.png"
    },
    {
        "name": "Friend",
        "category": "Phrases",
        "description": "Used to refer to a friend.",
        "image": "friend.png"
    },
    {
        "name": "Family",
        "category": "Phrases",
        "description": "Used to refer to family.",
        "image": "family.png"
    },
    {
        "name": "Water",
        "category": "Phrases",
        "description": "Sign for water.",
        "image": "water.png"
    },
    {
        "name": "Eat",
        "category": "Phrases",
        "description": "Sign for eating.",
        "image": "eat.png"
    },
    {
        "name": "Drink",
        "category": "Phrases",
        "description": "Sign for drinking.",
        "image": "drink.png"
    },
    {
        "name": "Home",
        "category": "Phrases",
        "description": "Sign for home.",
        "image": "home.png"
    },

    # -------------------------
    # Emotions
    # -------------------------
    {
        "name": "Happy",
        "category": "Emotions",
        "description": "Expresses happiness.",
        "image": "happy.png"
    },
    {
        "name": "Sad",
        "category": "Emotions",
        "description": "Expresses sadness.",
        "image": "sad.png"
    },
    {
        "name": "Angry",
        "category": "Emotions",
        "description": "Expresses anger.",
        "image": "angry.png"
    },
    {
        "name": "Scared",
        "category": "Emotions",
        "description": "Expresses fear.",
        "image": "scared.png"
    },
    {
        "name": "Excited",
        "category": "Emotions",
        "description": "Expresses excitement.",
        "image": "excited.png"
    },
    {
        "name": "Love",
        "category": "Emotions",
        "description": "Expresses love or affection.",
        "image": "love.png"
    },
    {
        "name": "Tired",
        "category": "Emotions",
        "description": "Expresses tiredness.",
        "image": "tired.png"
    },
    {
        "name": "Confused",
        "category": "Emotions",
        "description": "Expresses confusion.",
        "image": "confused.png"
    },

    # -------------------------
    # Common Words
    # -------------------------
    {
        "name": "Who",
        "category": "Common Words",
        "description": "Used to ask about a person.",
        "image": "who.png"
    },
    {
        "name": "Where",
        "category": "Common Words",
        "description": "Used to ask about a location.",
        "image": "where.png"
    },
    {
        "name": "When",
        "category": "Common Words",
        "description": "Used to ask about time.",
        "image": "when.png"
    },
    {
        "name": "Why",
        "category": "Common Words",
        "description": "Used to ask for a reason.",
        "image": "why.png"
    },
    {
        "name": "How",
        "category": "Common Words",
        "description": "Used to ask about a method or condition.",
        "image": "how.png"
    },
    {
        "name": "More",
        "category": "Common Words",
        "description": "Used to ask for additional quantity.",
        "image": "more.png"
    },
    {
        "name": "Stop",
        "category": "Common Words",
        "description": "Used to indicate stopping.",
        "image": "stop.png"
    },
    {
        "name": "Go",
        "category": "Common Words",
        "description": "Used to indicate movement.",
        "image": "go.png"
    },
    {
        "name": "Good",
        "category": "Common Words",
        "description": "Expresses something positive.",
        "image": "good.png"
    },
    {
        "name": "Bad",
        "category": "Common Words",
        "description": "Expresses something negative.",
        "image": "bad.png"
    },
    {
        "name": "Learn",
        "category": "Common Words",
        "description": "Related to gaining knowledge.",
        "image": "learn.png"
    },
    {
        "name": "Understand",
        "category": "Common Words",
        "description": "Indicates understanding.",
        "image": "understand.png"
    },
    {
        "name": "Work",
        "category": "Common Words",
        "description": "Related to work or employment.",
        "image": "work.png"
    },
    {
        "name": "Play",
        "category": "Common Words",
        "description": "Related to playing.",
        "image": "play.png"
    },
    {
        "name": "Time",
        "category": "Common Words",
        "description": "Related to time.",
        "image": "time.png"
    },
    {
        "name": "Day",
        "category": "Common Words",
        "description": "Refers to a day.",
        "image": "day.png"
    },
    {
        "name": "Night",
        "category": "Common Words",
        "description": "Refers to nighttime.",
        "image": "night.png"
    },
    {
        "name": "Today",
        "category": "Common Words",
        "description": "Refers to the current day.",
        "image": "today.png"
    },
    {
        "name": "Tomorrow",
        "category": "Common Words",
        "description": "Refers to the following day.",
        "image": "tomorrow.png"
    },
    {
        "name": "Yesterday",
        "category": "Common Words",
        "description": "Refers to the previous day.",
        "image": "yesterday.png"
    }
]


# =========================================================
# SEED DATABASE
# =========================================================

def seed_database():
    """Insert initial SignSpeak data into the database."""

    print("Initializing SignSpeak database...")

    # Make sure tables exist
    init_database()

    inserted = 0

    for sign in SIGNS:
        try:
            add_sign(
                name=sign["name"],
                category=sign["category"],
                description=sign["description"],
                image=sign["image"]
            )

            inserted += 1

        except Exception as error:
            print(
                f"Could not add sign "
                f"'{sign['name']}': {error}"
            )

    print(f"Database seeding completed.")
    print(f"Signs processed: {inserted}")


# =========================================================
# RUN SEED SCRIPT
# =========================================================

if __name__ == "__main__":
    seed_database()
    