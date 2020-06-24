# ML dashboard

To run locally, clone the repo and then:

```bash
cd ml-dashboard/

docker-compose --file docker/docker-compose.yml up --build
```

The above re-builds the image if it's outdated, then starts the app. 
If the db hasn't been started, it creates it. The app is served at 
<http://localhost:8080>
