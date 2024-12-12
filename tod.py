from flask import Flask, jsonify, render_template_string
import requests
import random
import os

app = Flask(__name__)

# API Endpoints for fetching questions
TRUTH_API_URL = "https://opentdb.com/api.php?amount=1&category=9&type=multiple"
DARE_API_URL = "https://api.chucknorris.io/jokes/random"

FUNNY_TRUTHS = [
    "What is the most embarrassing thing you've ever done?",
    "If you could be invisible, what's the first thing you'd do?",
    "Who was your first crush?",
    "Have you ever lied to your best friend?",
    "What's the weirdest dream you've ever had?",
    "If you could swap lives with someone for a day, who would it be?",
    "What's the most childish thing you still do?",
    "Have you ever been caught doing something you shouldn't?",
    "If you had to marry one person in this room, who would it be?",
    "What is your biggest fear?",
    "What's the last thing you searched for on your phone?",
    "If you had to delete one app from your phone, what would it be?",
    "What's your guilty pleasure?",
    "Who is your celebrity crush?",
    "Have you ever cheated on a test?",
    "What's the worst haircut you've ever had?",
    "Have you ever stolen something?",
    "What's a secret you've never told anyone?",
    "What would you do if you were the opposite gender for a day?",
    "What's your worst habit?",
    "What's the dumbest thing you've ever said?",
    "What's the craziest thing you've ever done?",
    "What's your worst fear in a relationship?",
    "What's the most embarrassing thing you've done for someone you love?",
    "Have you ever had a wardrobe malfunction?",
    "Have you ever accidentally sent a text to the wrong person?",
    "What's the most embarrassing thing you've posted on social media?",
    "Have you ever been rejected by someone?",
    "What is your dream job?",
    "Have you ever peed in a pool?",
    "What is something you've never told your parents?",
    "What's the most annoying habit someone else has?",
    "If you could live anywhere in the world, where would it be?",
    "What is the most expensive thing you've ever bought?",
    "Have you ever laughed at the wrong moment?",
    "What's the most awkward date you've ever been on?",
    "What's the craziest thing you've done while drunk?",
    "Who in this room do you trust the least?",
    "Have you ever eavesdropped on a conversation?",
    "If you could time travel, where would you go?",
    "What's the worst gift you've ever received?",
    "Have you ever pretended to like a gift?",
    "What's your biggest regret?",
    "What's the worst lie you've ever told?",
    "If you had to eat one food for the rest of your life, what would it be?",
    "Have you ever skipped school or work?",
    "What's the weirdest thing you've ever eaten?",
    "What's the most embarrassing thing you've done in front of a crush?",
    "Have you ever had a crush on a teacher?",
    "What's the longest you've gone without showering?",
    "What's the weirdest thing you've ever bought?",
    "Have you ever danced in front of a mirror?",
    "What's a song that you're embarrassed to admit you like?",
    "Have you ever talked to yourself out loud?",
    "What's your most irrational fear?",
    "If you could switch lives with anyone in this room, who would it be?",
    "What's the most embarrassing thing you've said in public?",
    "Have you ever been caught singing in the shower?",
    "What's your favorite guilty pleasure TV show?",
    "Have you ever sent a text you regret?",
    "What's the most embarrassing thing in your room?",
    "Have you ever lied to get out of trouble?",
    "What's the most ridiculous thing you've done on a dare?",
    "Have you ever broken a bone?",
    "What's the weirdest thing you've done when you were alone?",
    "Have you ever been caught picking your nose?",
    "What's the most ridiculous thing you've cried over?",
    "Have you ever stalked someone on social media?",
    "What's the most awkward text you've received?",
    "What's the most embarrassing photo you have?",
    "Have you ever pretended to be sick to get out of something?",
    "What's your worst cooking disaster?",
    "What's the silliest thing you're afraid of?",
    "Have you ever walked into something while texting?",
    "What's the most embarrassing thing you've worn?",
    "What's your biggest pet peeve?",
    "If you could trade lives with a fictional character, who would it be?",
    "Have you ever accidentally said 'I love you' to someone?",
    "What's the most awkward moment you've ever had?",
    "Have you ever tripped in public?",
    "What's your biggest insecurity?",
    "Have you ever had a crush on someone older than you?",
    "What's the dumbest thing you've ever done in public?",
    "What's the most awkward thing you've done on a date?",
    "Have you ever lied to a teacher?",
    "What's the weirdest thing you've done with your hair?",
    "Have you ever been caught cheating on a test?",
    "What's the most annoying thing about your best friend?",
    "Have you ever been caught snooping through someone's stuff?",
    "If you could erase one embarrassing moment from your past, what would it be?",
    "What's the most awkward question you've been asked?",
    "Have you ever been caught in a lie?",
    "What's the most ridiculous thing you've done for attention?",
    "Have you ever had an imaginary friend?",
    "What's the weirdest thing you've done while bored?",
    "What's your most embarrassing nickname?",
    "What's the most ridiculous rule you've broken?",
    "Have you ever been caught talking about someone behind their back?",
    "What's the worst thing you've ever eaten?"
]

