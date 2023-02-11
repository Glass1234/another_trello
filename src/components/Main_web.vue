<template>
  <div class="bg-no-repeat bg-bottom bg-auto flex justify-center pt-[100px] cloud">
    <div class="flex flex-col"
         style="font-family: 'SpaceGrotesk-Light', sans-serif">
      <div>
        <div class="text-white font-semibold">
          <p class="text-[48px] leading-tight">Trello brings all your<br> tasks, teammates, and<br> tools
            together</p>
          <p class="text-[20px]">Keep everything in the same place—even if your team<br> isn’t.</p>
        </div>
      </div>
      <div class="pt-[30px]">
        <input type="email" placeholder="Email" class="p-[12px] rounded-[0.3rem]" v-model="user_email">
        <button @click="go_auth"
                class="p-[12px] ml-[10px] rounded-[0.3rem] ease-in duration-300 bg-[#0066ff] hover:bg-[#003f9e]">
          <span class="text-white"> Sign up-it's free!</span></button>
        <div class="flex pt-[15px] text-white">
          <button><span class="underline">Watch video</span></button>
          <button><img src="@/assets/icons/play_circle_FILL0_wght400_GRAD0_opsz48.svg" alt="icon"
                       class="h-[40%] pl-[5px]">
          </button>
        </div>
      </div>
    </div>
    <div class="w-[35%]">
      <img src="@/assets/img/TrelloUICollage_4x.png" alt="img">
    </div>
  </div>

</template>

<script>
export default {
  name: "Main_web",
  data() {
    return {user_email: ""}
  },
  methods: {
    go_auth() {
      this.$router.push('/auth')
    }
  }
}
</script>

<style scoped>
.cloud {
  background-image: url('@/assets/icons/white-wave-bg.svg'), linear-gradient(90deg, #354dc0, #813ba8, #a52a8a);
  background-size: 100% auto;
}
</style>