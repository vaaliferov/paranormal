#!/usr/bin/env python3

import json
import pickle
import numpy as np
import pandas as pd
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler


classes = [
    'negative', 
    'positive'
]

columns = [
    'age',
    'gender',
    'polyuria',
    'polydipsia',
    'sudden_weight_loss',
    'weakness',
    'polyphagia',
    'genital_thrush',
    'visual_blurring',
    'itching',
    'irritability',
    'delayed_healing',
    'partial_paresis',
    'muscle_stiffness',
    'alopecia',
    'obesity'
]

questions = [
    ['age?', int, 0, 120, None],
    ['gender? (male / female)', str, None, None, ['male','female']],
    ['polyuria? (yes / no)', str, None, None, ['yes','no']],
    ['polydipsia? (yes / no)', str, None, None, ['yes','no']],
    ['sudden_weight_loss? (yes / no)', str, None, None, ['yes','no']],
    ['weakness? (yes / no)', str, None, None, ['yes','no']],
    ['polyphagia? (yes / no)', str, None, None, ['yes','no']],
    ['genital_thrush? (yes / no)', str, None, None, ['yes','no']],
    ['visual_blurring? (yes / no)', str, None, None, ['yes','no']],
    ['itching? (yes / no)', str, None, None, ['yes','no']],
    ['irritability? (yes / no)', str, None, None, ['yes','no']],
    ['delayed_healing? (yes / no)', str, None, None, ['yes','no']],
    ['partial_paresis? (yes / no)', str, None, None, ['yes','no']],
    ['muscle_stiffness? (yes / no)', str, None, None, ['yes','no']],
    ['alopecia? (yes / no)', str, None, None, ['yes','no']],
    ['obesity? (yes / no)', str, None, None, ['yes','no']]
]

answers = {}


def check_answer(q, m):
    
    if q[1] == int:
        try: m = int(m)
        except: return None
    
    if (q[2] is not None) and (m < q[2]): return None
    if (q[3] is not None) and (m > q[3]): return None
    if (q[4] is not None) and (m not in q[4]): return None
    return m


def handle_text(update, context):

    text = update.message.text
    chat_id = update.message.chat_id
    
    if text == '/start':
        answers[chat_id] = []
        update.message.reply_text(questions[0][0])
    
    elif chat_id in answers:
        
        if len(answers[chat_id]) < len(questions):
            q = questions[len(answers[chat_id])]
            a = check_answer(q, text.lower())
            if a is not None: answers[chat_id].append(a)
        
        if len(answers[chat_id]) < len(questions):
            update.message.reply_text(questions[len(answers[chat_id])][0])
        
        else:
            data = pd.DataFrame([answers[chat_id]], columns=columns)
            data.replace({'male':1,'female':0}, inplace=True)
            data.replace({'yes':1,'no':0}, inplace=True)
            probas = model.predict_proba(data)[:,1]
            predicted = model.predict(data)
            update.message.reply_text(f'{classes[predicted[0]]} ({probas[0]:.4f})')


model = pickle.load(open('ext_random_forest.pkl', 'rb'))
opt = json.load(open('config.json','r'))
updater = Updater(opt['bot_token'])
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, handle_text))
updater.start_polling()
updater.idle()