FUNNY_DARES = [
    "Do your best chicken dance outside on the street.",
    "Sing the chorus of your favorite song in a funny voice.",
    "Act like a monkey until it's your turn again.",
    "Try to lick your elbow.",
    "Speak in an accent for the next 3 rounds.",
    "Do 10 pushups and yell 'I'm strong!' after each one.",
    "Wear socks on your hands until your next turn.",
    "Dance with no music for 1 minute.",
    "Talk like a robot for the next 5 minutes.",
    "Do an impression of your favorite cartoon character.",
    "Let the person next to you redo your hairstyle.",
    "Pretend you're a waiter/waitress and take snack orders from everyone in the room.",
    "Do the worm dance.",
    "Call a friend and sing 'Happy Birthday' to them.",
    "Let someone tickle you for 30 seconds.",
    "Try to juggle 3 items chosen by the group.",
    "Speak in a different language (or gibberish) for the next 2 minutes.",
    "Walk like a runway model across the room and back.",
    "Talk without using your lips for the next 3 rounds.",
    "Let the group give you a new nickname and use it for the rest of the game.",
    "Hop on one foot for the next 5 minutes.",
    "Spin around 10 times and then try to walk in a straight line.",
    "Do an impression of your favorite celebrity until someone guesses who you are.",
    "Pretend you're a cheerleader and create a cheer for the group.",
    "Wear a hat made out of toilet paper for the next 2 rounds.",
    "Try to touch your toes without bending your knees.",
    "Do your best animal impression.",
    "Sing everything you say for the next 10 minutes.",
    "Draw a mustache on your face with lipstick and keep it there for the next hour.",
    "Do a stand-up comedy routine for 2 minutes.",
    "Speak in rhymes for the next 3 rounds.",
    "Pretend to be a statue for the next 2 minutes.",
    "Do 20 jumping jacks in slow motion.",
    "Act like you're underwater for the next 3 rounds.",
    "Do your best impersonation of someone in the group.",
    "Pretend to be a dog and fetch something.",
    "Try to balance a spoon on your nose for 10 seconds.",
    "Let the group write something on your forehead with a marker.",
    "Try to do a handstand.",
    "Make up a rap about the group.",
    "Pretend to be a superhero and describe your powers.",
    "Let someone style your hair however they want.",
    "Act like a baby until your next turn.",
    "Sing the chorus of a song with water in your mouth.",
    "Make the most annoying sound you can for 10 seconds.",
    "Pretend to be an alien and introduce yourself to the group.",
    "Try to do 10 squats while holding a heavy object chosen by the group.",
    "Do your best imitation of a zombie.",
    "Speak in a high-pitched voice for the next 3 minutes.",
    "Let the group create a new hairstyle for you and keep it for the next 2 rounds.",
    "Dance like nobody's watching for 2 minutes.",
    "Try to say the alphabet backward as fast as you can.",
    "Pretend to be a waiter and take fake orders from the group.",
    "Do your best impression of a dinosaur.",
    "Let someone draw a tattoo on your arm with a pen.",
    "Try to keep a straight face while the group tries to make you laugh.",
    "Do your best opera singing for 1 minute.",
    "Pretend to be a newscaster and give the daily news.",
    "Try to whistle a song chosen by the group.",
    "Let the group choose an emoji and make that face until your next turn.",
    "Try to balance a book on your head while walking across the room.",
    "Pretend you're a flight attendant and give safety instructions.",
    "Do your best impression of a celebrity on the red carpet.",
    "Try to eat a snack without using your hands.",
    "Pretend to be a robot for the next 5 minutes.",
    "Do a dramatic reading of a nursery rhyme.",
    "Let someone create a fake social media post for you.",
    "Try to stand on one leg for the next 2 minutes.",
    "Make up a song about the group and sing it.",
    "Let someone paint your nails any color they choose.",
    "Do your best impression of a TV show character.",
    "Try to keep your eyes crossed for 30 seconds.",
    "Pretend to be a teacher and give a lesson on a random topic.",
    "Do a dance like you're in a musical.",
    "Try to carry on a conversation using only movie quotes.",
    "Pretend to be a cat for the next 2 minutes.",
    "Try to make up a story using all the items in the room.",
    "Let the group create a nickname for you and use it for the rest of the game.",
    "Try to sing a song while holding your tongue.",
    "Do your best impression of someone in the room.",
    "Try to do a cartwheel or somersault.",
    "Do an impression of your favorite animal.",
    "Let the group create a new signature dance move for you and perform it.",
    "Pretend to be a pirate and talk like one until your next turn.",
    "Try to balance a broom on your hand for 10 seconds.",
    "Pretend to be a chef and describe a crazy recipe.",
    "Do your best runway walk across the room.",
    "Try to do 10 pushups while someone counts out loud.",
    "Do your best impression of a chicken until someone guesses what you are.",
    "Try to walk across the room while balancing a cup of water on your head.",
    "Let the group choose a word, and you must say it in every sentence for the next 5 minutes.",
    "Pretend to be a waiter and serve an imaginary meal to everyone in the room.",
    "Act like you’re underwater until your next turn.",
    "Stand on one leg and sing the national anthem.",
    "Speak in Shakespearean English for the next 3 rounds.",
    "Wear a funny hat (or create one) for the rest of the game.",
    "Mime an entire scene from your favorite movie and let others guess it.",
    "Do your best impression of a baby learning to walk.",
    "Let someone draw a mustache on your face using eyeliner or marker.",
    "Pretend to be a rockstar and perform a 1-minute concert.",
    "Spin around 10 times, then try to walk in a straight line.",
    "Pretend you are on a cooking show and describe how to make a peanut butter sandwich.",
    "Act like a mime stuck in a box until your next turn."
]

