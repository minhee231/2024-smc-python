<template>
    <v-main class="bg-grey-darken-2">
    <v-sheet  min-height="100vh" class="bg-grey-darken-2">
        <v-btn
            v-for = "i in 1218"
            :key="i"
            :text="i"
            :id="'Box' + i"
            class="bg-orange-accent-2"
            variant="text"
            :style="{ width:'60px', height: '60px'}"
            @click="clickBT(i)"
        ></v-btn>
        <v-dialog v-model="dialog" max-width="800">
        <H1 style="color: red;">축하드립니다 당신은 양지환선생님을 찾았습니다!</H1>
        <v-img :src="Good" width="100%" height="100%" object-fit="contain"></v-img>
    </v-dialog>
    </v-sheet>
    </v-main>
</template>
    
    

<script setup>
import Good from '@/assets/GoodYJH.png'

</script>

<script>
export default {
  name: 'FoundJiHwan',


  data() {
    return {
      dialog: false,
      randomNumber: 0,
    };
  },

  mounted() {
    this.randomNumber = this.generateRandomNumber();
  },

  methods: {
    generateRandomNumber() {
      return Math.floor(Math.random() * 1218);
    },

    clickBT(id) {
      const element = document.getElementById(`Box${id}`);
      if (element) {
        element.textContent = '';
        element.classList.add('bg-orange-accent-3');
        element.classList.remove('bg-orange-accent-2'); 

        if (this.randomNumber == id) {
          console.log('찾았다!!!');
          this.dialog = true;
        }
      }
    },
  },
};
</script>

