# Static web container

This container runs a default install nginx to serve static content. Start it with `docker run -v /full/path/to/web/pages/root/:/var/www/html:ro -d pocketinternet/http-static:0.1`

## Sample page

There's an included folder in the repo with an `index.html` and a picture that you can use (remember you need to put the full path in the docker run command).
