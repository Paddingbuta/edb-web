// vue.config.js
module.exports = {
  devServer: {
    host: '0.0.0.0', // 使得服务器可在局域网访问
    port: 8080, // 可以根据需要修改端口
    disableHostCheck: true, // 关闭主机检查，允许访问
  },
};
