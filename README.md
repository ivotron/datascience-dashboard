# ML dashboard

To run locally, install Popper, then:

```bash
git clone https://github.com/ivotron/ml-dashboard

cd ml-dashboard/

popper run
```

the app will be served at <http://localhost:8080>. The `admin` user is 
created if the app is executed for the first time (password is 
`admin`) or if the `app/app.db` file gets deleted or moved.

To stop the app:

```bash
docker-compose -f docker/docker-compose.yml stop
```
