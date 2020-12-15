import Vue from 'vue'
import App from './App.vue'

import vuetify from './plugins/vuetify'
import './config/msgs'
import store from './config/store'
import router from './config/router'

Vue.config.productionTip = false

//TEMPORARIO!
require('axios').defaults.headers.common['Authorization'] = 'Token f25070b0926a7eca8bc3963deed9c984a4b51269'

window.app = new Vue({
  store,
  router,
  vuetify,
  render: h => h(App),
}).$mount('#app')
