<template>
  <div class="bg-[#f9fafc]">
    <div class="min-h-screen"
         style="background: url('@/assets/img/signup-left.svg') no-repeat left bottom,
                             url('@/assets/img/signup-right.svg') no-repeat right bottom;
                             background-size: 20%">
      <header>
        <div @click="go_main" class="pt-[40px]">
          <img class="m-auto cursor-pointer"
               src="@/assets/icons/trello-logo-blue.svg"
               alt="img">
        </div>
        <div class="flex bg-white">
        </div>
      </header>
      <div class="flex justify-center pt-[40px]">
        <div class="bg-white px-[40px] py-[25px] rounded-[3px]"
             style="box-shadow: rgb(0 0 0 / 10%) 0 0 10px;">
          <div class="w-[320px]"
               style="font-family: 'SpaceGrotesk-Bold',sans-serif">
            <h3 class="font-bold text-[#5e6c84] text-center mb-[25px]">Log in to Trello</h3>
            <div class="flex flex-col"
                 style="font-family: 'Roboto-Light',sans-serif">
              <input type="email" placeholder="Enter email" v-model="email_login"
                     class="rounded-[3px] border-[#dfe1e6] border-[2px] p-[7px] mb-[17px] font-light">
              <input type="password" placeholder="Enter passwd" v-model="passwd_login"
                     class="rounded-[3px] border-[#dfe1e6] border-[2px] p-[7px] mb-[17px] font-light">
              <button class="bg-[#5aac44] hover:bg-[#61BD4F] rounded-[5px] py-[8px]"><span class="text-white font-bold"
                                                                                           style="font-family: 'SpaceGrotesk-Bold',sans-serif">Login</span>
              </button>
            </div>
          </div>
          <p class="font-extralight text-[#4d4d4d] text-center py-[16px]"
             style="font-family: 'Roboto-Light',sans-serif">OR</p>
          <div class="w-[320px] mt-[25px]">
            <h3 class="font-bold text-[#5e6c84] text-center mb-[25px]"
                style="font-family: 'SpaceGrotesk-Bold',sans-serif">Sign up for Trello</h3>
            <div class="flex flex-col"
                 style="font-family: 'Roboto-Light',sans-serif">
              <input type="email" placeholder="Enter email" v-model="email_sign"
                     class="rounded-[3px] border-[#dfe1e6] border-[2px] p-[7px] mb-[17px] font-light">
              <input type="password" placeholder="Enter passwd" v-model="passwd1_sign"
                     class="rounded-[3px] border-[#dfe1e6] border-[2px] p-[7px] mb-[17px] font-light">
              <input type="password" placeholder="Enter passwd" v-model="passwd2_sign"
                     class="rounded-[3px] border-[#dfe1e6] border-[2px] p-[7px] mb-[17px] font-light">
              <button class="bg-[#0066ff] hover:bg-[#003f9e] rounded-[5px] py-[8px]"><span class="text-white font-bold"
                                                                                           style="font-family: 'SpaceGrotesk-Bold',sans-serif">Sing up</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Authorization_main",
  data() {
    return {
      email_login: "", passwd_login: "",
      email_sign: "", passwd1_sign: "", passwd2_sign: ""
    }
  },
  methods: {
    go_main() {
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>

</style>