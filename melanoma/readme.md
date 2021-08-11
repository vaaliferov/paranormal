
### simple

```bash
git clone git@github.com:vaaliferov/paranormal.git
git clone https://github.com/vaaliferov/paranormal.git

cd paranormal/melanoma/bot
cp simple.service melanoma_bot.service
vim melanoma_bot.service (<user>)
vim config.json (<token>)
apt install $(cat apt.txt)
pip3 install -r requirements.txt

mkdir /opt/melanoma
chown <user> /opt/melanoma
chmod 755 /opt/melanoma
cp bot.py config.json /opt/melanoma
cp melanoma_bot.service /etc/systemd/system
gdown --id 1t74E3bt8bzW3ZDHqL4cV2nmlTSXQhmF7 -O /opt/melanoma/model.pt
chmod +x /opt/melanoma/bot.py

systemctl daemon-reload
systemctl start melanoma_bot.service
systemctl status melanoma_bot.service
systemctl enable melanoma_bot.service
```

### virtualenv

```bash
git clone git@github.com:vaaliferov/paranormal.git
git clone https://github.com/vaaliferov/paranormal.git

cd paranormal/melanoma/bot
cp venv.service melanoma_bot.service
vim melanoma_bot.service (<user>)
vim config.json (<token>)
apt install $(cat apt.txt)

mkdir /opt/melanoma
chown <user> /opt/melanoma
chmod 755 /opt/melanoma
cp bot.py config.json /opt/melanoma
cp melanoma_bot.service /etc/systemd/system

pip3 install virtualenv
python3 -m venv /opt/melanoma/env
source /opt/melanoma/env/bin/activate
pip3 install -r requirements.txt
source deactivate

gdown --id 1t74E3bt8bzW3ZDHqL4cV2nmlTSXQhmF7 -O /opt/melanoma/model.pt
chmod +x /opt/melanoma/bot.py

systemctl daemon-reload
systemctl start melanoma_bot.service
systemctl status melanoma_bot.service
systemctl enable melanoma_bot.service
```

### docker

```bash
git clone git@github.com:vaaliferov/paranormal.git
git clone https://github.com/vaaliferov/paranormal.git
gdown --id 1t74E3bt8bzW3ZDHqL4cV2nmlTSXQhmF7 -O /opt/melanoma/model.pt

vim dockerfile (<user>)
vim config.json (<token>)

docker build -t <user>/melanoma_bot .
docker run --rm --user user --name melanoma_bot <user>/melanoma_bot
```

https://t.me/paranormal_melanoma_bot
![image](../pics/bot.png)