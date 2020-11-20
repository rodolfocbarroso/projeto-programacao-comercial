<template>
  <div id="app">
    <Header title="Cookie Comp"/>
    <Menu />
    <Content />
    <Footer />
  </div>
</template>

<script>
import Header from "@/components/template/Header";
import Menu from "@/components/template/Menu";
import Content from "@/components/template/Content"
import Footer from "@/components/template/Footer";

export default {
  name: "App",
  components: { Header, Menu, Content, Footer }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

</style>
