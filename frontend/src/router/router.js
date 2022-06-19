import { createRouter, createWebHistory } from 'vue-router'
import MainPage from "@/views/MainPage";
import SnippetPage from "@/views/SnippetPage";
import PhotosPage from "@/views/PhotosPage";
import NotFound from "@/views/NotFound";
import Photo from "@/components/photo/Photo";
import LoginPage from "@/views/LoginPage";
import ProfileListPage from "@/views/ProfileListPage";
import RegistrationPage from "@/views/RegistrationPage";


const routes = [

  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/',
    name: 'main',
    component: MainPage
  },
  {
    path: '/snippet',
    name: 'snippet',
    component: SnippetPage
  },
  {
    path: '/photos',
    name: 'photos',
    component: PhotosPage
  },
  {
    path: '/photos/:id',
    name: 'photo',
    component: Photo,
    props: true
  },

  //  catchall 404
  {
    path: '/:catchall(.*)',
    name: 'NotFound',
    component: NotFound
  },
  {
    path: '/register',
    name: 'register',
    component: RegistrationPage
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileListPage
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
