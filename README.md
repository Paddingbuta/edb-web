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

## Docker

``` bash
docker pull paddingbuta/mysql:latest
docker pull paddingbuta/test-docker:1.0.0

docker network create --subnet=172.18.0.0/16 mynet

docker run -d -p 4306:3306 --net mynet --ip 172.18.0.3 -v /root/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 mysql:latest
docker run -p 3060:8086 -p 5000:5000 -d -v /root/project:/root/project --net mynet --ip 172.18.0.2 --name vueApp test-docker:1.0.0

# in vueApp container
python3 /usr/share/nginx/test/app.py

```
Then access http://localhost:3060 in the host machine's browser.

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
