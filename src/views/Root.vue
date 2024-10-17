<template>
  <div class="contents">
    <div class="background">
      <div class="title">SCTruster</div>
      <div class="description">可信软件供应链治理平台提供了面向多种业务场景的软件供应链漏洞检测、验证、修复、攻防等全栈式安全防护示例。
      </div>
    </div>
    <div class="box">
      <div class="awards">
        <h2>软件供应链安全研究工作共计6次获得CCF-A类国际顶级会议的ACM SIGSOFT Distinguished Paper Awards荣誉</h2>
        <div class="sixaward">ICSE 2018, ICSE 2021, ASE 2022, ICSE 2023, ASE 2023, FSE 2024</div>
      </div>
      <div class="trophy"></div>
    </div>
    <div class="large-box">
      <p>研究成果在国家电网、中汽中心、华为等知名企业落地</p>
      <div class="company">
        <div class="company-pictures">
          <div class="picture3">
            <img src="../../src/assets/guojiadianwang.png" alt="Company 3 Logo">
          </div>
          <div class="picture2">
            <img src="../../src/assets/ZQZX.png" alt="Company 2 Logo" style="width: 50%; height: auto;">
          </div>
          <div class="picture1">
            <img src="../../src/assets/HUAWEI.png" alt="Company 1 Logo">
          </div>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="empty"></div>
      <div class="left-content">
        <h1>VulD2024</h1>
        <p>领域内大规模漏洞数据汇聚及增强平台，具备漏洞组件名称和漏洞影响版本范围归一化功能，并提供漏洞描述信息的融合与补全功能。</p>
        <a href="/" class="explore-link">EXPLORE ➤</a>
      </div>
      <div class="right-image">
        <img src="../../src/assets/CVEdata.png" alt="Description">
      </div>
      <div class="empty"></div>
    </div>

    <div class="container">
      <div class="empty"></div>
      <div class="left-image">
        <img src="../../src/assets/cybersploit.png" alt="Description">
      </div>
      <div class="right-content">
        <h1>CyberSploit</h1>
        <p>领域内最大规模的漏洞PoC数据汇聚及增强平台CyberSploit，具备漏洞PoC多源融合与补全功能，并提供Aspect-Level的细粒度漏洞PoC搜索功能。</p>
        <a href="/cybersploit" class="explore-link">EXPLORE ➤</a>
      </div>
      <div class="empty"></div>
    </div>

    <div class="container">
      <div class="empty"></div>
      <div class="left-content">
        <h1>HarmonyFlow</h1>
        <p>基于Panda IR的静态分析框架HarmonyFlow。该框架包括了指针分析和数据依赖分析两大核心模块，通过构建调用图和数据依赖图，帮助开发者更好地理解程序结构、优化性能以及识别安全漏洞，助力鸿蒙系统安全生态建设。
        </p>
        <a href="http://harmonyflow.sctruster.com:8080/" class="explore-link">EXPLORE ➤</a>
      </div>
      <div class="right-image">
        <img src="../../src/assets/HarmonyFlow.png" alt="Description">
      </div>
      <div class="empty"></div>
    </div>

    <div class="container">
      <div class="empty"></div>
      <div class="left-image">
        <img src="../../src/assets/CFLinker.png" alt="Description">
      </div>
      <div class="right-content">
        <h1>CFLinker</h1>
        <p>基于IR转化的跨平台移动应用分析框架CFLinker，提供了针对多种Host OS （Android，iOS，HarmonyOS）的多种跨平台开发框架（Flutter、React
          Native、Weex等）应用分析功能。</p>
        <a href="/" class="explore-link">EXPLORE ➤</a>
      </div>
      <div class="empty"></div>
    </div>

    <div class="container">
      <div class="empty"></div>
      <div class="left-content">
        <h1>VulsTotal</h1>
        <p>领域内面向安卓应用软件分析最全的开源SAST漏洞检测汇聚及增强平台，提供待分析APK文件的CSV格式的检测报告。</p>
        <a href="http://vulstotal.com" class="explore-link">EXPLORE ➤</a>
      </div>
      <div class="right-image">
        <img src="../../src/assets/VulsTotal.png" alt="Description">
      </div>
      <div class="empty"></div>
    </div>

    <div class="container">
      <div class="empty"></div>
      <div class="left-image">
        <img src="../../src/assets/SCA.png" alt="Description">
      </div>
      <div class="right-content">
        <h1>探巡SCA</h1>
        <p>赋能探巡面向二进制文件的软件成分分析（SCA）漏洞检测技术与功能。</p>
        <a href="/" class="explore-link">EXPLORE ➤</a>
      </div>
      <div class="empty"></div>
    </div>

    <div class="container">
      <div class="empty"></div>
      <div class="left-content">
        <h1>ProMal</h1>
        <p>领域内首个对Android恶意软件/开源恶意软件包进行恶意行为画像的平台，提供恶意攻击序列用于恶意行为的理解。</p>
        <a href="http://promal.top" class="explore-link">EXPLORE ➤</a>
      </div>
      <div class="right-image">
        <img src="../../src/assets/promal.png" alt="Description">
      </div>
      <div class="empty"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Root",
};
</script>

<style scoped>
@font-face {
  font-family: "Poppins";
  src: url("../assets/fonts/Poppins-Bold.ttf") format("ttf");
  font-weight: bold;
  font-style: normal;
}

.contents {
  width: 100%;
  display: flex;
  flex-direction: column;
  /* 使内容从上到下排列 */
  height: 400vh;
  /* 设置容器高度为视口高度 */
  justify-content: flex-start;
  /* 从顶部开始对齐内容 */
  align-items: center;
  /* 水平居中所有内容 */
}

