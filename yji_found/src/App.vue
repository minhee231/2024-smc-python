<template>
  <v-app>
    <v-main>
      <JihwanHeader></JihwanHeader>
      <RouterView></RouterView>
    </v-main>
  </v-app>
</template>

<script>
import { RouterView } from 'vue-router';
import JihwanHeader from './components/Herder.vue'


export default {
  name: 'App',

  components: {
    JihwanHeader,
    RouterView,
},

  data: () => ({
    //
  }),
}
</script>
