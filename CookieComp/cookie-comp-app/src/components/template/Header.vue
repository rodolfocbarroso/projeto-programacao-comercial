<template>
  <header>
    <v-app-bar app data-app>
      <v-app-bar-nav-icon v-if="!hideToggle" @click="toggleMenu"></v-app-bar-nav-icon>

      <v-spacer>
        <v-toolbar-title>
          {{ title }}
        </v-toolbar-title>
      </v-spacer>
      
      <UserDropdown v-if="!hideUserDropdown"/>
    </v-app-bar>
  </header>
</template>

<script>
import UserDropdown from './UserDropdown'

export default {
  name: "Header",
  components: {UserDropdown },
  props: {
    title: String,
    hideToggle: Boolean,
    hideUserDropdown: Boolean
  },
  methods: {
    toggleMenu() {
      this.$store.commit("toggleMenu");
    },
  },
};
</script>

<style>
</style>