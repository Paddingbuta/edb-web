<template>
  <nav class="title-bar">
    <router-link to="/">
      <img src="../assets/logo.png">
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
    background-color: #d6e6fe;
    color: white;
    height: 100px;
    width:100%;
  }
  img{
    width: 600px;
    height: 100px;
  }
  </style>
  