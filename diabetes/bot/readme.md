#### systemd

```bash
git clone https://github.com/vaaliferov/paranormal.git

cd paranormal/diabetes/bot
sudo ./install.sh <name> <user> <token> <owner>

systemctl status diabetes_bot.service

cd /opt/diabetes_bot
sudo ./uninstall.sh
```

#### docker

```bash
git clone https://github.com/vaaliferov/paranormal.git

cd paranormal/diabetes/bot
docker build -t <user>/diabetes_bot .
docker run --rm --name diabetes_bot <user>/diabetes_bot
```