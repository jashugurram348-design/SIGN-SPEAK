# SignSpeak

SignSpeak is a web application designed to help users learn and translate sign language. It provides a simple interface for text-to-sign translation, a sign dictionary, learning lessons, and translation history.

## Features

- Text-to-sign translation
- Sign language dictionary
- Search signs
- Filter signs by category
- Learning section
- Translation history
- Camera access for future sign recognition
- Responsive dark-themed user interface
- Flask backend API
- REST API endpoints for sign data and translation

## Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Flask
- REST API

### Storage

- Browser Local Storage
- SQLite can be added for persistent backend storage

## Project Structure

```text
SignSpeak/
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── dictionary.html
│   ├── history.html
│   └── learn.html
│
└── static/
    ├── style.css
    └── script.js