<!-- PageFooter.vue -->
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
    background-color: #122d4f;
    color: white;
    padding: 10px;
  }
  </style>
  