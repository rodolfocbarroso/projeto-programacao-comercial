<template>
  <aside>
    <v-navigation-drawer v-model="isMenuVisible" app>
      <!--  -->
    </v-navigation-drawer>
  </aside>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: "Menu",
  computed: mapState(['isMenuVisible']),
}
</script>

<style>
</style>