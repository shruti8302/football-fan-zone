<template>
  <q-page class="q-pa-md teams">
    <h2 class="text-h4 text-weight-bold q-mb-md title">

🤝 Teams</h2>

    <!-- Team List -->
    <div class="row q-col-gutter-md">
      <div
        v-for="team in teams"
        :key="team.id"
      
      >
        <TeamCard :team="team" />
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import TeamCard from "../components/TeamCard.vue";

const teams = ref([]);

const fetchTeams = async (searchQuery = '') => {
  try {
    // Fetch teams from the backend
    const response = await fetch(`http://127.0.0.1:5000//teams?search=${searchQuery}`);
    const data = await response.json();
    teams.value = data;
  } catch (error) {
    console.error("Error fetching teams:", error);
  }
};

// Fetch teams when the component is mounted
onMounted(() => {
  fetchTeams();
});

</script>

<style scoped>
.teams {
  background-color: #121212;
  color: white;
  min-height: 100vh;
}

h2{
  line-height: 0px;
}

.title {
  color: white;
  margin-bottom: 40px !important;
  /* text-align: center; */
}
</style>
