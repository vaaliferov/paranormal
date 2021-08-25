#### systemd

```bash
git clone https://github.com/vaaliferov/paranormal.git

cd paranormal/melanoma/bot
vim config.json (<token>)
sudo ./install.sh <user>

systemctl status melanoma_bot.service

cd /opt/melanoma_bot
sudo ./uninstall.sh
```

#### docker

```bash
git clone https://github.com/vaaliferov/paranormal.git

cd paranormal/melanoma/bot
vim config.json (<token>)
gdown --id 1KNeRnzxYF4X-DhvFfL_mrMDabWnTrPmg -O model.onnx

docker build -t <user>/melanoma_bot .
docker run --rm --name melanoma_bot <user>/melanoma_bot
```