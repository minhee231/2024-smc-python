<template>
  <v-app-bar flat color="black">
    <v-container class="mx-auto d-flex align-center justify-center">
      <v-btn
        v-for=" info in header_info"
        :key="info['title']"
        :text="info['title']"
        variant="text"
        @click="goLink(info['link'])"
      ></v-btn>
      <v-spacer></v-spacer>
    </v-container>
  </v-app-bar>
</template>

<script setup>
const header_info = [
{'title': 'Founding Jihwan', 'link': 'http://catch.yjiwhan.store'},
{'title': 'Grow Jihwan', 'link': 'http://grow.yjiwhan.store'}
];

function goLink(link) {
window.open(link, '_blank');
}

</script>

<script>
export default {
  name: 'JihwanHeader',
  data: () => ({

  }),
}
</script>