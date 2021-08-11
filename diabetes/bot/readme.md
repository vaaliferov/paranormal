
#### simple

```bash
git clone git@github.com:vaaliferov/paranormal.git
git clone https://github.com/vaaliferov/paranormal.git

cd paranormal/diabetes/bot
cp simple.service diabetes_bot.service
vim diabetes_bot.service (<user>)
vim config.json (<token>)
apt install $(cat apt.txt)
pip3 install -r requirements.txt

mkdir /opt/diabetes
chown <user> /opt/diabetes
chmod 755 /opt/diabetes
cp random_forest.pkl /opt/diabetes
cp bot.py config.json /opt/diabetes
cp diabetes_bot.service /etc/systemd/system
chmod +x /opt/diabetes/bot.py

systemctl daemon-reload
systemctl start diabetes_bot.service
systemctl enable diabetes_bot.service
systemctl status diabetes_bot.service
```

#### virtualenv

```bash
git clone git@github.com:vaaliferov/paranormal.git
git clone https://github.com/vaaliferov/paranormal.git

cd paranormal/diabetes/bot
cp venv.service diabetes_bot.service
vim diabetes_bot.service (<user>)
vim config.json (<token>)
apt install $(cat apt.txt)

mkdir /opt/diabetes
chown <user> /opt/diabetes
chmod 755 /opt/diabetes
cp random_forest.pkl /opt/diabetes
cp bot.py config.json /opt/diabetes
cp diabetes_bot.service /etc/systemd/system

pip3 install virtualenv
python3 -m venv /opt/diabetes/env
source /opt/diabetes/env/bin/activate
pip3 install -r requirements.txt
deactivate

chmod +x /opt/diabetes/bot.py

systemctl daemon-reload
systemctl start diabetes_bot.service
systemctl status diabetes_bot.service
systemctl enable diabetes_bot.service
```

#### docker

```bash
git clone git@github.com:vaaliferov/paranormal.git
git clone https://github.com/vaaliferov/paranormal.git

cd paranormal/diabetes/bot
vim config.json (<token>)

docker build -t <user>/diabetes_bot .
docker run --rm --user user --name diabetes_bot <user>/diabetes_bot
```

https://t.me/paranormal_diabetes_bot
![image](../pics/tg.png)