<template>
  <div class="p-[15px] flex w-full"
       style="font-family: 'Roboto-Medium',sans-serif">
    <div class="text-[14px] w-[240px]">
      <div class="flex flex-col">
        <div class="p-[5px] rounded-[4px] flex items-center hover:bg-[#e7e9ed] ease-in duration-100">
          <img class="h-[20px]"
               src="@/assets/icons/new_window_FILL0_wght400_GRAD0_opsz48.svg" alt="img">
          <span class="pl-[8px]">Создание</span>
        </div>
        <div class="mt-[5px] rounded-[4px] p-[5px] flex items-center hover:bg-[#e7e9ed] ease-in duration-100">
          <img class="h-[20px]"
               src="@/assets/icons/edit_FILL0_wght400_GRAD0_opsz48.svg" alt="img">
          <span class="pl-[8px]">Редактирование</span>
        </div>
        <div class="mt-[5px] rounded-[4px] p-[5px] flex items-center hover:bg-[#e7e9ed] ease-in duration-100">
          <img class="h-[20px]"
               src="@/assets/icons/folder_copy_FILL0_wght400_GRAD0_opsz48.svg" alt="img">
          <span class="pl-[8px]">Все доски</span>
        </div>
      </div>
    </div>
    <div class="border-l-[3px] mx-[3px]"></div>
    <div class="w-full bg-[#f5f6f7] rounded-[5px]">
      <div class="p-[5px] text-[13px]">
        <div class="flex items-center">
          <img class="h-[22px]"
               src="@/assets/icons/format_paint_FILL0_wght400_GRAD0_opsz48.svg"
               alt="img">
          <span class="text-[#5e6c84]">Выбирите фон:</span>
          <ul class="flex w-[230px] justify-evenly">
            <li class="color_default color_select bg-[#0079bf]" @click="boards_background_color = '#0079bf'">
              <button></button>
            </li>
            <li class="color_default color_select bg-[#d29034]" @click="boards_background_color = '#d29034'">
              <button></button>
            </li>
            <li class="color_default color_select bg-[#519839]" @click="boards_background_color = '#519839'">
              <button></button>
            </li>
            <li class="color_default color_select bg-[#b04632]" @click="boards_background_color = '#b04632'">
              <button></button>
            </li>
            <li class="color_default color_select bg-[#89609e]" @click="boards_background_color = '#89609e'">
              <button></button>
            </li>
          </ul>
          <!--          <form>-->
          <!--            <div class="inline-block">-->
          <!--              <div class="inline-block form_color form_radio_btn">-->
          <!--                <input class="hidden" type="radio" id="contactChoice1" name="contact" value="#0079bf">-->
          <!--                <label class="color_default color_select"></label>-->
          <!--              </div>-->
          <!--              <input type="radio" id="contactChoice1"-->
          <!--                     name="contact" value="#d29034">-->
          <!--              <input type="radio" id="contactChoice1"-->
          <!--                     name="contact" value="#519839">-->
          <!--              <input type="radio" id="contactChoice1"-->
          <!--                     name="contact" value="#b04632">-->
          <!--              <input type="radio" id="contactChoice1"-->
          <!--                     name="contact" value="#89609e">-->
          <!--            </div>-->
          <!--          </form>-->

        </div>
        <div class="flex flex-col mt-[15px] ml-[5px]">
          <p class="text-[#5e6c84]">Заголовок доски<span class="text-red-600"> *</span></p>
          <input type="text"
                 v-model="boards_name"
                 class="w-[280px] h-[34px] my-[7px] border-2 border-[#8086f2] rounded focus:border-[#eb4034] hover:border-[#eb4034] duration-100">
          <div class="flex items-center" :class="{ 'hidden': boards_name.length > 0 }">
            <img src="@/assets/icons/waving_hand_FILL0_wght400_GRAD0_opsz48.svg" alt="img" class="h-[20px]">
            <span style="font-family: 'Roboto-Regular',sans-serif" class="pl-[5px]">
              Укажите название доски.
            </span>
          </div>
        </div>
        <div class="ml-[4px] mt-[15px]">
          <template v-if="boards_name.length > 0">
            <button class="bg-[#0079bf] hover:bg-[#026aa7] duration-100 h-[35px] rounded"
                    @click="creat_board">
              <span style="font-family: Roboto-Regular,sans-serif"
                    class="text-white text-[14px] px-[60px] py-[7px]">Создать</span>
            </button>
          </template>
          <template v-else>
            <button disabled class="bg-[#aaadb3] cursor-not-allowed h-[35px] rounded">
              <span style="font-family: Roboto-Regular,sans-serif"
                    class="text-white text-[14px] px-[60px] py-[7px]">Создать</span>
            </button>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "v-Boards",
  data() {
    return {
      boards_name: "",
      boards_background_color: "#0079bf"
    }
  },
  methods: {
    creat_board() {
      console.log(this.boards_name, this.boards_background_color)
    }
  }
}
</script>

<style scoped>
.color_select:hover {
  background-image: url("@/assets/icons/done_FILL0_wght400_GRAD0_opsz48.svg");
}

.color_default {
  cursor: pointer;
  padding: 8px 20px 8px 20px;
  border-radius: 0.25rem;
  background-position: center;
  background-repeat: no-repeat;
}


</style>