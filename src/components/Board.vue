<template>
  <div class="flex">
    <div class="flex-col bg-[#cfd9e7] border-t border-r border-[#bcc7d7] min-w-[120px] text-center min-h-screen">
      <div class="mx-[10px] flex justify-center">
        <img @click="go_boards" class="cursor-pointer rounded hover:bg-[#afb7c3]"
             src="@/assets/icons/undo_FILL0_wght400_GRAD0_opsz48.svg" alt="img" style="height: 25px">
      </div>
      <div class="py-[19px] border-y border-[#bcc7d7]">
        <span>{{ board.name }}</span>
      </div>
      <div class="select-none cursor-pointer">
        <div v-for="dask in boards" v-bind:key="dask">
          <template v-if="dask.id === board.id">
            <div class="bg-[#afb7c3] my-[5px] mx-[10px] p-[2px] rounded"
                 style="overflow-wrap: break-word;">
              {{ dask.name }}
            </div>
          </template>
          <template v-else>
            <div @click="go_boards_id(dask.id)"
                 class="hover:bg-[#afb7c3] my-[5px] mx-[10px] p-[2px] rounded"
                 style="overflow-wrap: break-word;">
              {{ dask.name }}
            </div>
          </template>
        </div>
      </div>
    </div>
    <div class="flex p-[10px] w-full bg_color">
      <div class="mr-[8px] p-[5px] bg-[#ecedf0] rounded w-[20%] h-fit relative z-20"
           v-for="(columns,col) in board.columns"
           v-bind:key="columns">
        <button @click="delete_colum(col)"
                class="mt-[-5px] text-2xl bg-gray-400 hover:bg-gray-600 rounded absolute z-10 right-0">
          <img class="h-[25px]" src="@/assets/icons/close_FILL0_wght400_GRAD0_opsz48.svg" alt="X">
        </button>
        <div>
          <input class="rounded p-[3px] pl-[5px] cursor-pointer focus:bg-white focus:outline-blue-500 bg-transparent"
                 type="text" v-model="columns.name">
          <div class="pt-[10px]">
            <div class="flex my-[7px]" v-for="(task,index) in columns.tasks" v-bind:key="index">
              <div class="w-full">
                <div
                    @click="go_modal(col,index)"
                    style="word-wrap: break-word;"
                    data-bs-toggle="modal" data-bs-target="#exampleModal"
                    class="rounded p-[3px] pl-[5px] bg-white cursor-pointer select-none hover:bg-[#f4f5f7]">
                  <span>{{ columns.tasks[index].msg }}</span>
                </div>
              </div>
            </div>
            <template v-if="is_add_card === col">
              <textarea rows="3" placeholder="Ввести заголовок для этой карточки"
                        class="resize-none w-full rounded p-[3px] pl-[5px]"
                        v-model="msg_card"></textarea>
              <div class="flex">
                <button @click="add_card(col)"
                        class="py-[3px] px-[10px] bg-[#007ac0] hover:bg-[#006aa8] rounded">
                  <span class="text-white">Добавить карточку</span>
                </button>
                <button class="ml-[5px]">
                  <img @click="is_add_card=null; msg_card=''"
                       class="p-[6px] h-[40px]"
                       src="@/assets/icons/close_FILL0_wght400_GRAD0_opsz48.svg"
                       alt="x">
                </button>
              </div>
            </template>
            <template v-else>
              <button @click="is_add_card=col; msg_card=''"
                      class="w-full flex rounded pl-[10px] hover:bg-[#dbdce3]">
                <span class="text-[#5e6c84]"
                      style="font-family: 'Roboto-Light',sans-serif">
                  + Добавить карточку
                </span>
              </button>
            </template>
          </div>
        </div>
      </div>
      <div class="w-[260px] h-fit bg-[#ecedf0] rounded">
        <button @click="is_add_colum = true" v-bind:class="{'hidden': is_add_colum}"
                class="bg-[#c4cdda] rounded p-[8px] w-full">
          <span class="text-[#172b4d]">+ Добавить ещё одну колонку</span>
        </button>
        <div class="p-[5px]" v-bind:class="{'hidden': !is_add_colum}">
          <input v-model="name_colum"
                 class="py-[3px] pl-[5px] rounded focus:outline-blue-500"
                 type="text" placeholder="Ввести заголовок списка">
          <div class="flex mt-[5px]">
            <button @click="add_colum"
                    class="bg-[#0079bf] hover:bg-[#006aa8] px-[6px] py-[3px] rounded">
              <span class="text-white">Добавить список</span>
            </button>
            <button @click="is_add_colum = false;name_colum = ''">
              <img class="h-[30px]" src="@/assets/icons/close_FILL0_wght400_GRAD0_opsz48.svg" alt="x">
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- Модальное окно -->
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Изменить карточку</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button>
        </div>
        <div class="modal-body">
          <textarea v-model="msg_model.msg"
                    class="w-full min-h-[30vh] rounded border-2 border-[#0d6efd] p-[5px]"></textarea>
        </div>
        <div class="modal-footer">
          <template v-if="is_success_delete">
            <button type="button" class="btn btn-success">Успешно</button>
          </template>
          <template v-else>
            <button @click="delete_task"
                    data-bs-dismiss="modal" type="button" class="btn btn-danger">Удалить карточку
            </button>
          </template>
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Отмена</button>
          <template v-if="is_success_edit">
            <button type="button" class="btn btn-success">Успешно</button>
          </template>
          <template v-else>
            <button @click="edit_task"
                    type="button" class="btn btn-primary">Сохранить изменения
            </button>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import user_data from "@/data/user_data";
import axios from "axios";

