import { createWebHistory, createRouter } from 'vue-router';
import Dashboard from '../views/DashboardView.vue';
import Login from '../views/LoginView.vue';
import Items from '../views/ItemsView.vue';
import AddItem from '../views/AddItemView.vue';
import ProductOverview from '../views/ProductOverview.vue';
import LandingView from '../views/LandingView.vue';
import TestProduct from '../views/TestProduct.vue';
import TestResults from '../views/TestResults.vue';
import PricingView from '../views/PricingView.vue';
import RegisterView from '../views/RegisterView.vue';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        { path: '/', component: LandingView },
        { path: '/test', component: TestProduct},
        { path: '/pricing', component: PricingView},
        { path: '/results/:productName?', name:'results', component: TestResults},
        { path: '/login', component: Login},
        { path: '/register', component: RegisterView},
        { path: '/dashboard', component: Dashboard },
        { path: '/items', component: Items },
        { path: '/addItem', component: AddItem },
        { path: '/productOverview/:id?', name:'productView', component: ProductOverview },
    ]
})

export default router;