# Function to fetch data from APIs
def fetch_from_api(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        if api_url == TRUTH_API_URL:
            return data["results"][0]["question"]
        elif api_url == DARE_API_URL:
            return data["value"]  
        else:
            return "Invalid API response."
    except Exception as e:
        return f"Error connecting to the API: {e}"

# Flask routes
@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Truth or Dare</title>
        <style>
            body {
                font-family: 'Comic Sans MS', cursive, sans-serif;
                text-align: center;
                background: url('https://images.unsplash.com/photo-1585578911801-e4f8582859a8?q=80&w=2035&auto=format&fit=crop') no-repeat center center fixed;
                background-size: cover;
                margin: 0;
                padding: 0;
                color: white;
                overflow: hidden;
            }
            .container {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                padding: 20px;
                background: rgba(0, 0, 0, 0.5);
                border-radius: 20px;
                margin: auto;
            }
            .button {
                background-color: #f48fb1;
                color: white;
                padding: 15px 30px;
                margin: 10px;
                border: none;
                cursor: pointer;
                border-radius: 50px;
                font-size: 20px;
                transition: all 0.3s ease;
                box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
            }
            .button:hover {
                transform: translateY(-5px);
                box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.3);
                background-color: #ec407a;
            }
            .loader {
                border: 4px solid #f3f3f3;
                border-top: 4px solid #ec407a;
                border-radius: 50%;
                width: 20px;
                height: 20px;
                animation: spin 1s linear infinite;
                display: inline-block;
                margin-left: 10px;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            .result {
                margin-top: 20px;
                font-size: 20px;
                color: #fff;
                background: rgba(0, 0, 0, 0.6);
                padding: 15px;
                border-radius: 10px;
                animation: fadeIn 1s ease-in-out;
            }
            .avatar {
                width: 150px;
                height: 150px;
                background: url('https://cdn-icons-png.flaticon.com/512/190/190614.png') no-repeat center center;
                background-size: contain;
                margin-bottom: 15px;
                animation: bounce 2s infinite;
            }
            @keyframes bounce {
                0%, 100% {
                    transform: translateY(0);
                }
                50% {
                    transform: translateY(-10px);
                }
            }
            .bottle {
                width: 120px;
                height: 120px;
                background: url('https://cdn-icons-png.flaticon.com/512/168/168748.png') no-repeat center center;
                background-size: contain;
                animation: none;
                margin: 20px auto;
            }
            .spin {
                animation: spinBottle 3s ease-in-out;
            }
            @keyframes spinBottle {
                from { transform: rotate(0deg); }
                to { transform: rotate(360deg); }
            }
             footer {
                margin-top: 20px;
                color: #fff;
                font-size: 16px;
                padding: 10px;
                border-radius: 10px;
                width: 25%;
                text-align: center;
                position: fixed;
                bottom: 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="avatar"></div>
            <h1>Truth or Dare Game</h1>
            <button class="button" onclick="spinBottle()">Spin the Bottle</button>
            <div class="bottle" id="bottle"></div>
            <div class="result" id="result"></div>
        </div>
        <footer>
            Built with ❤️ by Ram for fun!
        </footer>
        <script>
            function spinBottle() {
                const bottle = document.getElementById('bottle');
                bottle.classList.add('spin');
                setTimeout(() => {
                    bottle.classList.remove('spin');
                    const randomChoice = Math.random() < 0.5 ? 'truth' : 'dare';
                    fetch('/' + randomChoice)
                        .then(response => response.json())
                        .then(data => {
                            document.getElementById('result').innerText = data.result;
                        })
                        .catch(() => {
                            document.getElementById('result').innerText = 'Error fetching task.';
                        });
                }, 3000);
            }
        </script>
    </body>
    </html>
    """)

@app.route('/truth')
def get_truth():
    question = random.choice(FUNNY_TRUTHS)
    return jsonify({"result": question})

@app.route('/dare')
def get_dare():
    activity = random.choice(FUNNY_DARES)
    return jsonify({"result": activity})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


