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
      <div class="title">CodeSecLab</div>
      <div class="description">Located at Tianjin University, our research focuses on software supply chain security and vulnerability detection.</div>
    </div>
    <div class="box"></div> <!-- 添加的方框 -->
    <div class="large-box">
      <p>The companies and products we work with</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Root",
};
</script>

<style scoped>
.contents {
  width: 100%;
  display: flex;
  flex-direction: column; /* 使内容从上到下排列 */
  height: 100vh; /* 设置容器高度为视口高度 */
  justify-content: flex-start; /* 从顶部开始对齐内容 */
  align-items: center; /* 水平居中所有内容 */
}
.background {
  background-image: url("../../dist/static/img/bg1.png");
  background-position: center; /* 图片居中显示 */
  background-repeat: no-repeat; /* 不重复背景图片 */
  width: 100%; /* 容器宽度 */
  height: 60%; 
  display: flex;
  flex-direction: column;
  justify-content: center; /* 垂直居中内容 */
  align-items: center; /* 水平居中内容 */
  color: white; /* 字体颜色，可以根据需要调整 */
}

.title {
  font-size: 36px; /* 标题字体大小 */
  font-weight: bold; /* 加粗标题 */
  margin-bottom: 10px; /* 标题和描述之间的间距 */
}

.description {
  font-size: 18px; /* 描述字体大小 */
  text-align: center; /* 居中对齐描述文本 */
}

.box {
  width: 50%; /* 方框宽度 */
  height: 200px; /* 方框高度 */
  background-color: rgba(255, 255, 255, 0.8); /* 方框背景色，带透明度 */
  border-radius: 10px; /* 方框边角圆滑 */
  margin-top: -20px; /* 向上移动方框以使其中线穿过图片下端 */
  display: flex;
  justify-content: center; /* 水平居中内容 */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* 添加阴影效果 */
}

.large-box {
  width: 90%; /* 大框宽度 */
  height: 150px; /* 大框高度 */
  background-color: rgba(240, 240, 240, 0.9); /* 设置大框背景色 */
  border-radius: 15px; /* 边角圆滑 */
  margin-top: 30px; /* 与上方内容保持一定距离 */
  display: flex;
  justify-content: center; /* 水平居中内容 */
  align-items: center; /* 垂直居中内容 */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* 添加阴影 */
}

.large-box p {
  font-size: 24px; /* 文字大小 */
  font-weight: bold; /* 文字加粗 */
  color: #333; /* 文字颜色 */
  text-align: center; /* 文字居中对齐 */
}
/*
.card {
    position: relative;
    box-sizing: border-box;
    width: 300px;
    height: 400px;
    box-shadow: 12px 17px 51px rgba(3, 50, 219, 0.22);
    backdrop-filter: blur(6px);
    border-radius: 50px;
    text-align: center;
    cursor: pointer;
    transition: all 0.5s;
    display: flex;
    align-items: center;
    justify-content: center;
    user-select: none;
    font-weight: bolder;
    color: black;
}

.number {
    position: absolute;
    top: 50px;
    left: 130px;
    width: 30px;
    height: 30px;
    font-size: 40px;
    text-transform: uppercase;
    padding: 0px 5px 0px 8px;
    color: #9b9ced;
    background: rgba(228, 142, 99, 0.103);
}

.text {
    flex-grow: 1;
    padding: 15px;
    display: flex;
    flex-direction: column;
    color: rgb(117, 139, 237);
    font-weight: 900;
    font-size: 1.2em;
}

.contactButton {
    position: absolute;
    top: 330px;
    left: 100px;
    background: #adb1ef;
    color: white;
    font-family: inherit;
    padding: 0.45em;
    padding-left: 1em;
    font-size: 17px;
    font-weight: 500;
    border-radius: 0.9em;
    border: none;
    cursor: pointer;
    letter-spacing: 0.05em;
    display: flex;
    align-items: center;
    box-shadow: inset 0 0 1.6em -0.6em #714da6;
    overflow: hidden;
    height: 2.8em;
    padding-right: 3em;
}

.iconButton {
    margin-left: 1em;
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 2.2em;
    width: 2.2em;
    border-radius: 0.7em;
    box-shadow: 0.1em 0.1em 0.6em 0.2em #7a8cf3;
    right: 0.3em;
    transition: all 0.3s;
}

.contactButton:hover {
    transform: translate(-0.05em, -0.05em);
    box-shadow: 0.15em 0.15em #5566c2;
}

.contactButton:active {
    transform: translate(0.05em, 0.05em);
    box-shadow: 0.05em 0.05em #5566c2;
}
*/
</style>