# ML dashboard

To run locally, clone the repo and then run [`deploy.sh`](./deploy.sh) 
and the app will be served at <http://localhost:8080>. The `admin` 
user is created if the app is executed for the first time (password is 
`admin`) or if the `app/app.db` gets deleted or moved.

To stop the app:

```bash
docker-compose -f docker/docker-compose.yml stop
```
