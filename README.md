# edb-web

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```
For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

## Docker

``` bash
docker pull paddingbuta/mysql:1.0.0
docker pull paddingbuta/dockervue:v1

docker network create --subnet=172.18.0.0/16 mynet

docker run -d -p 4306:3306 --net mynet --ip 172.18.0.3 -v /root/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 --name sqlserver paddingbuta/mysql:1.0.0
docker run -p 80:8086 -p 5000:5000 -d -v /root/project:/root/project --net mynet --ip 172.18.0.2 --name vueApp paddingbuta/dockervue:v1

# Create your database and table in sqlserver container.
# in vueApp container
python3 /usr/share/nginx/test/add_poc.py
python3 /usr/share/nginx/test/app.py
```
Then access http://172.18.0.2:80 in the host machine's browser.

