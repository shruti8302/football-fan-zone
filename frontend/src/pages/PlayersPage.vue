<template>
  <q-page class="q-pa-md players">
    <h1 class="page-heading">🏃 Players</h1>

    <!-- Search & Filters -->
    <div class="flex filter-card">
      <q-input
        v-model="searchQuery"
        label="Search Player"
        outlined
        dense
        class="filter-class"
        dark
        @update:model-value="fetchPlayers"
      />
      <q-select
        v-model="selectedTeam"
        :options="teamOptions"
        label="Filter by Team"
        outlined
        dense
        class="filter-class"
        dark
        @update:model-value="fetchPlayers"
      />
      <q-select
        v-model="selectedPosition"
        :options="positionOptions"
        label="Filter by Position"
        outlined
        dense
        class="filter-class"
        dark
        @update:model-value="fetchPlayers"
      />
    </div>

    <!-- Players List -->
    <q-list class="row q-col-gutter-md player-info-card">
      <q-card
        v-for="player in players"
        :key="player.id"
        class="player-card col-12 col-sm-6 col-md-4 col-lg-3"
        clickable
        @click="goToPlayer(player.id)"
      >
        <q-img :src="player.image" class="player-image" />
        <q-card-section class="text-center">
          <q-item-label class="text-bold text-h6 text-white">{{ player.name }}</q-item-label>
          <q-item-label caption class="text-grey-5">
            {{ player.position }} - {{ player.team }}
          </q-item-label>
        </q-card-section>
      </q-card>
    </q-list>
  </q-page>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const players = ref([]);
const searchQuery = ref("");
const selectedTeam = ref("All"); // Default to "All"
const selectedPosition = ref("All"); // Default to "All"

// Add "All" option to team and position filters
const teamOptions = ref(["All", "Inter Miami", "Al Nassr", "Al Hilal", "Barcelona"]);
const positionOptions = ref(["All", "Forward", "Midfielder", "Defender", "Goalkeeper"]);

// Fetch players from the backend
const fetchPlayers = async () => {
  try {
    const params = new URLSearchParams();
    if (searchQuery.value) params.append("search", searchQuery.value);

    // Only append team filter if "All" is not selected
    if (selectedTeam.value && selectedTeam.value !== "All") {
      params.append("team", selectedTeam.value);
    }

    // Only append position filter if "All" is not selected
    if (selectedPosition.value && selectedPosition.value !== "All") {
      params.append("position", selectedPosition.value);
    }

    const response = await fetch(`http://127.0.0.1:5000/players/?${params.toString()}`);
    if (!response.ok) throw new Error("Failed to fetch players");
    players.value = await response.json();
  } catch (error) {
    console.error("Error fetching players:", error);
  }
};

// Fetch players when the component is mounted
onMounted(fetchPlayers);

// Watch for changes in searchQuery, selectedTeam, or selectedPosition
watch([searchQuery, selectedTeam, selectedPosition], () => {
  fetchPlayers();
});

// Navigate to player details page
const goToPlayer = (playerId) => {
  router.push(`/players/${playerId}`);
};
</script>

<style scoped>
/* Apply Full Black Theme */
.players {
  background: #121212;
}

/* Keep all other styles unchanged */
.player-info-card {
  margin-top: 20px !important;
  margin-left: 5px !important;
}

.page-heading {
  color: white;
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 30px;
}

.filter-card {
  border-radius: 8px;
  padding-left: 10px;
}

.filter-class {
  width: 30vw;
  margin-right: 15px;
  background: #242424;
  color: white;
  border-radius: 8px;
}

.player-card {
  transition: transform 0.2s, box-shadow 0.2s;
  cursor: pointer;
  border-radius: 12px;
  overflow: hidden;
  width: 30vw;
  padding: 15px;
  padding-bottom: 0px;
  margin: 7.5px;
  background: #242424;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.player-card:hover {
  transform: scale(1.05);
  box-shadow: 0px 4px 12px rgba(255, 255, 255, 0.15);
}

.player-image {
  height: 180px;
  object-fit: cover;
}

h1 {
  line-height: 1rem;
}
</style>