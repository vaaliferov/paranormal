#!/usr/bin/env python3

import json
import numpy as np
from PIL import Image

from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler

import torch
import torchvision
import torch.nn as nn
import torchvision.transforms.functional as F
from torchvision.transforms import Compose, Resize
from torchvision.transforms import ToTensor, Normalize

from efficientnet_pytorch import EfficientNet

def load_model(path):
    model = EfficientNet.from_name('efficientnet-b6', num_classes=1)
    model.load_state_dict(torch.load(path, map_location=torch.device('cpu')))
    return model.eval()

def pad(x):
    w, h = x.size; m = np.max([w, h])
    hp, hpr = (m - w) // 2, (m - w) % 2
    vp, vpr = (m - h) // 2, (m - h) % 2
    p = (hp + hpr, vp + vpr, hp, vp)
    return F.pad(x, p, 0, 'constant')

def to_tensor(x):
    x = ToTensor()(pad(x))
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    return Normalize(mean, std)(x)

def predict(model, path):
    x = Image.open(path)
    x.thumbnail((224,224), Image.ANTIALIAS)
    x = to_tensor(x).unsqueeze(0)
    y = model(x).detach()[0]
    y = nn.Sigmoid()(y).item()
    return int(y > 0.5), y

def handle_text(update, context):
    update.message.reply_text('waiting for photos...')

def handle_photo(update, context):
    file_id = update.message.photo[-1]['file_id']
    context.bot.getFile(file_id).download('in.jpg')
    pred, prob = predict(model, 'in.jpg')
    update.message.reply_text(f'{pred} ({prob:.4f})')

model = load_model('model.pt')
opt = json.load(open('config.json','r'))
updater = Updater(opt['bot_token'])
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, handle_text))
dispatcher.add_handler(MessageHandler(Filters.photo, handle_photo))
updater.start_polling()
updater.idle()