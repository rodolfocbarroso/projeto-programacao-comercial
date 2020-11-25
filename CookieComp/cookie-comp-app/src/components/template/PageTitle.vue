<template>
  <div class="page-title">
    <h1>
      <v-icon v-if="icon">{{ icon }}</v-icon> {{ main }}
    </h1>
    <h2>{{ sub }}</h2>
    <v-divider></v-divider>
  </div>
</template>

<script>
export default {
  name: "PageTitle",
  props: ["icon", "main", "sub"],
};
</script>

<style>
.page-title h1 {
  margin: 0px;
}
.page-title h2 {
  margin-top: 5px;
  font-size: 1.3rem;
}
</style>