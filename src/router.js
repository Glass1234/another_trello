import {createRouter, createWebHashHistory} from "vue-router";
import Authorization_main from "@/views/Authorization_main.vue";
import Main_page from "@/views/Main_page.vue";
import Boards from "@/views/Boards.vue";
import Board from "@/views/Board.vue";

export default createRouter({
    history: createWebHashHistory(),
    routes: [
        {path: '/', name: 'main_web', component: Main_page},
        {path: '/auth', name: 'auth', component: Authorization_main},
        {path: '/boards', name: 'boards', component: Boards},
        {path: '/board/:id', name: 'board', component: Board, props: true,},
    ]
})