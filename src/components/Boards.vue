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
      <div class="p-[5px]">
        <div class="flex items-center">
          <img class="h-[22px]"
               src="@/assets/icons/format_paint_FILL0_wght400_GRAD0_opsz48.svg"
               alt="img">
          <span>Выбирите фон:</span>
          <ul class="flex w-[230px] justify-evenly">
            <li class="w-[40px] h-[32px] bg-[#0079bf] rounded"><button class="w-full h-full"></button></li>
            <li class="w-[40px] h-[32px] bg-[#d29034] rounded"><button class="w-full h-full"></button></li>
            <li class="w-[40px] h-[32px] bg-[#519839] rounded"><button class="w-full h-full"></button></li>
            <li class="w-[40px] h-[32px] bg-[#b04632] rounded"><button class="w-full h-full"></button></li>
            <li class="w-[40px] h-[32px] bg-[#89609e] rounded"><button class="w-full h-full"></button></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "v-Boards"
}
</script>

<style scoped>

</style>