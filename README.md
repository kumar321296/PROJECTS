

🧠 Python Mini Projects

This repository contains three beginner-friendly Python projects that showcase different functionalities — from games to voice-controlled assistants. Each project is self-contained and demonstrates fundamental programming concepts.

📁 Projects
1. 🎯 Guess the Number (CLI Game)

A terminal-based guessing game where the user tries to guess a randomly selected number between 1 and 100.

📌 Features

Random number generation

Unlimited guesses

Input validation

Feedback for each attempt

▶️ Run the Game
python guess_the_number.py

2. 🐍 Snake Game (Turtle Graphics)

A classic Snake game made with Python’s turtle graphics module. Eat food, grow your snake, and avoid collisions with the walls or yourself.

📌 Features

Real-time movement with arrow keys

Score and high score tracking

Snake grows after eating food

Restarts automatically on collision

▶️ Run the Game
python snake_game.py


💡 Make sure your screen supports GUI rendering (not compatible with pure terminal environments like some SSH sessions).

3. 🗣️ Vani - Voice Assistant

Vani is a voice-controlled assistant that can open local apps and popular websites based on your spoken commands.

📌 Features

Voice recognition (speech_recognition)

Text-to-speech feedback (pyttsx3)

Opens common apps like Notepad, Chrome, VS Code, etc.

Opens websites like Google and YouTube

Tracks opened apps/websites to avoid duplicates

🛠 Requirements
pip install speechrecognition pyttsx3
pip install pipwin
pipwin install pyaudio


✅ Make sure your microphone is enabled and working.

▶️ Run the Assistant
python vani_voice_assistant.py
