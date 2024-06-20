<template>
  <nav class="title-bar">
    <router-link to="/">
      <img src="../assets/logo.png">
    </router-link>
    <div class="additional-text">(Related paper is under review, only a small part of data published)</div>
  </nav>
</template>
  
  <script>
  export default {
    name: 'PageFooter',
  };
  </script>
  
  <style scoped>
/*   
  .title-bar {
    background-color: #d6e6fe;
    color: white;
    height: 100px;
    width:100%;
  } */
  .title-bar {
  position: relative;
  background-color: #d6e6fe;
  color: white;
  height: 100px;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
  img{
    width: 600px;
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
  