<template>
  <div class="p-[15px] flex w-full"
       style="font-family: 'Roboto-Medium',sans-serif">
    <div class="text-[14px] w-[240px]">
      <div class="flex flex-col select-none">
        <div @click="tab_content = 1;board_success = false;board_error = false"
             v-bind:class="{'bg-[#babab8]':tab_content === 1}"
             class="p-[5px] rounded-[4px] flex items-center hover:bg-[#e7e9ed]">
          <img class="h-[20px]"
               src="@/assets/icons/new_window_FILL0_wght400_GRAD0_opsz48.svg" alt="img">
          <span class="pl-[8px]">Создание</span>
        </div>
        <div @click="tab_content = 2;board_success = false;board_error = false"
             v-bind:class="{'bg-[#babab8]':tab_content === 2}"
             class="mt-[5px] rounded-[4px] p-[5px] flex items-center hover:bg-[#e7e9ed]">
          <img class="h-[20px]"
               src="@/assets/icons/edit_FILL0_wght400_GRAD0_opsz48.svg" alt="img">
          <span class="pl-[8px]">Редактирование</span>
        </div>
        <div @click="tab_content = 3;board_success = false;board_error = false"
             v-bind:class="{'bg-[#babab8]':tab_content === 3}"
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
                <template v-if="board_background_color === '#0079bf'">
                  <button>+</button>
                </template>
                <button></button>
              </li>
              <li class="color_default color_select bg-[#d29034]" @click="board_background_color = '#d29034'">
                <template v-if="board_background_color === '#d29034'">
                  <button>+</button>
                </template>
                <button></button>
              </li>
              <li class="color_default color_select bg-[#519839]" @click="board_background_color = '#519839'">
                <template v-if="board_background_color === '#519839'">
                  <button>+</button>
                </template>
                <button></button>
              </li>
              <li class="color_default color_select bg-[#b04632]" @click="board_background_color = '#b04632'">
                <template v-if="board_background_color === '#b04632'">
                  <button>+</button>
                </template>
                <button></button>
              </li>
              <li class="color_default color_select bg-[#89609e]" @click="board_background_color = '#89609e'">
                <template v-if="board_background_color === '#89609e'">
                  <button>+</button>
                </template>
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
              <button class="btn btn-primary"
                      @click="creat_board">
              <span style="font-family: Roboto-Regular,sans-serif"
                    class="text-white text-[14px] px-[60px] py-[7px]">Создать</span>
              </button>
            </template>
            <template v-else>
              <button disabled class="btn btn-secondary cursor-not-allowed">
              <span style="font-family: Roboto-Regular,sans-serif"
                    class="text-white text-[14px] px-[60px] py-[7px]">Создать</span>
              </button>
            </template>
          </div>

          <br>
          <div v-bind:class="board_success ? 'show':'hidden'"
               class="ml-[4px] alert alert-success alert-dismissible fade flex justify-between">
            <strong>Доска была успешно создана</strong>
            <button type="button" class="close" data-bs-dismiss="alert">
              X
            </button>
          </div>
          <div v-bind:class="board_error ? 'show':'hidden'"
               class="ml-[4px] alert alert-danger alert-dismissible fade flex justify-between">
            <strong>Ошибка создания доски</strong>
            <button type="button" class="close" data-bs-dismiss="alert">
              X
            </button>
          </div>

        </template>

        <template v-if="tab_content === 2">
          <span class="text-[16px]">Отредактировать или удалить доску</span>
          <ul class="m-0 p-0">
            <li v-for="(board,index) in boards" v-bind:key="board">
              <div class="text-[13px] rounded my-[10px] flex justify-between"
                   :style="{'background-color': board.background_color}">
                <div class="p-[10px]">
                  <div>
                    <div class="bg-white inline rounded p-[2px]">Имя:</div>
                    <br>
                    <input type="text" placeholder="Изменить имя доски" v-model="board.name"
                           class="rounded p-[3px] mt-[3px]" @input="check_name(index)">
                  </div>
                  <div class="mt-[15px]">
                    <div class="bg-white inline rounded p-[2px]">Цвет фона:</div>
                    <br>
                    <input type="text" placeholder="#fff" v-model="board.background_color"
                           class="rounded p-[3px] mt-[3px]" @input="set_color($event, index)">
                  </div>
                </div>
                <div class="p-[10px] text-[16px] flex flex-col justify-between"
                     style="font-family: Roboto-Regular,sans-serif">
                  <div class="flex content-end">
                    <button @click="delete_board(index)"
                            class="btn btn-danger">Удалить доску
                    </button>
                  </div>
                  <div class="flex">
                    <template v-if="boards_not_valid.indexOf(index) === -1 && not_valid_name.indexOf(board.id)=== -1">
                      <button @click="save_board(index)"
                              class="btn btn-success">Сохранить
                      </button>
                    </template>
                    <template v-else>
                      <button class="btn btn-success cursor-not-allowed" disabled>Сохранить</button>
                    </template>
                    <button @click="undo_changes_board(index)"
                            class="btn btn-secondary ml-[10px]">Отмена
                    </button>
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
            <ul class="m-0 p-0">
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


import user_data from "@/data/user_data";
import axios from "axios";

