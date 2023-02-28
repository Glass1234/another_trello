<template>
  <div class="bg-[#f9fafc]">
    <div class="min-h-screen bg-img">
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
              <template v-if="is_valid_login===1">
                <span>Укажите почту</span>
                <br>
              </template>
              <template v-else-if="is_valid_login===2">
                <span>Укажите пароль</span>
                <br>
              </template>
              <template v-if="is_success_login===true">
                <span class="text-green-600">{{ tmp.response }}</span>
                <br>
              </template>
              <template v-if="is_success_login===false">
                <span class="text-red-600">{{ tmp.response }}</span>
                <br>
              </template>
              <button @click="login"
                      class="bg-[#5aac44] hover:bg-[#61BD4F] rounded-[5px] py-[8px]">
                <span class="text-white font-bold" style="font-family: 'SpaceGrotesk-Bold',sans-serif">Login</span>
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
              <template v-if="is_valid===1">
                <p>Укажите почту</p>
                <br>
              </template>
              <template v-else-if="is_valid===2">
                <p>Пароли не совпадают (</p>
                <br>
              </template>
              <template v-else-if="is_valid===3">
                <p>Слишком короткий пароль</p>
                <br>
              </template>
              <template v-if="is_success_sign===false">
                <span class="text-red-600">{{ tmp.response }}</span>
                <br>
              </template>
              <template v-if="is_success_sign===true">
                <span class="text-green-600">{{ tmp.response }}</span>
                <br>
              </template>
              <button @click="sign_up"
                      class="bg-[#0066ff] hover:bg-[#003f9e] rounded-[5px] py-[8px]"><span class="text-white font-bold"
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
import user_data from "@/data/user_data";
import axios from "axios";

export default {
  name: "Authorization_main",
  watch: {},
  data() {
    return {
      email_login: "", passwd_login: "",
      email_sign: user_data[0].sign_email, passwd1_sign: "", passwd2_sign: "",
      is_valid: 0, // 0 = valid
      is_valid_login: 0, // 0 = valid
      is_success_sign: null,
      is_success_login: null,
      tmp: null
    }
  },
  methods: {
    is_valid_mail(mail) {
      const EMAIL_REGEXP = /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/iu;
      return EMAIL_REGEXP.test(mail)
    },
    go_main() {
      this.$router.push('/')
    },
    login: async function () {
      this.is_success_login = null
      this.is_success_sign = null
      if (!this.is_valid_mail(this.email_login)) {
        this.is_valid_login = 1
        return
      }
      if (this.passwd_login.length === 0) {
        this.is_valid_login = 2
        return
      }
      this.is_valid_login = 0

      const data = {
        'user_name': this.email_login,
        'passwd': this.passwd_login
      }
      const data_token = {
        'username': this.email_login,
        'password': this.passwd_login
      }
      const res = await this.send_auth(data, data_token)
      if (res.status_code === 1) {
        this.is_success_login = false
      } else if (res.status_code === 0) {
        this.is_success_login = true
      }
      this.tmp = res
      if (res.status_code === 0) {
        localStorage.token = this.tmp.access_token
        this.$router.push('/boards')
      }
    },
    sign_up: async function () {
      this.is_success_sign = null
      this.is_success_login = null
      if (!this.is_valid_mail(this.email_sign)) {
        this.is_valid = 1
        return
      }
      if (this.passwd1_sign !== this.passwd2_sign) {
        this.is_valid = 2
        return
      }
      if (this.passwd1_sign.length <= 8) {
        this.is_valid = 3
        return
      }
      if (this.passwd1_sign === this.passwd2_sign && this.passwd1_sign.length >= 8 && this.email_sign !== "") {
        this.is_valid = 0
      }
      const data = {
        'user_name': this.email_sign,
        'passwd': this.passwd1_sign
      }

      const res = await this.send_reg(data)
      if (res.status_code === 1) {
        this.is_success_sign = false
      } else {
        this.is_success_sign = true
      }
      this.tmp = res
      if (res.status_code === 0) {
        this.$router.push('/')
      }
    },
    send_reg: async function (data) {
      const url = user_data[0].api_url + '/reg'
      return (await axios.post(url, data)).data
    },
    send_auth: async function (data, data_token) {
      const tk_url = user_data[0].api_url + '/token'
      return (await axios.post(tk_url, new URLSearchParams(
          data_token))).data
    },
  }
}
</script>

<style scoped>
.bg-img {
  background: url("@/assets/img/signup-left.svg") no-repeat left bottom,
  url("@/assets/img/signup-right.svg") no-repeat right bottom;
  background-size: 20%
}

</style>