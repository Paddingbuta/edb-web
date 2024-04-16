<template>
  <div id="app">
    <titlebar/>
    <router-view/>
    <pagefooter/>
  </div>
</template>

<script>
import titlebar from "./components/TitleBar.vue"
import pagefooter from "./components/PageFooter.vue"
export default {
  name: 'App',
  components: {
    titlebar,
    pagefooter,
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #ebecf1;
  margin: 0px;
  min-height: 100vh;
  width: 100%;
}
</style>
