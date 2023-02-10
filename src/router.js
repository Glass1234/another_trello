import {createRouter, createWebHashHistory} from "vue-router";
import Authorization_main from "@/components/Authorization_main.vue";
import Main_page from "@/components/Main_page.vue";
import Boards from "@/components/Boards.vue";

-Boards
export default createRouter({
    history: createWebHashHistory(),
    routes: [
        {path: '/', name: 'main_web', component: Main_page},
        {path: '/auth', name: 'auth', component: Authorization_main},
        {path: '/boards', name: 'boards', component: Boards},
    ]
})