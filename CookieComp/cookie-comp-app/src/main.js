import Vue from 'vue'
import App from './App.vue'

import vuetify from './plugins/vuetify'

import store from './config/store'
import router from './config/router'

Vue.config.productionTip = false

window.app = new Vue({
  store,
  router,
  vuetify,
  render: h => h(App),
}).$mount('#app')
