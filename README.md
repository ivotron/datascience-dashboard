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

To stop the app just cancel with ```Ctrl+C```


### Integration

[Guia para integrar aplicaciones al dashboard (ES)](docs/guides/integration-es.md).

### Notes

Executing ```popper run``` regenerates all html applications and templates.
As this may take a while, after running it once (and once more after adding a new application)
its better to execute ```popper run start-dashboard```
instead, as it should take considerably less time to be ready.
