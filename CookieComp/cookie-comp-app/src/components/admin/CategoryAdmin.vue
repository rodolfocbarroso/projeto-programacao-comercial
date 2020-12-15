<template>
  <div class="category-admin">
    <form>
      <input type="hidden" v-model="categoria.id" />

      <v-text-field 
          v-model="categoria.nome" 
          :counter="100" 
          label="Nome">
      </v-text-field>

      <v-select
          v-model="categoria.categoriaPai"
          :items="categorias"
          label="Categoria Pai"
          data-vv-name="select"
      ></v-select>

      <v-btn
        class="mr-4"
        v-if="mode === 'save'"
        @click="save">
        Salvar
      </v-btn>

      <v-btn 
        v-if="mode === 'remove'"
        @click="remove">
        Excluir
      </v-btn>

      <v-btn 
        v-if="mode === 'remove'"
        @click="reset">
        Cancelar
      </v-btn>
    </form>
    <br>
    <v-divider></v-divider>
    <br>
    <v-data-table
      :headers="headers"
      :items="categorias"
      item-key="id"
      :items-per-page="5"
      class="elevation-1">
    </v-data-table>
  </div>
</template>

<script>
import { baseApiUrl, showError } from "@/global";
import axios from "axios";

export default {
  name: "CategoryAdmin",
  data: function () {
    return {
      mode: "save",
      categoria: {},
      categorias: [],
      headers: [
        { text: "Código", align: 'start', sortable: true },
        { text: "Nome", align: 'start', sortable: true },
        { text: "Caminho", align: 'start', sortable: true },
        { text: "Ações" },
      ],
    };
  },
  methods: {
    loadCategorias() {
      const url = `${baseApiUrl}/categorias/`;
      axios.get(url).then((res) => {
        this.categorias = res.data
        console.log(res.data)
        // this.categorias = res.data.map((categoria) => {
        //   return { ...categoria, value: categoria.id, text: categoria.path };
        // });
      });
    },
    reset() {
      this.mode = "save";
      this.categoria = {};
      this.loadCategorias();
    },
    save() {
      const method = this.categoria.id ? "put" : "post";
      const id = this.categoria.id ? `/${this.categoria.id}` : "";
      axios[method](`${baseApiUrl}/categorias${id}`, this.categoria)
        .then(() => {
          this.$toasted.global.defaultSuccess();
          this.reset();
        })
        .catch(showError);
    },
    remove() {
      const id = this.categoria.id;
      axios
        .delete(`${baseApiUrl}/categorias/${id}`)
        .then(() => {
          this.$toasted.global.defaultSuccess();
          this.reset();
        })
        .catch(showError);
    },
    loadCategoria(categoria, mode = "save") {
      this.mode = mode;
      this.categoria = { ...categoria };
    },
  },
  mounted() {
    this.loadCategorias();
  },
};
</script>

<style>
</style>