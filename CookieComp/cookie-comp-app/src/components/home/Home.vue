<template>
  <div class="home">
    <PageTitle icon="mdi-home" main="Dashboard" sub="Cookie Computação" />
    <div class="stats">
            <Stat title="Categorias" :value="0"
                icon="mdi-folder" color="#d54d50" />
            <Stat title="Artigos" :value="0"
                icon="mdi-newspaper-variant-outline" color="#3bc480" />
            <Stat title="Usuários" :value="0"
                icon="mdi-account" color="#3282cd" />
        </div>
  </div>
</template>

<script>
import PageTitle from "../template/PageTitle.vue";
import Stat from './Stat'

export default {
  name: "Home",
  components: { PageTitle, Stat },
  data: function() {
    return {
      stat: {}
    }
  }
};
</script>

<style>
.stats {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
    }
</style>