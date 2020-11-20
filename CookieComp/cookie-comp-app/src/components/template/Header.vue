<template>
  <header>
    <v-app-bar app>
      <v-app-bar-nav-icon @click="toggleMenu"></v-app-bar-nav-icon>

      <v-spacer>
        <v-toolbar-title>
          {{ title }}
        </v-toolbar-title>
      </v-spacer>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>
  </header>
</template>

<script>
export default {
  name: "Header",
  props: {
    title: String,
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