<!-- PageFooter.vue -->
<template>
  <div class="page-footer">
    <!-- <h4>CyberSploit</h4>
    <h4>Large-Scale Proof-of-Concept Data Storage and Submission Sites</h4> -->
    <div
      v-if="isHomePage"
      class="icp">
    <strong>Copyright©CodeSecLab</strong>
    All Rights Reserved
      <a
        href="https://beian.miit.gov.cn"
        target="_blank"
      >{{ record }}</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "PageFooter",
  data() {
    return {
      year: 2024,
      author: "CodeSecLab",
      record: "津ICP备2024017050号-1",
    };
  },
  computed: {
    isHomePage() {
      return this.$route.path === "/"; // 主页的路径是 '/'
    },
  },
};
</script>

<style scoped>
/* h4 {
  font-size: 15px;
  color: #000000;
} */
.icp {
  position: absolute;
  bottom: 0;
  right: 0;
  margin: 10px 0;
  width: 100%;
  
  white-space: pre;
  text-align: center;
  color: gray;
  z-index: 1000;
}
.icp > a {
  color: gray;
  text-decoration: none;
}
.icp > a:hover {
  color: rgb(242, 15, 15);
  text-decoration: none;
}

.page-footer {
  font-size: 1vw;
  position: relative;
  bottom: 0;
  width: 100%;
  height: 90px;
  background-image: linear-gradient(
    to bottom,
    #f1f1f1,
    #d5dbe8,
    #c1cee1,
    #b2cbe9
  );
  font-size: 1vw;
  color: white;
  text-align: center;
}

</style>
