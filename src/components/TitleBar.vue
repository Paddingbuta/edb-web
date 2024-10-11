<template>
  <nav class="title-bar">
    <!-- <router-link to="/"> -->
    <img src="../assets/logo.png" class="logo">
    <!-- </router-link> -->
    <div class="option">
      Data
      <div class="dropdown">
        <a href="#">Vul</a>
        <router-link to="/cybersploit"><a href="#">PoC</a></router-link>
      </div>
    </div>
    <div class="option">
      Tools
      <div class="dropdown">
        <a href="#">Attack</a>
        <a href="#">Defence</a>
      </div>
    </div>
    <div class="option">
      Architectures
      <div class="dropdown">
        <a href="#">HarmonyOS</a>
        <a href="#">Android/HOS</a>
      </div>
    </div>
    <div class="additional-text">(Related paper is under review, only a small part of data published)</div>
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
  background-color: #d6e6fe;
  color: white;
  height: 150px;
  width: 100%;
  display: flex;
  justify-content: flex-start; /* 从左开始排列元素 */
  align-items: center;
}

.logo {
  width: 280px;
  height: 100px;
  margin-right: 20px; /* 给图片添加右边距，让下拉框离图片有一定距离 */
}

.option {
  position: relative;
  width: 100px;
  height: 35px;
  color: black;
  border: 1px solid black;
  cursor: pointer;
  margin-right: 20px;
  text-align: center; /* 文本居中 */
  line-height: 35px;  /* 使文本垂直居中 */
  padding-right: 20px; /* 留出倒三角的空间 */
}


/* after伪元素，添加小三角形 */
.option::after {
  position: absolute;
  top: 12px;
  right: 12px;
  content: "";
  width: 8px;
  height: 8px;
  border-right: 2px solid #000;
  border-bottom: 2px solid #000;
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
  border: 1px solid black;
  background-color: white;
  z-index: 1;
}

/* 下拉菜单的选项 */
.dropdown a {
  display: block;
  padding: 10px;
  text-decoration: none;
  color: black;
}

.dropdown a:hover {
  background-color: #ddd;
}

/* 显示下拉菜单 */
.option:hover .dropdown {
  display: block;
}

img {
  width: 280px;
  height: 100px;
}

.additional-text {
  position: absolute;
  bottom: 0;
  right: 0;
  padding: 5px;
  background-color: #d6e6fe;
  color: rgb(50, 50, 50);
}
</style>
