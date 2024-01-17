<template>
  <v-app>
    <v-main>
      <JihwanHeader></JihwanHeader>
      <JihwanGrow></JihwanGrow>
    </v-main>
  </v-app>
</template>

<script>
import JihwanHeader from './components/Herder.vue'
import JihwanGrow from './components/Grow.vue'


export default {
  name: 'App',

  components: {
    JihwanHeader,
    JihwanGrow

},

  data: () => ({
    //
  }),
}
</script>