export default {
  name: "Board_",
  props: ['id'],
  async mounted() {
    await this.main()
  },
  watch: {
    '$route.params.id'() {
      this.main()
    }
  },
  data() {
    return {
      board: {
        name: "",
        background_color: '',
        id: "",
        columns: [
          {
            name: "",
            tasks: [
              {
                "id": null,
                "msg": null
              },
            ]
          },
        ]
      },
      boards: [],
      is_add_card: null,
      is_add_colum: false,
      msg_card: "",
      name_colum: "",
      msg_model: {"msg": "", "col": null, "index": null},
      is_success_delete: null,
      is_success_edit: null,
    }
  },
  methods: {
    main: async function () {
      let res = await this.req_get_board()
      this.boards = JSON.parse(JSON.stringify(res.data.boards))

      res = await this.req_post_board(this.$route.params.id)
      this.board = JSON.parse(JSON.stringify(res.data.board))
      this.board['columns'] = JSON.parse(JSON.stringify(res.data.columns))
      for (let i = 0; i < this.board.columns.length; i++) {
        this.board.columns[i]["tasks"] = res.data.tasks[i]
        console.log(this.board.columns[i])
      }
    },
    go_boards() {
      this.$router.push('/boards')
    },
    go_boards_id(id) {
      this.$router.push('/board/' + id.toString())
    },
    go_modal(col, index) {
      this.msg_model.msg = this.board.columns[col].tasks[index].msg
      this.msg_model.col = col
      this.msg_model.index = index
      this.is_success_delete = false
      this.is_success_edit = false
    },
    edit_task: async function () {
      if (this.board.columns[this.msg_model.col].tasks[this.msg_model.index].msg === this.msg_model.msg) {
        return
      }
      const data = {
        "id": this.board.columns[this.msg_model.col].tasks[this.msg_model.index].id,
        "msg": this.msg_model.msg
      }
      const res = await this.req_put_task(data)
      if (res.data.response === 'yes') {
        this.is_success_edit = true
        this.board.columns[this.msg_model.col].tasks[this.msg_model.index].msg = this.msg_model.msg
      }
    },
    delete_task: async function () {
      const res = await this.req_delete_task(this.board.columns[this.msg_model.col].tasks[this.msg_model.index].id)
      console.log(res.data)
      if (res.data.response === 'yes') {
        this.board.columns[this.msg_model.col].tasks.splice(this.msg_model.index, 1)
        this.is_success_delete = true
      }
    },
    add_card: async function (col) {
      if (this.msg_card.length < 1) {
        return
      }
      this.is_add_card = col
      const data = {
        "board_id": this.board.id,
        "column_id": this.board.columns[col].id,
        "msg": this.msg_card
      }
      const res = await this.req_post_task(data)
      if (res.data.response === 'yes') {
        const task = {
          "id": res.data.task_id,
          "msg": this.msg_card
        }
        if ("tasks" in this.board.columns[col]) {
          this.board.columns[col].tasks.push(task)
        } else {
          this.board.columns[col]['tasks'] = [task]
        }

      }
      this.msg_card = ""
      this.is_add_card = false
    },
    delete_colum: async function (col) {
      const data = {
        "board_id": this.board.id,
        "id": this.board.columns[col].id
      }
      const res = await this.req_delete_colum(data)
      if (res.data.response === 'yes') {
        this.board.columns.splice(col, 1)
      }
    },
    add_colum: async function () {
      if (this.name_colum.length === 0) {
        return
      }
      const data = {
        "name": this.name_colum,
        "id": this.board.id
      };
      const res = await this.req_post_createColum(data);
      if (res.data.response === 'yes') {
        const _ = {
          "name": this.name_colum,
          "id": res.data.column_id,
          "tasks": []
        }
        this.board.columns.push(_)
        this.is_add_colum = false
        this.name_colum = ''
      }
    },

    create_config() {
      return {
        headers: {
          'Authorization': "Bearer " + localStorage.token
        }
      }
    },
    req_get_board: async function () {
      const allBoards_url = user_data[0].api_url + '/board'
      console.log('requests from:', allBoards_url)

      const res = await axios.get(allBoards_url, this.create_config())
      return res
    },
    req_post_board: async function (id) {
      const url = `${user_data[0].api_url}/board?board_id=${id.toString()}`
      console.log('requests from:', url)

      const res = await axios.post(url, {}, this.create_config())
      return res
    },
    req_post_createColum: async function (data) {
      const url = `${user_data[0].api_url}/createColum?colum_name=${data.name}&board_id=${data.id.toString()}`
      console.log('requests from:', url)

      const res = await axios.post(url, {}, this.create_config())
      return res
    },
    req_delete_colum: async function (data) {
      const url = `${user_data[0].api_url}/colum?column_id=${data.id}&board_id=${data.board_id.toString()}`
      console.log('requests from:', url)

      const res = await axios.delete(url, this.create_config())
      return res
    },
    req_post_task: async function (data) {
      const url = `${user_data[0].api_url}/task?board_id=${data.board_id}&column_id=${data.column_id}&msg=${data.msg}`
      console.log('requests from:', url)

      const res = await axios.post(url, {}, this.create_config())
      return res
    },
    req_delete_task: async function (id) {
      const url = `${user_data[0].api_url}/task?task_id=${id}`
      console.log('requests from:', url)

      const res = await axios.delete(url, this.create_config())
      return res
    },
    req_put_task: async function (data) {
      const url = `${user_data[0].api_url}/task`
      console.log('requests from:', url)

      const res = await axios.put(url, data, this.create_config())
      return res
    }
  },
}
</script>

<style scoped>

.bg_color {
  background-color: v-bind('board.background_color');
}
</style>