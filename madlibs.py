from random import choice, sample

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


# @app.route('/')
# def start_here():
#     """Homepage."""

#     return "Hi! This is the home page."


@app.route('/')
@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)
    compliment = sample(AWESOMENESS, 3)
    print compliment
    return render_template("compliment.html",
                           person=player,
                           compliments=compliment)

@app.route('/game')
def show_game_form():
    """Show the game"""

    want_to_play = request.args.get("game")
    print want_to_play

    if want_to_play == "yes":
        return render_template("game.html")

    else:
        return render_template("goodbye.html")

@app.route('/madlib', methods=["POST","GET"])
def show_madlib():
    """Shows the madlib"""

    print request.method

    
    person = request.form.get("first")
    favourite_color = request.form.get("color")
    person_noun = request.form.get("noun")
    adjective = request.form.get("theadjective")

    madlibs_html = ["madlib1.html", "madlib2.html", "madlib3.html" ]

    render_random = choice(madlibs_html)
    print render_random
    # print adjective
    return render_template(render_random,
                            name = person,
                            noun = person_noun,
                            color = favourite_color,
                            adjective = adjective
                            )

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
