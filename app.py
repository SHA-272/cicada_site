from flask import Flask, render_template, request, make_response
import requests, os, json, random

app = Flask(__name__)

API_KEY = os.environ.get(
    "CTFD_API_KEY",
    "ctfd_2c71a65dc478092a47cdebf982b250337ba33b3f15505001fd0dbec10f62b89e",
)
API_URL = f"""{os.environ.get("CTFD_URL", "https://krductf.ru")}/api/v1/challenges/{os.environ.get("CTFD_TASK_ID", 87)}/solves"""

headers = {
    "Authorization": f"Token {API_KEY}",
    "Content-Type": "application/json",
}


incorrect_responses = [
    "Congratulations! You must be a genius. Or not.",
    "Nice try! Maybe next time use your brain cells, they're there for a reason.",
    "Oh, come on! Even my pet rock could do better.",
    "Is this your first day using a computer, or are you just naturally clueless?",
    "Well, that was impressively wrong. Do you practice being this bad?",
    "Error 404: Correct answer not found. Try again... or not.",
    "Your answer is like a broken pencil - pointless.",
    "I've seen better answers from a magic 8-ball.",
    "If stupidity were a currency, you'd be a billionaire right now.",
    "Next time, maybe think twice before clicking randomly. Just a suggestion.",
    "That answer was so wrong, it's breaking my heart. Or maybe it's just breaking basic logic.",
    "If ignorance is bliss, you must be the happiest person on Earth right now.",
    "Did you consult a fortune cookie for that answer? Because it's not working like magic.",
    "I'm not saying your answer is wrong, but even a stopped clock is right twice a day.",
    "Your answer is wandering in the desert of correctness without a compass.",
    "Well, aren't you a master of misinformation!",
    "I've seen better decision-making in a game of rock-paper-scissors.",
    "If your brain was dynamite, it wouldn't have enough to blow your nose.",
    "Did you graduate from the University of Dunning-Kruger?",
    "That answer is so far from correct, it's practically in a different galaxy.",
    "Well, that wasn't even close. Maybe try guessing lottery numbers instead.",
    "If wrong answers were an art form, you'd be a Picasso.",
    "You must have a black belt in misinformation.",
    "Your answer is like a bad pun - painful for everyone involved.",
    "Is this a performance art piece titled 'The Failure Symphony'?",
    "I've seen better answers on the back of cereal boxes.",
    "Did you learn to count from playing hide and seek with the truth?",
    "Your answer is like a broken record - repetitive and annoying.",
    "In the world of correct answers, you're the unicorn - mythical and non-existent.",
    "If ignorance were a sport, you'd be an Olympic gold medalist.",
    "Can't you really just write 'secret'?",
    "Even cracking MD5 is easier.",
    "Search in the heavens.",
    "Maybe the answer is on page 404?",
    "Watch the movie 'Dark Web: Cicada 3301'",
]


questions = {
    "secret": "In cryptography, what is the term for a piece of information used to control the operation of an encryption algorithm?",
    "key": "What is the result of applying a cryptographic function to input data, producing a fixed-size string of characters?",
    "hash": "MD5: e48e13207341b6bffb7fb1622282247b",
    "1337": "What decentralized and distributed technology underlies cryptocurrencies, ensuring secure and transparent transactions?",
    "blockchain": "In cryptography, what is the measure of uncertainty or randomness in a system?",
    "entropy": "-- --- .-. --.. . ... . -.-. .-. . -",
    "morzesecret": "What type of attack involves trying all possible combinations of a password until the correct one is found?",
    "bruteforce": "What network security device monitors and controls incoming and outgoing network traffic based on predetermined security rules?",
    "firewall": "c3VwM3JzM2NyM3Q=",
    "sup3rs3cr3t": "https://cicada.krductf.ru/c98a679441798bdb9c194f9ca471e6cd",
    "vaultsecret": "https://cicada.krductf.ru/c4d34107574167d0d7df7edf1169012b",
    "letsbeatheaven": "https://cicada.krductf.ru/390f15df565c93c0a56e50b24dc0d5ec",
}

keys = list(questions.keys())
values = list(questions.values())

random.shuffle(keys)
random.shuffle(values)

responses = {key.lower(): value for key, value in zip(keys, values)}


@app.route("/")
def index():
    r = requests.get(API_URL, headers=headers)

    if r.status_code == 200:
        data = r.json()["data"]
        return render_template("index.html", users=data)
    else:
        return render_template("index.html")


@app.route("/327a6c4304ad5938eaf0efb6cc3e53dc")
def flag():
    return render_template("flag.html")


@app.route("/4eb5d6bd65ed1b4f5ac431b04a2cac1f", methods=["POST", "GET"])
def vault():
    user_input = request.form.get("user_input", "").lower()
    if user_input:
        response = questions.get(user_input, random.choice(incorrect_responses))
        return render_template("storage.html", response=response)
    else:
        return render_template("storage.html")


@app.route("/c98a679441798bdb9c194f9ca471e6cd")
def math():
    return render_template("math.html")


@app.route("/ee54449478c54a5a5cc4f774e3d4ba34")
def cookie():
    response = make_response(render_template("cookie.html"))
    response.set_cookie(
        "cookie",
        "aHR0cHM6Ly9jaWNhZGEua3JkdWN0Zi5ydS80OWUzYzE5ODMzMTFhMjc1ZmFkYzE1MDkxNDhmN2ZmMQ==",
    )
    return response


@app.route("/49e3c1983311a275fadc1509148f7ff1")
def star():
    return render_template("star.html")


@app.route("/c4d34107574167d0d7df7edf1169012b")
def music():
    return render_template("moonlight.html")


@app.route("/390f15df565c93c0a56e50b24dc0d5ec")
def qrcode():
    return render_template("qrcode.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
