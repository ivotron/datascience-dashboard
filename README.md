# ML dashboard

To run locally, clone the repo and then:

```bash
cd ml-dashboard/

docker-compose --file docker/docker-compose.yml up --build -d
```

The above re-builds the image if it's outdated, then starts the app. 
If the db hasn't been started, it creates it. The app is served at 
<http://localhost:8080>


To create an admin you can execute:

```bash
docker exec mldashes bash -c \
    "flask fab create-admin \
      --username admin \
      --firstname admin \
      --lastname admin \
      --email admin@admin.com \
      --password admin"
```

And then you can login with the provided credentials as an administrator.
