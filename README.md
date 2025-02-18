sudo docker build -t django-prom .

docker compose up -d

sudo docker ps

nohup python3 restart_server.py &

--
curl -X POST http://localhost:5000 - to restart django-prom app
