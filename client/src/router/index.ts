import { createWebHistory, createRouter, NavigationGuardNext, RouteLocationNormalized } from "vue-router";
import Dashboard from "../views/DashboardView.vue";
import Login from "../views/LoginView.vue";
import Items from "../views/ItemsView.vue";
import AddItem from "../views/AddItemView.vue";
import ProductOverview from "../views/ProductOverview.vue";
import LandingView from "../views/LandingView.vue";
import TestProduct from "../views/TestProduct.vue";
import TestResults from "../views/TestResults.vue";
import PricingView from "../views/PricingView.vue";
import RegisterView from "../views/RegisterView.vue";
import storageService from "../services/storage-service";

export const authGuard = async function (
    to: RouteLocationNormalized,
    from: RouteLocationNormalized,
    next: NavigationGuardNext
  ) {
    try {
      if (storageService.retrieveAccessToken() == null || storageService.retrieveAccessToken() == "") {
        next({ name: "auth" });
        return;
      }
    } catch (e) {
      console.log(e);
    }
  
    next();
  };

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: "/", component: LandingView },
    { path: "/test", component: TestProduct },
    { path: "/pricing", component: PricingView },
    { path: "/results/:productName?", name: "results", component: TestResults, beforeEnter: authGuard },
    { path: "/login", name: "auth", component: Login },
    { path: "/register", component: RegisterView },
    { path: "/dashboard", component: Dashboard, beforeEnter: authGuard},
    { path: "/items", component: Items, beforeEnter: authGuard},
    { path: "/addItem", component: AddItem, beforeEnter: authGuard},
    {
      path: "/productOverview/:id?",
      name: "productView",
      component: ProductOverview,
      beforeEnter: authGuard,
    },
  ],
});

export default router;
