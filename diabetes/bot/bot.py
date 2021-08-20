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
    ['Укажите Ваш возраст?', int, 0, 120, None],
    ['Ваш пол? (м / ж)', str, None, None, ['м','ж']],
    ['Есть ли у Вас симптомы полиурии (увеличенное образование мочи)? (Да / Нет)', str, None, None, ['Да','Нет']],
    ['Испытываете ли Вы неутолимую жажду?? (Да / Нет)', str, None, None, ['Да','Нет']],
    ['Наблюдается ли у Вас внезапная потеря веса? (Да / Нет)', str, None, None, ['Да','Нет']],
    ['Испытываете ли слабость? (Да / Нет)', str, None, None, ['Да','Нет']],
    ['Наблюдаете ли у себя повышенный аппетит? (Да / Нет)', str, None, None, ['Да','Нет']],
    ['Генитальная молочница? (Да / Нет)', str, None, None, ['Да','Нет']],
    ['Расплывчатость зрения? (Да / Нет)', str, None, None, ['Да','Нет']],
    ['Зуд? (Да / Нет)', str, None, None, ['Да','Нет']],
    ['Раздражительность? (Да / Нет)', str, None, None, ['Да','Нет']],
    ['Медленное заживление ран? (Да / Нет)', str, None, None, ['Да','Нет']],
    ['Частичный парез (потеря мышечной силы)? (Да / Нет)', str, None, None, ['Да','Нет']],
    ['Жесткость мышц? (Да / Нет)', str, None, None, ['Да','Нет']],
    ['Усиленное выпадение волос? (Да / Нет)', str, None, None, ['Да','Нет']],
    ['Ожирение? (Да / Нет)', str, None, None, ['Да','Нет']]
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
            data.replace({'м':1,'ж':0}, inplace=True)
            data.replace({'Да':1,'Нет':0}, inplace=True)
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