<template>
  <div class="contents">
    <!-- <router-link to="/cybersploit">CyberSploit: Large Scale Proof-of-Concept Databse</router-link>
        <br>
        <a href="http://harmonyflow.sctruster.com:8080/">harmonyflow</a>
        <br>
        <a href="http://159.75.80.253:8888/mutisource">mutisource</a> -->
    <!--
        <div class="card">
            <div>
                <div class="number">01</div>
                <div class="text">
                    <span>CyberSploit</span>
                </div>
                <router-link to="/cybersploit">
                    <button class="contactButton">
                        Entry
                        <div class="iconButton">
                            <svg height="24" width="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 0h24v24H0z" fill="none"></path>
                                <path
                                    d="M16.172 11l-5.364-5.364 1.414-1.414L20 12l-7.778 7.778-1.414-1.414L16.172 13H4v-2z"
                                    fill="currentColor"></path>
                            </svg>
                        </div>
                    </button>
                </router-link>
            </div>
        </div>
        <div class="card">
            <div>
                <div class="number">02</div>
                <div class="text">
                    <span>Harmonyflow</span>
                </div>
                <a href="http://harmonyflow.sctruster.com:8080/">
                    <button class="contactButton">
                        Entry
                        <div class="iconButton">
                            <svg height="24" width="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 0h24v24H0z" fill="none"></path>
                                <path
                                    d="M16.172 11l-5.364-5.364 1.414-1.414L20 12l-7.778 7.778-1.414-1.414L16.172 13H4v-2z"
                                    fill="currentColor"></path>
                            </svg>
                        </div>
                    </button>
                </a>
            </div>
        </div>
        <div class="card">
            <div>
                <div class="number">03</div>
                <div class="text">
                    <span>Mutisource</span>
                </div>
                <a href="http://159.75.80.253:8888/mutisource">
                    <button class="contactButton">
                        Entry
                        <div class="iconButton">
                            <svg height="24" width="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 0h24v24H0z" fill="none"></path>
                                <path
                                    d="M16.172 11l-5.364-5.364 1.414-1.414L20 12l-7.778 7.778-1.414-1.414L16.172 13H4v-2z"
                                    fill="currentColor"></path>
                            </svg>
                        </div>
                    </button>
                </a>
            </div>
        </div> -->
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
      <!-- <div class="awards">ACM SIGSOFT Distinguished Paper Awards</div> -->
      <div class="trophy"></div>
    </div> <!-- 添加的方框 -->
    <div class="large-box">
      <p>研究成果在国家电网、中汽中心、华为等知名企业落地</p>
      <div class="company">
        <div class="picture3">
          <img
            src="../../src/assets/guojiadianwang.png"
            alt="Company 3 Logo"
          >
        </div>
        <div class="picture2">
          <img
            src="../../src/assets/ZQZX.png"
            alt="Company 2 Logo"
            style="width: 50%; height: auto;"
          >
        </div>
        <div class="picture1">
          <img
            src="../../src/assets/HUAWEI.png"
            alt="Company 1 Logo"
          >
        </div>
      </div>
    </div>

     <div class="container">
      <div class="empty"></div>
      <div class="left-content">
        <h1>VulD2024</h1>
        <p>领域内大规模漏洞数据汇聚及增强平台，具备漏洞组件名称和漏洞影响版本范围归一化功能，并提供漏洞描述信息的融合与补全功能。</p>
        <a
          href="/"
          class="explore-link"
        >EXPLORE ➤</a>
      </div>
      <div class="right-image">
        <img
          src="../../src/assets/CVEdata.png"
          alt="Description"
        >
      </div>
      <div class="empty"></div>
    </div>

    <div class="container">
      <div class="empty"></div>
      <div class="left-content">
        <h1>CyberSploit</h1>
        <p>领域内最大规模的漏洞PoC数据汇聚及增强平台CyberSploit，具备漏洞PoC多源融合与补全功能，并提供Aspect-Level的细粒度漏洞PoC搜索功能。</p>
        <a
          href="/cybersploit"
          class="explore-link"
        >EXPLORE ➤</a>
      </div>
      <div class="right-image">
        <img
          src="../../src/assets/cybersploit.png"
          alt="Description"
        >
      </div>
      <div class="empty"></div>
    </div>

    <div class="container">
      <div class="empty"></div>
      <div class="left-content">
        <h1>HarmonyFlow</h1>
        <p>基于Panda IR的静态分析框架HarmonyFlow。该框架包括了指针分析和数据依赖分析两大核心模块，通过构建调用图和数据依赖图，帮助开发者更好地理解程序结构、优化性能以及识别安全漏洞，助力鸿蒙系统安全生态建设。</p>
        <a
          href="http://harmonyflow.sctruster.com:8080/"
          class="explore-link"
        >EXPLORE ➤</a>
      </div>
      <div class="right-image">
        <img
          src="../../src/assets/HarmonyFlow.png"
          alt="Description"
        >
      </div>
      <div class="empty"></div>
    </div>

    <div class="container">
      <div class="empty"></div>
      <div class="left-content">
        <h1>CFLinker</h1>
        <p>基于IR转化的跨平台移动应用分析框架CFLinker，提供了针对多种Host OS （Android，iOS，HarmonyOS）的多种跨平台开发框架（Flutter、React Native、Weex等）应用分析功能。</p>
        <a
          href="/"
          class="explore-link"
        >EXPLORE ➤</a>
      </div>
      <div class="right-image">
        <img
          src="../../src/assets/CFLinker.png"
          alt="Description"
        >
      </div>
      <div class="empty"></div>
    </div>

    <div class="container">
      <div class="empty"></div>
      <div class="left-image">
        <img
          src="../../src/assets/VulsTotal.png"
          alt="Description"
        >
      </div>
      <div class="right-content">
        <h1>VulsTotal</h1>
        <p>领域内面向安卓应用软件分析最全的开源SAST漏洞检测汇聚及增强平台，提供待分析APK文件的CSV格式的检测报告。</p>
        <a
          href="http://vulstotal.com"
          class="explore-link"
        >EXPLORE ➤</a>
      </div>
      <div class="empty"></div>
    </div>

    <div class="container">
      <div class="empty"></div>
      <div class="left-image">
        <img
          src="../../src/assets/SCA.png"
          alt="Description"
        >
      </div>
      <div class="right-content">
        <h1>探巡SCA</h1>
        <p>赋能探巡面向二进制文件的软件成分分析（SCA）漏洞检测技术与功能。</p>
        <a
          href="/"
          class="explore-link"
        >EXPLORE ➤</a>
      </div>
      <div class="empty"></div>
    </div>

    <div class="container">
      <div class="empty"></div>
      <div class="left-content">
        <h1>ProMal</h1>
        <p>领域内首个对Android恶意软件/开源恶意软件包进行恶意行为画像的平台，提供恶意攻击序列用于恶意行为的理解。</p>
        <a
          href="http://promal.top"
          class="explore-link"
        >EXPLORE ➤</a>
      </div>
      <div class="right-image">
        <img
          src="../../src/assets/promal.png"
          alt="Description"
        >
      </div>
      <div class="empty"></div>
    </div>

    

    
    <!-- <div class="container">
      <div class="empty"></div>
      <div class="left-image">
        <img
          src="../../src/assets/PoCCompletion.png"
          alt="Description"
        >
      </div>
      <div class="right-content">
        <h1>PoC-info Completion</h1>
        <p>This tool integrates and fuses multi-source PoC information and vulnerability details to enhance PoC completeness. By consolidating diverse data sources, it enriches PoCs with more detailed context, making them more comprehensive and informative.</p>
        <a
          href="promal.top"
          class="explore-link"
        >EXPLORE ➤</a>
      </div>
      <div class="empty"></div>
    </div> -->

    

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
  /* 图片居中显示 */
  background-repeat: no-repeat;
  /* 不重复背景图片 */
  width: 100%;
  /* 容器宽度 */
  height: 40%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  /* 垂直居中内容 */
  align-items: center;
  /* 水平居中内容 */
  color: white;
  /* 字体颜色，可以根据需要调整 */
  font-family: "Poppins", sans-serif;
}

