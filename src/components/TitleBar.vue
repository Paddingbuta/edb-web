<!-- PageFooter.vue -->
<template>
  <nav class="title-bar">
    <router-link to="/">
      <img src="../assets/logo3.png">
    </router-link>
  </nav>
</template>
  
  <script>
  export default {
    name: 'PageFooter',
  };
  </script>
  
  <style scoped>
  
  .title-bar {
    background-color: #122d4f;
    color: white;
    height: 160px;
    width: 100%;
  }
  img{
    width: 420px;
    height: 150px;
  }
  </style>
  