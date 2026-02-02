import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import Diary from "../views/life/Diary"
import Works from "@/views/work/works";
import Login from "@/views/account/Login";
import Blog from "@/views/technology/Blog";
import UpFile from "@/views/file/UpFile";
import Skill1 from "@/views/technology/Skill1";
import Skill2 from "@/views/technology/Skill2";
import Reading from "@/views/life/Reading";
import Skill3 from "@/views/technology/Skill3";
import Skill4 from "@/views/technology/Skill4";
import Skill5 from "@/views/technology/Skill5";
import Skill6 from "@/views/technology/Skill6";
import Skill7 from "@/views/technology/Skill7";
import Skill8 from "@/views/technology/Skill8";
import Music from "@/views/video/Music";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/life/diary',
        name: 'Diary',
        component: Diary
    },
    {
        path: '/works',
        name: 'Works',
        component: Works
    },
    {
        path: '/blog',
        name: 'Blog',
        component: Blog
    },
    {
        path: '/upFile',
        name: 'UpFile',
        component: UpFile
    },
    {
        path: '/skill/vue',
        name: 'Skill1',
        component: Skill1
    },
    {
        path: '/skill/django',
        name: 'Skill2',
        component: Skill2
    },
    {
        path: '/life/reading',
        name: 'Reading',
        component: Reading
    },
    {
        path: '/skill/order',
        name: 'Skill3',
        component: Skill3
    },
    {
        path: '/skill/deploy',
        name: 'Skill4',
        component: Skill4
    },
    {
        path: '/skill/mail',
        name: 'Skill5',
        component: Skill5
    },
    {
        path: '/skill/1',
        name: 'Skill6',
        component: Skill6
    },
    {
        path: '/skill/7',
        name: 'Skill7',
        component: Skill7
    },
    {
        path: '/skill/8',
        name: 'Skill8',
        component: Skill8
    },
    {
        path: '/music',
        name: 'music',
        component: Music
    },


]

const router = new VueRouter({
    mode: 'hash',
    base: process.env.BASE_URL,
    routes
})

export default router
