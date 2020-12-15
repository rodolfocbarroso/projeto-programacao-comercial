<template>
  <div class="admin-pages">
    <PageTitle
      icon="mdi-cogs"
      main="Gerenciador"
      sub="Administração do Sistema"
    />
    <div class="admin-pages-tabs">
      <v-tabs>
        <v-tab>Artigos</v-tab>
        <v-tab-item>
          <ArticleAdmin />
        </v-tab-item>
        <v-tab>Categorias</v-tab>
         <v-tab-item>
          <CategoryAdmin />
        </v-tab-item>
        <v-tab>Usuários</v-tab>
         <v-tab-item>
          <UserAdmin />
        </v-tab-item>
      </v-tabs>
    </div>
  </div>
</template>

<script>
import PageTitle from "../template/PageTitle.vue";
import ArticleAdmin from "./ArticleAdmin";
import CategoryAdmin from "./CategoryAdmin";
import UserAdmin from "./UserAdmin";

export default {
  name: "AdminPages",
  components: { PageTitle, ArticleAdmin, CategoryAdmin, UserAdmin },
  data() {
    return {
      tab: null,
      items: ["web", "shopping", "videos", "images", "news"],
    };
  },
};
</script>

<style>
</style>