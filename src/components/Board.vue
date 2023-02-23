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
          <div @click="go_boards_id(dask.id)"
               class="hover:bg-[#afb7c3] my-[5px] mx-[10px] p-[2px] rounded"
               style="overflow-wrap: break-word;">
            {{ dask.name }}
          </div>
        </div>
      </div>
    </div>
    <div class="flex bg-green-500 p-[10px] w-full">
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
                    @click="edit_task(col,index)"
                    style="word-wrap: break-word;"
                    class="rounded p-[3px] pl-[5px] bg-white cursor-pointer select-none hover:bg-[#f4f5f7]">
                  <span>{{ columns.tasks[index] }}</span>
                </div>
              </div>
            </div>
            <template v-if="is_add_card === col">
              <textarea rows="3" placeholder="Ввести заголовок для этой карточки"
                        class="resize-none w-full rounded p-[3px] pl-[5px]"
                        v-model="msg_card"></textarea>
              <div class="flex">
                <button class="py-[3px] px-[10px] bg-[#007ac0] hover:bg-[#006aa8] rounded">
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
            <button @click="is_add_colum=false; name_colum=''">
              <img class="h-[30px]" src="@/assets/icons/close_FILL0_wght400_GRAD0_opsz48.svg" alt="x">
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Board_",
  props: ['id'],
  data() {
    return {
      board: {
        name: "Доска 1",
        background_color: '#0079bf',
        id: "1",
        columns: [
          {
            name: "Дела на утро",
            tasks: ["Помыть посуду", "Пораньше покакать"]
          },
          {
            name: "Что нужно сделать днём",
            tasks: ["Поесть", "Сделать уроки11111111111111111111111111111111111111111111111"]
          },
          {
            name: "Перед сном",
            tasks: ["Почистить зубы"]
          },
          {
            name: "Выполненные",
            tasks: []
          }]
      },
      boards: [{name: "Доска 1", background_color: "#0079bf", id: "1"},
        {name: "доска 2", background_color: "#dc1f1f", id: "2"},
        {name: "Дос3", background_color: "#111", id: "3"},
        {name: "dasdqwarw", background_color: "#FFF", id: "6"},
        {name: "Доска 1", background_color: "#36bf00", id: "4"},
        {name: "доска 2", background_color: "#9900ff", id: "5"},
        {name: "Дос3", background_color: "#0e1750", id: "7"},
        {name: "dasdqwarw", background_color: "#ab912b", id: "8"},
        {name: "Доска 1", background_color: "#0079bf", id: "9"},
        {name: "доска 2", background_color: "#999", id: "10"},
        {name: "Дос3", background_color: "#111", id: "11"},
        {name: "dasdqwarwfffffffff", background_color: "#FFF", id: "12"},],
      is_add_card: null,
      is_add_colum: false,
      msg_card: "",
      name_colum: ""
    }
  },
  methods: {
    go_boards() {
      this.$router.push('/boards')
    },
    go_boards_id(id) {
      this.$router.push('/board' + id.toString())
    },
    edit_task(col, index) {
      console.log(col, index)
    },
    add_card(col) {
      this.is_add_card = col
    },
    delete_colum(col) {
      console.log(col)
    },
    add_colum() {
      if (this.name_colum.length === 0) {
        return
      }
    }
  },
}
</script>

<style scoped>
</style>