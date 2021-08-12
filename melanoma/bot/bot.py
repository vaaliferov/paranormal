#!/usr/bin/env python3

import json
import numpy as np
import onnxruntime
from PIL import Image, ImageOps

from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler

def pad(im):
    w, h = im.size; m = np.max([w, h])
    hp, hpr = (m - w) // 2, (m - w) % 2
    vp, vpr = (m - h) // 2, (m - h) % 2
    return (hp + hpr, vp + vpr, hp, vp)

def norm(x):
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    return (x - mean) / std

def load_image(path, size):
    im = Image.open(path)
    im.thumbnail((size, size), Image.ANTIALIAS)
    im = ImageOps.expand(im, pad(im))
    return np.array(im) / 255.

def to_tensor(x):
    x = np.float32(norm(x))
    x = x.transpose(2,0,1)
    return x.reshape((1,) + x.shape)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def load_model(path):
    return onnxruntime.InferenceSession(path)

def predict(model, path):
    x = to_tensor(load_image(path, 224))
    inps = {model.get_inputs()[0].name: x}
    outs = model.run(None, inps)
    y = sigmoid(outs[0])[0][0]
    return int(y > 0.5), y

def handle_text(update, context):
    update.message.reply_text('waiting for photos...')

def handle_photo(update, context):
    file_id = update.message.photo[-1]['file_id']
    context.bot.getFile(file_id).download('in.jpg')
    pred, prob = predict(model, 'in.jpg')
    update.message.reply_text(f'{pred} ({prob:.4f})')

model = load_model('model.onnx')
opt = json.load(open('config.json','r'))
updater = Updater(opt['bot_token'])
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, handle_text))
dispatcher.add_handler(MessageHandler(Filters.photo, handle_photo))
updater.start_polling()
updater.idle()