import { createRouter, createWebHistory } from 'vue-router';

// Import pages
import Home from '../pages/HomePage.vue';
import Matches from '../pages/MatchesPage.vue';
import Teams from '../pages/TeamsPage.vue';
import Players from '../pages/PlayersPage.vue';
import PlayerDetail from 'src/components/PlayerDetail.vue';
import Competitions from '../pages/CompetitionsPage.vue';
import NotFound from '../pages/NotFoundPage.vue'; // Create this page if not present

const routes = [
  { path: '/', component: Home },
  { path: '/matches', component: Matches },
  { path: '/teams', component: Teams },
  { path: '/players', component: Players },
  { path: '/competitions', component: Competitions },
  { path: '/players/:id', component: PlayerDetail },
  { path: '/:pathMatch(.*)*', component: NotFound }, // Catch-all route for 404
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
