<template>
<v-main class="bg-grey-darken-2">
      <v-container>
        <v-row>
          <v-col cols="2">
            <v-sheet rounded="lg">
                <v-list class="bg-grey-darken-3" rounded="lg">
                    <v-btn
                    v-for="n in select_Grow"
                    :key="n['title']"
                    :text="n['title']"
                    class="bg-grey-darken-3"
                    style="width: 350px; height: 60px;"
                    @click="goActivity(n['activity'])"
                    ></v-btn>
                    
                  </v-list>
                </v-sheet>
              </v-col>
              
              <v-col>
              <v-sheet
              min-height="90vh"
              rounded="lg"
              class="bg-grey-darken-3"
              >
              <v-dialog v-model="hamb">
                <v-img 
                class="rote"
                :src="_qkq"
                style="width: 600px; left: 600px; "
                ></v-img>
              </v-dialog>
              <v-img :src="jh1" style="width: 800px;"></v-img>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
    <v-dialog v-model="dialog" max-width="800">
      <div  id="text_box" class="bg-grey-darken-3 ">
        <h1 @click="next_text()" id="name" class="white-text">{{ name }}</h1>
        <p id="text" >{{ card_text }}</p>
      </div>
    </v-dialog>

    <v-dialog v-model="hamb">
      <v-img 
      style="width: 600px;"
      :src="jhface"></v-img> 
    </v-dialog>
    <v-dialog v-model="rnrjf__">
      <v-img 
      :src="_rnrjf"></v-img> 
    </v-dialog>
</template>

<script setup>
import jh1 from '@/assets/Good3.png'
// import ham from '@/assets/jwjwjw.gif'
import _qkq from '@/assets/qkq.png'
import jhface from '@/assets/Buuuugggga.png'
import _rnrjf from '@/assets/rnrjf.gif'
// import 
// import jh2 from '@/assets/GoodYJH.png'
// import jh3 from '@/assets/jihwangood.png'

const select_Grow = [
    {'title': '밥 먹이기', 'activity':'qkq'},
    {'title': '옷 입히기', 'activity':'dht'},
    {'title': '구걸하기', 'activity':'rnrjf'},
    {'title': '재우기', 'activity':'sleep'},
]

</script>

<script>
export default {
  name: 'JihwanGrow',
  data() {
    return {
      hamb: false,
      dialog: false,
      card_text: '클릭',
      name: '클릭',
      stats: 'qkq',
      stac: 0,
      qkq_text_list: [
        {'name': '나', 'text': '밥을 한 번 줘볼께요'},
        {'name': '나', 'text': '밥을 한 번 줘볼께요'},
        {'name': '양지환', 'text': '밥을 받았어요'},
        {'name': '양지환', 'text': '한 번 먹어볼께요'},
        {'name': '나', 'text': '잠깐!!'},
        {'name': '양지환', 'text': '먹기전에 댄스를 추고'},
        {'name': '양지환', 'text': '이제 먹어볼께요'},
      ],

      rnrjf_text_list: [
        {'name': '나', 'text': '음식 살 돈이 없어졌어요'},
        {'name': '나', 'text': '돈을 구해볼까요?'},
        {'name': '양지환', 'text': '기타를 쳐서 구걸을 해보아요'},
      ],
    };
  },


  methods: {
    next_text() {
      console.log(this.qkq_text_list.length)
      if (this.stac >= this.qkq_text_list.length - 1) {
        this.dialog = false;
        this.hamb = true;
        return
      }
      
      this.stac += 1
      this.changText(this.qkq_text_list[this.stac])
    },

    changText(info) {
      this.name = info['name'];
      this.card_text = info['text'];
    },

    openText() {
      this.dialog = true;
    },

    delay(ms, action) {
      return new Promise(resolve => {
        setTimeout(() => {
          action();
          resolve();
        }, ms);
      });
    },

    go_qkq() {
      this.openText()
    },

    go_dht() {

    },

    go_rnrjf() {
      this.rnrjf = true;
    },

    go_sleep() {
      
    },

    goActivity(acti) {
    if (acti == 'qkq') {
      this.openText()
      
    }
     
    else if (acti == 'dht') {
        this.go_dht()
    }

    else if (acti == 'rnrjf') {
      this.rnrjf__ = true;
      this.go_rnrjf()
    }

    else if (acti == 'sleep') {
      this.go_sleep()
    }

  }
},
}

</script>

<style scoped>
.transparent-card {
  background: rgba(255, 255, 255, 0.7); /* 반투명한 배경색 지정 (255, 255, 255은 흰색, 0.7은 투명도 조절) */
  padding: 16px; /* 적절한 여백 설정 */
}

.white-text {
  color: white;
}

.ab {
  position: absolute;
}

.rote {
  animation: RotateHam 1s linear infinite;
}

@keyframes RotateHam {
  0% {
    transform: rotate(0deg);
    left: 600px;
    width: 600px;
  }

  50% {
    transform: rotate(180deg);
  }

  100% {
    transform: rotate(360deg);
    left: 260px;
    width: 30px;
  }
}
</style>
