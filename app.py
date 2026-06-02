from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "chatbot_secret_key"

def chatbot_response(user_message):
    user_message = user_message.lower()

    if "hello" in user_message or "hi" in user_message:
        return "Hello! How can I help you?"
    elif "your name" in user_message or "who are you" in user_message:
        return "I am a simple AI chatbot created using Flask."
    elif "how are you" in user_message:
        return "I am doing great! Thanks for asking."
    elif "bye" in user_message or "goodbye" in user_message:
        return "Goodbye! Have a nice day!"
    elif "python" in user_message:
        return "Python is used for web development, AI, ML, and automation."
    elif "flask" in user_message:
        return "Flask is a lightweight Python framework used to build web apps."
    elif "ai" in user_message or "artificial intelligence" in user_message:
        return "AI allows machines to perform tasks that need human intelligence."
    elif "machine learning" in user_message or "ml" in user_message:
        return "Machine Learning helps computers learn patterns from data."
    elif "github" in user_message:
        return "GitHub is used to store, manage, and share code."
    elif "help" in user_message:
        return "You can ask me about Python, Flask, AI, ML, GitHub, or resume tips."
    else:
        return "I am still learning. Please ask me about Python, Flask, AI, ML, or GitHub."

@app.route("/", methods=["GET", "POST"])
def home():
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        user_message = request.form["message"]
        bot_reply = chatbot_response(user_message)

        session["chat_history"].append({
            "user": user_message,
            "bot": bot_reply
        })
        session.modified = True

    return render_template("index.html", chat_history=session["chat_history"])

@app.route("/clear")
def clear():
    session.pop("chat_history", None)
    return render_template("index.html", chat_history=[])

if __name__ == "__main__":
    app.run(debug=True)