<template>
  <div class="contents">
    <h1>{{ item.title }}</h1>
    

    <div class="container">
      <div class="box">
        <h2 class="top-text ownid">
          OWN-ID:
          <h3>{{item.own_ID}}</h3>
        </h2>
        <h2 class="top-text">
          CVE-ID:
          <h3>{{item.CVE_ID}}</h3>
        </h2>
        <h2 class="top-text">
          Test Platform:
          <h3>{{item.test_platform}}</h3>
        </h2>
        <h2 class="top-text">
          Software Version:
          <h3>{{item.software_version}}</h3>
        </h2>
        <h2 class="top-text">
          Author:
          <h3>{{item.author}}</h3>
        </h2>
        <h2 class="top-text">
          Source:
          <h3>{{item.source}}</h3>
        </h2>
        <h2 class="top-text">
          Publish Time:
          <h3>{{item.time}}</h3>
        </h2>
        <h2 class="top-text">
          Reference:
          <h3>{{item.reference}}</h3>
        </h2>
      </div>
      <!-- <div class="box">
        <h2 class="top-text">
          Test Platform:
          <h3>{{item.test_platform}}</h3>
        </h2>
        <h2 class="top-text">
          Software Version:
          <h3>{{item.software_version}}</h3>
        </h2> -->
        <!-- <h2 class="top-text">
          Tag: <h3>{{item.tag}}</h3>  Code Language:
          <h3>{{item.code_language}}</h3>
        </h2> -->
      <!-- </div> -->
      <!-- <div class="box">
        <h2 class="top-text">
          Author:
          <h3>{{item.author}}</h3>
        </h2>
        <h2 class="top-text">
          Source:
          <h3>{{item.source}}</h3>
        </h2>
        <h2 class="top-text">
          Publish Time:
          <h3>{{item.time}}</h3>
        </h2>
      </div> -->
    </div>
    <!-- <div class="bottom-blank"></div>
    <div class="bottom-blank"></div>

    <div class="container">
      <div class="box2">
        <h2 class="top-text">
          Reference:
          <h3>{{item.reference}}</h3>
        </h2>
      </div>
    </div> -->
    <!-- <div class="bottom-blank"></div> -->
    <!-- <div class="container">
      <div class="box2">
        <h2 class="top-text">
          Trigger Method:
          <h3>{{item.trigger_method}}</h3>
        </h2>
      </div>
    </div> -->
    <!-- <div class="bottom-blank"></div> -->
    <!-- <div class="container">
      <div class="box2">
        <h2 class="top-text">
          Record:
          <h3>{{item.record}}</h3>
        </h2>
      </div>
    </div> -->
    <!-- <div class="bottom-blank"></div> -->
    <div class="code">
      <!-- Python 代码 -->
      <pre>
      <code class="language-python">
        {{item.other_information}}
      </code>
    </pre>
    </div>

    <div class="bottom-blank"></div>
  </div>
</template>

<script>
import "prismjs/themes/prism.css";

export default {
  name: "Details",
  created() {
    this.item = this.$route.params.item;
  },
  data() {
    return {
      item: null,
    };
  },
};
</script>

<style>
h2 {
  display: inline-block !important;
  margin: 20px 10px;
  height: 15px;
  
}
h2.ownid{
  margin-top: 0px;
}
h3 {
  display: inline-block !important;
  font-size: 20px;
  color: #922d4f;
}
.language-python {
  width: 1000px;
  padding: 0px 20px;
}
.code {
  display: flex;
  align-items: center;
  justify-content: center;
}
pre {
  background-color: #f5f0ee;
}
pre code {
  display: block;
  padding: 1em;
  overflow-x: auto;
  background-color: #282c34;
  color: #abb2bf;
  border-radius: 4px;
}
.contents {
  margin-top: 0px;
  margin: 0;
  text-align: center;
}
h1 {
  font-size: 35px;
  margin: 40px 0px;
}
.bottom-blank {
  height: 30px;
}
.container {
  display: flex;
  justify-content: center;
}

.box {
  width: 950px;
  height: 380px;
  display: flex;
  flex-direction: column;
  align-items: center;
  /* background: radial-gradient(178.94% 106.41% at 26.42% 106.41%, #96b3b5 0%, rgba(255, 255, 255, 0) 71.88%); */
  
  margin-right: 40px;
  border-radius: 30px;
  /* box-shadow: 4px 4px 20px rgba(0, 0, 0, 0.3);
  
  background: #e0e0e0;
  box-shadow: 15px 15px 30px #bebebe,
             -15px -15px 30px #ffffff; */
             background: radial-gradient(ellipse farthest-side at 76% 77%, rgba(245, 228, 212, 0.25) 4%, rgba(255, 255, 255, 0) calc(4% + 1px)), radial-gradient(circle at 76% 40%, #fef6ec 4%, rgba(255, 255, 255, 0) 4.18%), linear-gradient(135deg, #eff0f2 0%, #000036 100%), radial-gradient(ellipse at 28% 0%, #ace3ff 0%, rgba(98, 149, 144, 0.5) 100%), linear-gradient(180deg, #bccace 0%, #f5eab0 69%, #d6c8a2 70%, #f3f5f4 100%);
  background-blend-mode: normal, normal, screen, overlay, normal;
  box-shadow: 0px 0px 10px 1px #000000;
}

.box2 {
  width: 1435px;
  height: 100px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f0f0f0;
  margin-right: 40px;
  border: 1px solid #ccc;
}

.box3 {
  width: 450px;
  height: 220px;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  background-color: #f0f0f0;
  
  margin-right: 40px;
  border: 1px solid #ccc;
}

.divider {
  width: 100%;
  height: 1px;
  background-color: #ccc;
  margin: 10px 0;
}

/* 上方文字样式 */
.top-text {
  margin-bottom: 10px;
}

</style>