.title {
  font-size: 120px;
  /* 标题字体大小 */
  font-weight: bold;
  /* 加粗标题 */
  margin-top: 1px;
  
  /* 标题和描述之间的间距 */
  color: #2c3e50;
  /* 或者可以使用其他颜色，比如 */
  /* color: #e74c3c; */
}

.description {
  font-size: 23px;
  width: 50%;
  font-weight: bold;
  /* 描述字体大小 */
  text-align: center;
  /* 居中对齐描述文本 */
  color: #252b3b;
}

.box {
  width: 60%;
  height: 500px;
  background-color: rgba(255, 255, 255);
  border-radius: 10px;
  margin-top: -50px;
  display: flex;
  /* Using flexbox for arranging children */
  justify-content: space-between;
  /* Space between awards and trophy */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.awards {
  width: 90%;
  /* Wider to accommodate text */
  height: 90%;
  /* Keep this consistent to maintain visual alignment */
  display: flex;
  flex-direction: column;
  /* Stack text vertically */
  justify-content: center;
  /* Center text vertically */
  padding: 20px;
  margin-top: -20px;
}

.sixaward {
  font-size: 16px;
  /* 标题字体大小 */
  /* font-weight: bold; */
  /* 加粗标题 */
  margin-top: 4px;
  /* margin-bottom: 50px; */
  /* 标题和描述之间的间距 */
  color: #7b8ea1;
  /* 或者可以使用其他颜色，比如 */
  /* color: #e74c3c; */
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
  /* 大框宽度 */
  height: 190px;
  /* 大框高度 */
  border-radius: 15px;
  /* 边角圆滑 */
  margin-top: 30px;
  /* 与上方内容保持一定距离 */
  display: flex;
  justify-content: center;
  /* 水平居中内容 */
  align-items: center;
  /* 垂直居中内容 */
  flex-direction: column;
  /* 使元素纵向排列 */
  align-items: center;
  /* 中心对齐 */
}

.large-box p {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  text-align: center;
}

.company {
  display: flex; /* 使公司 logos 在一行显示 */
  justify-content: center; /* 水平居中对齐 */
  margin-top: 10px; /* 如果需要，可以调整上下间距 */
}

.picture1 img,
.picture3 img {
  max-width: 70px; /* 设置图片最大宽度 */
  height: auto; /* 保持宽高比 */
  margin: 0 70px; /* 图片间距 */
}

.picture2 img {
  max-width: 300px; /* 设置图片最大宽度 */
  height: auto; /* 保持宽高比 */
  display: block; /* 将图片设置为块级元素 */
  margin: 0 auto; /* 上下间距为0，左右自动居中 */
}

.container {
  display: flex;
  align-items: center;
  font-family: "Poppins", sans-serif;
  padding: 20px;
  width: 80%;
  height: 600px; /* 根据需要调整 */
  box-sizing: border-box;
  flex-wrap: nowrap; /* 禁止换行 */
}

.empty {
  width: 10%;
}

.left-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 40%; /* 左半部分占 50% 宽度 */
  padding: 20px;
}

