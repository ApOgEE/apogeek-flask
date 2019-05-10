# APOGEEK Python Flask Project
My idea to create this project is to make it as a template for my future flask projects. I don't have any idea on how to grow this yet. But I'll keep on updating this project as my starter template for any python flask related project in the future.

Putting this code on github means that I'm willing to share this code. You may download and edit the code for your projects.

I'm using port 80. You may change the port on `docker-compose.yml` to `5000` for example like this:
```
   ports:
      - 5000:80
```

## Running the apps
I'm trying to make the simplest command to run this app. I finnaly found that `docker-compose` do helps alot to achieve that. Here is some commands that I'm using to run this python web app:

1. Starting the python app.

   `$ docker-compose up -d`

2. Stopping the app.

   `$ docker-compose down`

3. Delete all docker junks on my laptop to regain surface.

   `$ docker system prune -a` 
   
   But be extra careful with this command because you may remove all other docker files. I did this because I got limited SSD space and I don't mind to download everyting all over again.

