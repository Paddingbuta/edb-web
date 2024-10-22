<template>
  <nav class="title-bar">
    <img src="../assets/logo3.png" class="logo">
    <div class="option">
      安全数据
      <div class="dropdown">
        <a href="#">漏洞数据</a>
        <a href="/cybersploit">漏洞PoC</a>
      </div>
    </div>
    <div class="option">
      分析框架
      <div class="dropdown">
        <a href="http://119.29.73.177:5555/sctruster">鸿蒙应用分析</a>
        <a href="#">跨平台应用分析</a>
      </div>
    </div>
    <div class="option">
      漏洞检测
      <div class="dropdown">
        <a href="http://vulstotal.com">SAST漏洞检测</a>
        <a href="#">SCA漏洞检测</a>
        <a href="#">PoC漏洞验证</a>
      </div>
    </div>
    <div class="option">
      恶意软件
      <div class="dropdown">
        <a href="#">恶意代码检测</a>
        <a href="http://promal.top">恶意行为画像</a>
      </div>
    </div>


    <!--
    <div class="button-container">
      <div class="logsign">
        Log in
      </div>
      <div class="logsign">
        Sign up
      </div>
    </div> -->
    <!-- <div class="additional-text">(Related paper is under review, only a small part of data published)</div> -->
  </nav>
</template>

<script>
export default {
  name: "PageFooter",
};
</script>

<style scoped>
.title-bar {
  position: relative;
  background-color: #ffffff;
  color: white;
  /* height: 100px; */
  width: 100%;
  display: flex;
  justify-content: flex-start;
  /* 从左开始排列元素 */
  align-items: center;
}

.logo {
  width: 17vw;
  height: 6vw;
  margin-bottom: 1.1vw;
  /* margin-right: 50px; */
  /* 给图片添加右边距，让下拉框离图片有一定距离 */
}

.option {
  /* display: flex; */
  position: relative;
  font-size: 1vw;
  width: 9%;
  height: 4.8vw;
  color: rgb(0, 0, 0);
  /* border: 1px solid black; */
  /* border: 1px solid black; */
  /* background-color: #f0f0f0; Light grey background */
  font-weight: bold;
  cursor: pointer;
  margin-right: 3%;
  text-align: center;
  /* 文本居中 */
  line-height: 3.0vw;
  /* 使文本垂直居中 */
  /* padding-right: 1%; */
  /* 留出倒三角的空间 */
  margin-top: 1.5vw;
}

.option:hover {
  /* border-radius: 10px; */
  background-color: rgba(161, 195, 253, 0.1);
}


/* after伪元素，添加小三角形 */
.option::after {
  position: absolute;
  top: 1.2vw;
  right: 1vw;
  content: "";
  width: 0.3vw;
  height: 0.3vw;
  border-right: 0.2vw solid #4696ff;
  border-bottom: 0.2vw solid #4696ff;
  transform: rotate(45deg);
  transition: all 0.4s;
}

.option:hover::after {
  transform: rotate(225deg);
}

/* 隐藏的下拉菜单 */
.dropdown {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  /* border: 1px solid black; */
  background-color: rgb(244, 248, 255);
  z-index: 1;
  font-size: 0.9vw;
  /* border-radius: 10px; */
}

/* 下拉菜单的选项 */
.dropdown a {
  display: block;
  padding: 1px;
  text-decoration: none;
  color: black;
}

.dropdown a:hover {
  border-radius: 10px;
  background-color: rgba(131, 156, 213, 0.1);
}

/* 显示下拉菜单 */
.option:hover .dropdown {
  display: block;
}

img {
  width: 280px;
  height: 100px;
}

.button-container {
  display: flex;
  /* 使用 Flexbox 进行布局 */
  margin-left: 300px;
  /* 将整个容器往右移动 */
}

.logsign {
  width: 100px;
  /* 每个方框的宽度 */
  height: 50px;
  /* 每个方框的高度 */
  color: white;
  /* 字体颜色为白色 */
  background-color: #537aee;
  /* 背景颜色 */
  font-weight: bold;
  /* 字体加粗 */
  cursor: pointer;
  /* 鼠标悬停时显示手形光标 */
  margin-right: 20px;
  /* 右边框间距 */
  text-align: center;
  /* 文本水平居中 */
  line-height: 50px;
  /* 使文本垂直居中 */
  border-radius: 10px;
  /* 圆角 */
}

/* 最后一个方框不需要右侧间距 */
.logsign:last-child {
  margin-right: 0;
  /* 移除最后一个按钮的右边距 */
}

.additional-text {
  position: absolute;
  bottom: 0;
  right: 0;
  padding: 5px;
  background-color: #ffffff;
  color: rgb(50, 50, 50);
}
</style>
