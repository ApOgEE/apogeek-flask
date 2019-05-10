# APOGEEK Python Flask Project

I created this project as a template for my flask project. I don't have any idea on how to grow this yet. But I'll keep on updating this project as my starter template for any python flask related project in the future.

Putting this code on github means that I'm willing to share this code. You may download and edit the code for your project too.

I'm using port 80. You may change the port on `docker-compose.yml` to `5000` for example like this:
```
    ports:
      - 5000:80
```

Here is some commands that I'm using to run this python web app:

1. Starting the python app.
   `$ docker-compose up -d`

2. Stopping the app.
   `$ docker-compose down`

3. Delete all docker junks on my laptop to regain surface.
   `$ docker system prune -a` 