.background {
  background-image: url("../../src/assets/bg.png");
  background-position: center;
  width: 100%;
  height: 60%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  /* 垂直居中内容 */
  align-items: center;
  /* 水平居中内容 */
  font-family: "Poppins", sans-serif;
}

.title {
  font-size: 8vw;
  font-weight: bold;
  margin-top: 4%;
  color: #014f98;
  /* background-image: linear-gradient(to right, rgb(132, 148, 90), rgb(60, 133, 92), rgb(18, 56, 95), rgb(60, 119, 133), rgb(132, 148, 90), rgb(60, 133, 92));
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent; */
}

.description {
  font-size: 1.5vw;
  width: 46%;
  /* font-weight: bold; */
  text-align: center;
  color: #252b3b;
}

.box {
  width: 60%;
  height: 15%;
  background-color: rgb(238, 251, 255);
  border-radius: 10px;
  margin-top: -1%;
  display: flex;
  justify-content: space-between;
  /* Space between awards and trophy */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.awards {
  font-size: 1vw;
  width: 100%;
  /* Wider to accommodate text */
  height: 90%;
  /* Keep this consistent to maintain visual alignment */
  display: flex;
  flex-direction: column;
  /* Stack text vertically */
  justify-content: center;
  /* Center text vertically */
  padding: 2%;
  margin-top: -1%;
}

.sixaward {
  font-size: 1vw;
  margin-top: 2%;
  color: #7b8ea1;
}

.trophy {
  background-image: url("../../src/assets/trophy.png");
  background-position: calc(50% - 10px) center;
  /* Center the image */
  background-repeat: no-repeat;
  background-size: 60%;
  /* Make the image scale appropriately */
  width: 40%;
  /* Adjust as necessary for visual balance */
  height: 100%;
  /* Fill the height of the box */
  /* background-color: rgb(0, 0, 0); */
}

.large-box {
  width: 50%;
  height: 10%;
  margin-top: 5%;
  margin-bottom: 5%;
  display: flex;
  justify-content: center;
  align-items: center;
  /* 垂直居中内容 */
  flex-direction: column;
  /* 使元素纵向排列 */
  align-items: center;
  /* 中心对齐 */
}

.large-box p {
  font-size: 1.8vw;
  font-weight: bold;
  color: #333;
  text-align: center;
}

.company {
  display: flex;
  /* 使公司 logos 在一行显示 */
  justify-content: center;
  /* 水平居中对齐 */
  margin-top: 2%;
  /* 如果需要，可以调整上下间距 */
}

.company-pictures {
  display: flex;
  /* 启用 flexbox 布局 */
  justify-content: space-between;
  /* 图片之间均匀分布 */
  align-items: center;
  /* 垂直居中对齐 */
}

.picture1 img,
/* .picture2 img, */
.picture3 img {
  max-width: 45%;
  /* 设置图片最大宽度 */
  height: auto;
  /* 保持宽高比 */
  margin: 0 70px;
  /* 图片间距 */
}

.picture2 img {
  max-width: 25%;
  /* 设置图片最大宽度 */
  height: auto;
  /* 保持宽高比 */
  display: block;
  /* 将图片设置为块级元素 */
  margin: 0 auto;
  /* 上下间距为0，左右自动居中 */
}

.container {
  display: flex;
  align-items: center;
  font-family: "Poppins", sans-serif;
  /* padding: 30%; */
  width: 80%;
  height: 30%;
  /* 根据需要调整 */
  box-sizing: border-box;
  flex-wrap: nowrap;
  /* 禁止换行 */
}

.empty {
  width: 10%;
}

.left-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 40%;
  /* 左半部分占 50% 宽度 */
  padding: 2%;
}

.left-content h1 {
  font-size: 2.8vw;
  /* 大字体 */
  margin-bottom: 5%;
}

.left-content p {
  font-size: 1.3vw;
  /* 小字体 */
  margin-bottom: 5%;
}

.explore-link {
  display: inline-block;
  color: #007bff;
  /* 设置字体为蓝色 */
  font-size: 1.2vw;
  width: 25%;
  text-decoration: none;
  padding: 2% 5%;
  position: relative;
  transition: all 0.3s ease;
  /* 过渡效果 */
}

.explore-link:hover {
  background-color: rgba(0, 123, 255, 0.1);
  /* 鼠标悬停时的淡蓝色背景 */
  color: #0056b3;
  /* 鼠标悬停时字体变成深蓝色 */
  transform: translateX(10%);
  /* 字体右移 */
}

/* .explore-link::after { */
/* content: ""; */
/* margin-left: 5%; */
/* } */

.left-content button:hover {
  background-color: #0056b3;
}

.right-image {
  width: 40%;
  height: auto;
  /* 右半部分占 50% 宽度 */
  display: flex;
  justify-content: center;
}

.right-image img {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover;
  /* 确保图片保持比例 */
}

/* 图片在左边 */
.left-image {
  width: 40%;
  height: auto;
  /* 左半部分占 50% 宽度 */
  display: flex;
  justify-content: center;
}

/* 确保图片大小适应容器 */
.left-image img {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover;
  /* 确保图片保持比例 */
}

/* 右边内容的样式 */
.right-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 40%;
  padding: 2%;
}

/* 标题的样式 */
.right-content h1 {
  font-size: 2.8vw;
  /* 大字体 */
  margin-bottom: 5%;
}

/* 描述文本的样式 */
.right-content p {
  font-size: 1.3vw;
  /* 小字体 */
  margin-bottom: 5%;
}

h1 {
  font-weight: bold;
}
</style>