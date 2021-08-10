

#### connecting to our instance (ssh)
```bash
ssh vaaliferov@35.232.21.137
```

#### installing from github
```bash
git clone git@github.com:vaaliferov/paranormal.git
git clone https://github.com/vaaliferov/paranormal.git
cd paranormal/diabetes/bot
vim config.json (bot token)
vim diabetes_bot.service (user)
pip install -r requirements.txt
cp bot.py rf.pkl config.json /usr/local/diabetes
cp diabetes_bot.service /etc/systemd/system
chmod +x /usr/local/diabetes/bot.py
sudo systemctl daemon-reload
sudo systemctl start diabetes_bot.service
sudo systemctl enable diabetes_bot.service
sudo systemctl status diabetes_bot.service
```


#### registering a new telegram bot
```
https://t.me/BotFather -> /newbot -> token
```

#### figuring out the telegram bot owner id
```
https://t.me/userinfobot -> /start -> your id
```

#### creating and setting up our gcloud instance
```
https://console.cloud.google.com

navigation menu -> compute -> compute engine -> vm instances -> create instance
name: instance-2, machine family: general-purpose, series: e2, machine type: e2-small
boot disk: ubuntu 21.04-minimal, firewall: allow http(s) traffic
security -> ssh keys -> add item (ssh-keygen -t rsa; cat ~/.ssh/id_rsa.pub)
networking -> network interfaces -> external ip -> create ip address -> premium

navigation menu -> networking -> vpc network -> firewall -> default allow http -> edit (tcp: 8080,8765)
```

#### installing client tools (gcloud)
```bash
wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-342.0.0-linux-x86_64.tar.gz
tar -zxvf google-cloud-sdk-342.0.0-linux-x86_64.tar.gz
rm -f google-cloud-sdk-342.0.0-linux-x86_64.tar.gz
./google-cloud-sdk/install.sh
gcloud init (new bash session)
```

#### listing our instances (gcloud)
```bash
gcloud compute instances list
```

#### uploading files on our instance (gcloud)

```bash
gcloud compute scp -r detection vaaliferov@instance:~/
```

#### connecting to our instance (gcloud)

```bash
gcloud compute ssh vaaliferov@instance
```

#### uploading files on our instance (scp)
```bash
scp -r ~/github/paranormal/diabetes/* vaaliferov@35.232.21.137:~/diabetes
```

#### uploading files on our instance (rsync)
```bash
sudo apt install rsync  # local & remote
rsync -av -e ssh --exclude='.git' ~/github/paranormal/diabetes/* vaaliferov@35.232.21.137:~/diabetes
```

#### connecting to our instance (ssh)
```bash
ssh vaaliferov@35.232.21.137
```

#### installing dependencies and making scripts executable
```bash
sudo apt install libopencv-dev python3-opencv python3-pip
pip install -r ~/detection/requirements.txt
chmod +x ~/detection/*.py
```

#### /etc/systemd/system/detector_static.service
```
[Unit]
Description=detector_static

[Service]
Type=simple
User=vaaliferov
WorkingDirectory=/home/vaaliferov/detection
ExecStart=/home/vaaliferov/detection/static.py

[Install]
WantedBy=multi-user.target
```

#### activating our service
```bash
sudo systemctl daemon-reload

sudo systemctl start detector_static.service
sudo systemctl enable detector_static.service
sudo systemctl status detector_static.service
```

#### https://t.me/paranormal_diabetes_bot
![image](pics/tg.png)