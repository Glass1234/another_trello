<template>
  <header class="flex justify-around header_main SpaceGroteskB">
    <div class="flex">
      <div class="flex ">
        <div class="flex items-end">
          <img class="object-none"
               src="@/assets/icons/favorite_FILL0_wght400_GRAD0_opsz48.svg" alt="logo">
        </div>
        <div class="flex flex-col text-[24px] pl-[10px]">
          <h3 class="text-[#0052cc] font-semibold">ATLASSIAN</h3>
          <h1 class="text-[#253858] font-bold">Trello</h1>
        </div>
      </div>
      <div class="flex font-bold RobotoL">
        <button class=" px-[16px] hover:text-[#034efc]">
          <span>Features</span>
        </button>
        <button class="px-[16px] hover:text-[#034efc]"><span>Solutions</span></button>
        <button class="px-[16px] hover:text-[#034efc]"><span>Plans</span></button>
        <button class="px-[16px] hover:text-[#034efc]"><span>Pricing</span></button>
        <button class="px-[16px] hover:text-[#034efc]"><span>Resources</span></button>
      </div>
    </div>
    <div class="flex">
      <router-link class="px-[24px] flex items-center duration-300 bg-[#1ac320] hover:bg-[#308b2b] no-underline"
                   to="boards"><span class="text-white">Go app</span></router-link>
      <router-link class="px-[24px] flex items-center no-underline"
                   to="auth"><span>Log in</span></router-link>
      <router-link
          class="px-[24px] text-white ease-in duration-300 bg-[#0066ff] hover:bg-[#003f9e] flex items-center no-underline"
          to="auth"><span>Get Trello for free</span>
      </router-link>
    </div>
  </header>
</template>

<script>
export default {
  name: "Header_",
  data() {
    return {}
  }
}
</script>

<style scoped>
.RobotoL {
  font-family: 'Roboto-Light', sans-serif;
}

.SpaceGroteskB {
  font-family: 'SpaceGrotesk-Bold', sans-serif;
}
</style>