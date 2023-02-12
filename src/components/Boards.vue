<template>
  <div class="p-[15px] flex w-full"
       style="font-family: 'Roboto-Medium',sans-serif">
    <div class="text-[14px] w-[240px]">
      <div class="flex flex-col select-none">
        <div @click="tab_content = 1" v-bind:class="{'bg-[#babab8]':tab_content === 1}"
             class="p-[5px] rounded-[4px] flex items-center hover:bg-[#e7e9ed]">
          <img class="h-[20px]"
               src="@/assets/icons/new_window_FILL0_wght400_GRAD0_opsz48.svg" alt="img">
          <span class="pl-[8px]">Создание</span>
        </div>
        <div @click="tab_content = 2" v-bind:class="{'bg-[#babab8]':tab_content === 2}"
             class="mt-[5px] rounded-[4px] p-[5px] flex items-center hover:bg-[#e7e9ed]">
          <img class="h-[20px]"
               src="@/assets/icons/edit_FILL0_wght400_GRAD0_opsz48.svg" alt="img">
          <span class="pl-[8px]">Редактирование</span>
        </div>
        <div @click="tab_content = 3" v-bind:class="{'bg-[#babab8]':tab_content === 3}"
             class="mt-[5px] rounded-[4px] p-[5px] flex items-center hover:bg-[#e7e9ed]">
          <img class="h-[20px]"
               src="@/assets/icons/folder_copy_FILL0_wght400_GRAD0_opsz48.svg" alt="img">
          <span class="pl-[8px]">Все доски</span>
        </div>
      </div>
    </div>
    <div class="border-l-[3px] mx-[3px]"></div>
    <div class="w-full bg-[#f5f6f7] rounded-[5px]">
      <div class="p-[5px] text-[13px]">

        <template v-if="tab_content === 1">
          <div class="flex items-center">
            <img class="h-[22px]"
                 src="@/assets/icons/format_paint_FILL0_wght400_GRAD0_opsz48.svg"
                 alt="img">
            <span class="text-[#5e6c84]">Выбирите фон:</span>
            <ul class="flex w-[230px] justify-evenly">
              <li class="color_default color_select bg-[#0079bf]" @click="board_background_color = '#0079bf'">
                <button></button>
              </li>
              <li class="color_default color_select bg-[#d29034]" @click="board_background_color = '#d29034'">
                <button></button>
              </li>
              <li class="color_default color_select bg-[#519839]" @click="board_background_color = '#519839'">
                <button></button>
              </li>
              <li class="color_default color_select bg-[#b04632]" @click="board_background_color = '#b04632'">
                <button></button>
              </li>
              <li class="color_default color_select bg-[#89609e]" @click="board_background_color = '#89609e'">
                <button></button>
              </li>
            </ul>
          </div>
          <div class="flex flex-col mt-[15px] ml-[5px]">
            <p class="text-[#5e6c84]">Заголовок доски<span class="text-red-600"> *</span></p>
            <input type="text"
                   v-model="board_name"
                   class="w-[280px] h-[34px] my-[7px] border-2 border-[#8086f2] rounded focus:border-[#eb4034] hover:border-[#eb4034] duration-100">
            <div class="flex items-center" :class="{ 'hidden': board_name.length > 0 }">
              <img src="@/assets/icons/waving_hand_FILL0_wght400_GRAD0_opsz48.svg" alt="img" class="h-[20px]">
              <span style="font-family: 'Roboto-Regular',sans-serif" class="pl-[5px]">
              Укажите название доски.
            </span>
            </div>
          </div>
          <div class="ml-[4px] mt-[15px]">
            <template v-if="board_name.length > 0">
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
        </template>

        <template v-if="tab_content === 2">
          <span class="text-[16px]">Отредактировать или удалить доску</span>
          <br>
          <ul>
            <li v-for="(board) in boards" v-bind:key="board">
              <div class="text-[13px] rounded my-[10px] flex justify-between"
                   :style="{'background-color': board.background_color}">
                <div class="p-[10px]">
                  <div>
                    <div class="bg-white inline rounded p-[2px]">Имя:</div>
                    <br>
                    <input type="text" placeholder="Изменить имя доски" v-model="board.name"
                           class="rounded p-[3px] mt-[3px]">
                  </div>
                  <div class="mt-[15px]">
                    <div class="bg-white inline rounded p-[2px]">Цвет фона:</div>
                    <br>
                    <input type="text" placeholder="#fff" v-model="board.background_color"
                           class="rounded p-[3px] mt-[3px]">
                  </div>
                </div>
                <div class="p-[10px] text-[16px] flex flex-col justify-between">
                  <div class="flex content-end">
                    <button class="bg-red-600 rounded border-black border-2"><span
                        class="px-[10px] py-[3px] text-white">Удалить доску</span></button>
                  </div>
                  <div class="flex">
                    <button class="bg-green-500 rounded border-black border-2"><span
                        class="px-[10px] py-[3px] text-black">Сохранить</span></button>
                    <button class="bg-gray-500 rounded border-black border-2 ml-[10px]"><span
                        class="px-[10px] py-[3px] text-black">Отмена</span></button>
                  </div>
                </div>
              </div>
            </li>
          </ul>

        </template>

        <template v-if="tab_content === 3">
          <div>
            <span class="text-[16px]">Ваши доски:</span>
            <br>
            <input type="text" placeholder="Поиск" v-model="search_board"
                   class="text-[14px] w-[280px] h-[34px] my-[7px] border-2 border-[#32a852] rounded">
          </div>
          <div>
            <ul>
              <li v-for="(board,index) in boards" v-bind:key="board">
                <div class="w-[280px] h-[200px] my-[10px] rounded flex justify-center items-center cursor-pointer"
                     :style="{'background-color': board.background_color}"
                     v-if="board.name.indexOf(search_board)!==-1"
                     @click="go_board(index)">
                  <span class="bg-white rounded p-[5px]">{{ board.name }}</span>

                </div>
              </li>
            </ul>
          </div>
        </template>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "v-Boards",
  data() {
    return {
      board_name: "",
      board_background_color: "#0079bf",
      tab_content: 1,
      search_board: '',
      boards: [{name: "Доска 1", background_color: "#0079bf"},
        {name: "доска 2", background_color: "#dc1f1f"},
        {name: "Дос3", background_color: "#111"},
        {name: "dasdqwarw", background_color: "#FFF"},
        {name: "Доска 1", background_color: "#36bf00"},
        {name: "доска 2", background_color: "#9900ff"},
        {name: "Дос3", background_color: "#0e1750"},
        {name: "dasdqwarw", background_color: "#ab912b"},
        {name: "Доска 1", background_color: "#0079bf"},
        {name: "доска 2", background_color: "#999"},
        {name: "Дос3", background_color: "#111"},
        {name: "dasdqwarw", background_color: "#FFF"},],
    }
  },
  methods: {
    creat_board() {
      console.log(this.board_name, this.board_background_color)
    },
    go_board(index) {
      console.log(index)
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