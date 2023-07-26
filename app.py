from flask import Flask, render_template, request, flash
import university_chatbot

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

chat_history = []

@app.route("/")
@app.route("/chat", methods=['POST', 'GET'])
def chat():
    if 'question_input' not in request.form:
        return render_template("index.html", chat_history=chat_history)
    if chat_history == []:
        chat_history.append("Hello, I'm the Staffs Uni chatbot. How can I help you?")
    user_input = request.form['question_input']
    chat_history.append(user_input)
    response = university_chatbot.process_user_input(user_input)
    chat_history.append(response)
    flash(response)
    # if request.form.get('clear_history'):
    #     return render_template("index.html", chat_history=[])
       
    return render_template("index.html", chat_history=chat_history)


if __name__ == '__main__':
    app.run(debug=True)