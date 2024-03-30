import { createWebHistory, createRouter } from 'vue-router';
import Dashboard from '../views/DashboardView.vue';
import Login from '../views/LoginView.vue';
import Items from '../views/ItemsView.vue';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        { path: '/', component: Login },
        { path: '/dashboard', component: Dashboard },
        { path: '/items', component: Items },
    ]
})

export default router;