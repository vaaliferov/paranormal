#### systemd

```bash
git clone https://github.com/vaaliferov/paranormal.git

cd paranormal/app
sudo ./install.sh <user> <port>

systemctl status paranormal_app.service

cd /opt/paranormal_app
sudo ./uninstall.sh
```

#### docker

```bash
git clone https://github.com/vaaliferov/paranormal.git

cd paranormal/app
docker build -t <user>/paranormal_app .
docker run -p 127.0.0.1:8501:8501/tcp --rm --name paranormal_app <user>/paranormal_app

google-chrome http://127.0.0.1:8501
```