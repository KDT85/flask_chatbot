from flask import Flask, render_template, request, flash
import university_chatbot

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

chat_history = []

# @app.route("/hello")
# def index():
#     flash("what's your name?")
#     return render_template("index.html", chat_history=chat_history)
# @app.route("/")
# def index():
#     return render_template("index.html", chat_history=chat_history)

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
    if 'name_input' not in request.form:
        return render_template("index.html", chat_history=chat_history)
    user_input = request.form['name_input']
    chat_history.append(user_input)
    response = university_chatbot.process_user_input(user_input)
    chat_history.append(response)
    flash(response)
    # if request.form.get('clear_history'):
    #     chat_history.clear()
       
    return render_template("index.html", chat_history=chat_history)


if __name__ == '__main__':
    app.run(debug=True)