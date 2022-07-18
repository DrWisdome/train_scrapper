from train.train_delay import TrainDelay
import requests
import train.list_trains as const
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    with TrainDelay() as bot:
        for i in range(0, 8):
            bot.land_first_page()
            bot.find_train(i)
            bot.find_delay_time()
            return_string_header = "Čas: \t"+"Meškanie: "
            return_string_body = ""
            for i in range(len(bot.array)):
                return_string_body = const.times_of_trains[i]+ '\t' + " " + bot[array[i]] + '\n'
            return_string = return_string_header + return_string_body
    return return_string

