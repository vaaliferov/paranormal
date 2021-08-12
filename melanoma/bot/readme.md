
### virtualenv

```bash
git clone git@github.com:vaaliferov/paranormal.git
git clone https://github.com/vaaliferov/paranormal.git

cd paranormal/melanoma/bot
vim melanoma_bot.service (<user>)
vim config.json (<token>)
apt install $(cat apt.txt)

mkdir /opt/melanoma
chown <user> /opt/melanoma
chmod 755 /opt/melanoma
cp bot.py config.json /opt/melanoma
cp melanoma_bot.service /etc/systemd/system
gdown --id 1KNeRnzxYF4X-DhvFfL_mrMDabWnTrPmg -O /opt/melanoma/model.onnx

pip3 install virtualenv
python3 -m venv /opt/melanoma/env
source /opt/melanoma/env/bin/activate
pip3 install -r requirements.txt
deactivate

systemctl daemon-reload
systemctl start melanoma_bot.service
systemctl status melanoma_bot.service
systemctl enable melanoma_bot.service
```

### docker

```bash
git clone git@github.com:vaaliferov/paranormal.git
git clone https://github.com/vaaliferov/paranormal.git

cd paranormal/melanoma/bot
vim config.json (<token>)
gdown --id 1KNeRnzxYF4X-DhvFfL_mrMDabWnTrPmg -O model.onnx

docker build -t <user>/melanoma_bot .
docker run --rm --name melanoma_bot <user>/melanoma_bot
```

https://t.me/paranormal_melanoma_bot
![image](../pics/bot.png)