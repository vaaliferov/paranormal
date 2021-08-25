#### systemd

```bash
git clone https://github.com/vaaliferov/paranormal.git

cd paranormal/diabetes/bot
vim config.json (<token>)
sudo ./install.sh <user>

systemctl status diabetes_bot.service

cd /opt/diabetes_bot
sudo ./uninstall.sh
```

#### docker

```bash
git clone https://github.com/vaaliferov/paranormal.git

cd paranormal/diabetes/bot
vim config.json (<token>)

docker build -t <user>/diabetes_bot .
docker run --rm --name diabetes_bot <user>/diabetes_bot
```