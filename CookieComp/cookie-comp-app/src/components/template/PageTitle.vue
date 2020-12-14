<template>
  <div class="page-title">
    <v-container class="page-title-container">
      <h3>
        <v-icon size="35px" v-if="icon">{{ icon }}</v-icon>
        {{ main }}
      </h3>
      <h4>{{ sub }}</h4>
    </v-container>

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
.page-title-container {
  margin-left: 9px;
}
.page-title{
  margin-bottom: 10px;

}
.page-title h3{
  color: #3b3b3b;
  margin: 0px;
  font-size: 1.72rem;
  
}

.page-title h4{
  color: #777;
  margin-top: 2px;
  font-size: 1.2rem;
}
</style>