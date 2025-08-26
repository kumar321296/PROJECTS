import pyautogui
import time

def get_auto_reply(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm an AI chatbot, so I'm always good! How can I assist you?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("AI Chatbot (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        reply = get_auto_reply(user_input)
        print("Bot:", reply)
        # Wait 2 seconds to switch to the chat window
        time.sleep(2)
        pyautogui.typewrite(reply)
        pyautogui.press('enter')
        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    main()