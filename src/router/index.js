import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/views/Main'
import Details from '@/views/Details'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main,
    },
    {
      path: '/details',
      name: 'Details',
      component: Details,
    },
  ]
})
