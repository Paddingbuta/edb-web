import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/views/Main'
import Details from '@/views/Details'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/cybersploit',
    },
    {
      path: '/cybersploit',
      name: 'Main',
      component: Main,
    },
    {
      path: '/cybersploit/details',
      name: 'Details',
      component: Details,
      props: (route) => ({ item: route.params.item }),
    },
  ]
})
