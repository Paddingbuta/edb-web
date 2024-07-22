<!-- PageFooter.vue -->
<template>
  <div class="page-footer">
    <div class="br"></div>
    <h4>CyberSploit</h4>
    <h4>Large-Scale Proof-of-Concept Data Storage and Submission Sites</h4>
    <a href="https://beian.miit.gov.cn">备案号：津ICP备2024017050号-1</a>
  </div>
</template>

<script>
export default {
  name: 'PageFooter',
};
</script>

<style scoped>
h4 {
  font-size: 15px;
  color: #000000;
}
.page-footer {
  font-size: 13px;
  position: relative;
  bottom: 0;
  width: 100%;
  height: 125px;
  background-image: linear-gradient(to bottom,#f1f1f1,#d5dbe8, #c1cee1,#b2cbe9);  
  font-size: 13px;
  color: white;
  text-align: center;
}
.br{
  height: 5px;
}
</style>
