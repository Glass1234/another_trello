<template>
  <Header_/>
  <Main_web/>
</template>

<script>
import Header_ from "@/components/MainPage/Header_.vue";
import Main_web from "@/components/MainPage/Main_web.vue";

export default {
  name: "Main_page",
  components: {
    Header_,
    Main_web
  }
}
</script>

<style scoped>

</style>