.left-content h1 {
  font-size: 36px; /* 大字体 */
  margin-bottom: 10px;
}

.left-content p {
  font-size: 18px; /* 小字体 */
  margin-bottom: 20px;
}

.explore-link {
  display: inline-block;
  color: #007bff; /* 设置字体为蓝色 */
  font-size: 16px;
  width: 100px;
  text-decoration: none;
  padding: 10px 20px;
  position: relative;
  transition: all 0.3s ease; /* 过渡效果 */
}

.explore-link:hover {
  background-color: rgba(0, 123, 255, 0.1); /* 鼠标悬停时的淡蓝色背景 */
  color: #0056b3; /* 鼠标悬停时字体变成深蓝色 */
  transform: translateX(10px); /* 字体右移 */
}

.explore-link::after {
  content: "";
  margin-left: 5px;
}

.left-content button:hover {
  background-color: #0056b3;
}

.right-image {
  width: 40%; /* 右半部分占 50% 宽度 */
  display: flex;
  justify-content: center;
}

.right-image img {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover; /* 确保图片保持比例 */
}

/* 图片在左边 */
.left-image {
  width: 40%; /* 左半部分占 50% 宽度 */
  display: flex;
  justify-content: center;
}

/* 确保图片大小适应容器 */
.left-image img {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover; /* 确保图片保持比例 */
}

/* 右边内容的样式 */
.right-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 40%; 
  padding: 20px;
}

/* 标题的样式 */
.right-content h1 {
  font-size: 36px; /* 大字体 */
  margin-bottom: 10px;
}

/* 描述文本的样式 */
.right-content p {
  font-size: 18px; /* 小字体 */
  margin-bottom: 20px;
}

h1 {
  font-weight: bold;
}
</style>