export default {
  name: "v-Boards",
  async mounted() {
    const boards = await this.req_get_all_boards()
    this.boards = JSON.parse(JSON.stringify(boards.data.boards))
    this.boards_dump = JSON.parse(JSON.stringify(boards.data.boards))
  },
  data() {
    return {
      board_name: "",
      board_background_color: "#0079bf",
      tab_content: 1,
      search_board: '',
      boards: [],
      boards_dump: [],
      boards_not_valid: [],
      not_valid_name: [],
      board_success: false,
      board_error: false,
    }
  },
  methods: {
    creat_board: async function () {
      if (this.board_name.length < 1) {
        return
      }
      const data = {
        "name": this.board_name,
        "background_color": this.board_background_color
      }
      const res = await this.req_post_create_board(data)
      if (res.data.response === "yes") {
        data["id"] = res.data.id
        this.boards.push(data)
        this.boards_dump.push(data)
        this.board_success = true
        this.board_error = false
        this.board_name = ""
        this.board_background_color = "#0079bf"
      } else {
        this.board_error = true
        this.board_success = false
      }
    },
    save_board: async function (index) {
      if (this.boards[index].name === this.boards_dump[index].name &&
          this.boards[index].background_color === this.boards_dump[index].background_color) {
        return
      } else {
        this.boards_dump[index].name = this.boards[index].name
        this.boards_dump[index].background_color = this.boards[index].background_color
      }
      const data = {
        "name": this.boards[index].name,
        "background_color": this.boards[index].background_color,
        "id": this.boards[index].id
      }
      const res = await this.req_put_board(data)
      if (res.data.response === 'yes') {
        this.board_success = true
        this.board_error = false
      } else {
        this.board_error = true
        this.board_success = false
      }
    },
    delete_board: async function (index) {
      const data = {
        "id": this.boards[index].id
      }
      const res = await this.req_delete_board(data.id)
      if (res.data.response === 'yes') {
        this.boards.splice(index, 1)
        this.boards_dump.splice(index, 1)
      }
    },
    undo_changes_board(index) {
      this.boards[index].name = this.boards_dump[index].name
      this.boards[index].background_color = this.boards_dump[index].background_color
    },
    go_board(index) {
      this.$router.push('/board/' + this.boards[index].id)
    },
    set_color($event, index) {
      let color = $event.target.value
      let hexColorRegex = require('hex-color-regex')
      const is_valid = hexColorRegex().test(color)
      const index_of = this.boards_not_valid.indexOf(index)

      if (is_valid === false || color.length >= 8) {
        if (index_of === -1) {
          this.boards_not_valid.push(index)
        }
      } else {
        if (index_of !== -1) {
          this.boards_not_valid.splice(index_of, 1)
        }
      }
    },
    check_name(index) {
      const id = this.boards[index].id
      if (this.boards[index].name.length < 1) {
        if (this.not_valid_name.includes(id) === false) {
          this.not_valid_name.push(id)
        }
      } else {
        if (this.not_valid_name.includes(id)) {
          this.not_valid_name.splice(this.not_valid_name.indexOf(id), 1)
        }
      }
    },

    create_config() {
      return {
        headers: {
          'Authorization': "Bearer " + localStorage.token
        }
      }
    },
    req_get_all_boards: async function () {
      const allBoards_url = user_data[0].api_url + '/boards'
      console.log('requests from:', allBoards_url)

      const res = await axios.get(allBoards_url, this.create_config())
      return res
    },
    req_post_create_board: async function (data) {
      const create_board_url = user_data[0].api_url + '/boards'
      console.log('requests from:', create_board_url)

      const res = await axios.post(create_board_url, data, this.create_config())
      return res
    },
    req_put_board: async function (data) {
      const post_edit_board = user_data[0].api_url + '/boards'
      console.log('requests from:', post_edit_board)

      const res = await axios.put(post_edit_board, data, this.create_config())
      return res
    },
    req_delete_board: async function (id) {
      const delete_board_url = `${user_data[0].api_url}/boards?board_id=${id.toString()}`
      console.log('requests from:', delete_board_url)

      const res = await axios.delete(delete_board_url, this.create_config())
      return res
    },
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


.alert-arrow {
  border: 1px solid #60c060;
  color: #54a754;
}

.alert-arrow .alert-icon {
  position: relative;
  width: 3rem;
  background-color: #60c060;
}

.alert-arrow .alert-icon::after {
  content: "";
  position: absolute;
  width: 0;
  height: 0;
  border-top: .75rem solid transparent;
  border-bottom: .75rem solid transparent;
  border-left: .75rem solid #60c060;
  right: -.75rem;
  top: 50%;
  transform: translateY(-50%);
}

.alert-arrow .close {
  font-size: 1rem;
  color: #cacaca;
}

/* primary */
.alert-arrow-primary {
  border: 1px solid #4d90fd;
  color: #3a8ace;
}

.alert-arrow-primary .alert-icon {
  background-color: #4d90fd;
}

.alert-arrow-primary .alert-icon::after {
  border-left: .75rem solid #4d90fd;
}

/* warning */
.alert-arrow-warning {
  border: 1px solid #fc9700;
  color: #d68000;
}

.alert-arrow-warning .alert-icon {
  background-color: #fc9700;
}

.alert-arrow-warning .alert-icon::after {
  border-left: .75rem solid #fc9700;
}

/* danger */
.alert-arrow-danger {
  border: 1px solid #da4932;
  color: #ca452e;
}

.alert-arrow-danger .alert-icon {
  background-color: #da4932;
}

.alert-arrow-danger .alert-icon::after {
  border-left: .75rem solid #da4932;
}

</style>