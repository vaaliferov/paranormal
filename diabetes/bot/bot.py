#!/usr/bin/env python3

import json
import pickle
import numpy as np
import pandas as pd
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler


l_yes = 'да'
l_no = 'нет'
l_male = 'м'
l_female = 'ж'
l_age = 'Укажите Ваш возраст?'
l_gender = 'Ваш пол? (м / ж)'
l_polyuria = 'Есть ли у Вас симптомы полиурии (увеличенное образование мочи)? (Да / Нет)'
l_polydipsia = 'Испытываете ли Вы неутолимую жажду? (Да / Нет)'
l_sudden_weight_loss = 'Наблюдается ли у Вас внезапная потеря веса? (Да / Нет)'
l_weakness = 'Испытываете ли слабость? (Да / Нет)'
l_polyphagia = 'Наблюдаете ли у себя повышенный аппетит? (Да / Нет)'
l_genital_thrush = 'Генитальная молочница? (Да / Нет)'
l_visual_blurring = 'Расплывчатость зрения? (Да / Нет)'
l_itching = 'Зуд? (Да / Нет)'
l_irritability = 'Раздражительность? (Да / Нет)'
l_delayed_healing = 'Медленное заживление ран? (Да / Нет)'
l_partial_paresis = 'Частичный парез (потеря мышечной силы)? (Да / Нет)'
l_muscle_stiffness = 'Жесткость мышц? (Да / Нет)'
l_alopecia = 'Усиленное выпадение волос? (Да / Нет)'
l_obesity = 'Ожирение? (Да / Нет)'
l_high_risk = 'Высокий риск наличия заболевания, рекомендуется пройти полное обследование'
l_low_risk = 'Низкий риск наличия заболевания, нет необходимости в прохождении полного обследования'


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
    [l_age, int, 0, 120, None],
    [l_gender, str, None, None, [l_male,l_female]],
    [l_polyuria, str, None, None, [l_yes,l_no]],
    [l_polydipsia, str, None, None, [l_yes,l_no]],
    [l_sudden_weight_loss, str, None, None, [l_yes,l_no]],
    [l_weakness, str, None, None, [l_yes,l_no]],
    [l_polyphagia, str, None, None, [l_yes,l_no]],
    [l_genital_thrush, str, None, None, [l_yes,l_no]],
    [l_visual_blurring, str, None, None, [l_yes,l_no]],
    [l_itching, str, None, None, [l_yes,l_no]],
    [l_irritability, str, None, None, [l_yes,l_no]],
    [l_delayed_healing, str, None, None, [l_yes,l_no]],
    [l_partial_paresis, str, None, None, [l_yes,l_no]],
    [l_muscle_stiffness, str, None, None, [l_yes,l_no]],
    [l_alopecia, str, None, None, [l_yes,l_no]],
    [l_obesity, str, None, None, [l_yes,l_no]]
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

        if chat_id != opt['bot_owner_id']:
            username = update.message.from_user.username
            context.bot.send_message(opt['bot_owner_id'], f'user @{username}')

    
    elif chat_id in answers:
        
        if len(answers[chat_id]) < len(questions):
            q = questions[len(answers[chat_id])]
            a = check_answer(q, text.lower())
            if a is not None: answers[chat_id].append(a)
        
        if len(answers[chat_id]) < len(questions):
            update.message.reply_text(questions[len(answers[chat_id])][0])
        
        else:
            data = pd.DataFrame([answers[chat_id]], columns=columns)
            data.replace({l_male:1,l_female:0}, inplace=True)
            data.replace({l_yes:1,l_no:0}, inplace=True)
            probas = model.predict_proba(data)[:,1]
            predicted = model.predict(data)
            msg = l_high_risk if predicted[0] == 1 else l_low_risk
            update.message.reply_text(f'{msg} ({probas[0]:.4f})')


model = pickle.load(open('ext_random_forest.pkl', 'rb'))
opt = json.load(open('config.json','r'))
updater = Updater(opt['bot_token'])
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, handle_text))
updater.start_polling()
updater.idle()