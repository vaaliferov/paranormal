
```bash
git clone git@github.com:vaaliferov/paranormal.git
git clone https://github.com/vaaliferov/paranormal.git
cd paranormal/diabetes/bot
vim config.json (<token>)
vim diabetes_bot.service (<user>)
pip install -r requirements.txt
mkdir /opt/diabetes
chown <user> /opt/diabetes
chmod 755 /opt/diabetes
cp random_forest.pkl /opt/diabetes
cp bot.py config.json /opt/diabetes
cp diabetes_bot.service /etc/systemd/system
chmod +x /opt/diabetes/bot.py
sudo systemctl daemon-reload
sudo systemctl start diabetes_bot.service
sudo systemctl enable diabetes_bot.service
sudo systemctl status diabetes_bot.service
```

https://t.me/paranormal_diabetes_bot
![image](../pics/tg.png)