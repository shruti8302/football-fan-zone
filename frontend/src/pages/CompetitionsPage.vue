<template>
  <q-page class="q-pa-md dark-theme">
    <h2 class="page-title">🏆 Football Competitions</h2>

    <div class="q-pl-sm">
      <q-input
        class="competition-card"
        outlined
        v-model="searchQuery"
        placeholder="🔍 Search competitions..."
        dense
        dark
        @input="debouncedFetchCompetitions"
      />

      <q-list class="competition-list">
        <q-card
          v-for="competition in competitions"
          :key="competition.id"
          class="competition-item"
        >
          <q-card-section class="row items-center">
            <q-avatar size="50px">
              <img :src="competition.logo" alt="Competition Logo" />
            </q-avatar>
            <div class="q-ml-md">
              <div class="text-h6">{{ competition.name }}</div>
              <div class="text-subtitle2 text-grey-5">
                {{ competition.country }} | Season: {{ competition.season }}
              </div>
            </div>
          </q-card-section>
        </q-card>
      </q-list>

      <div v-if="competitions.length === 0" class="text-center text-grey-5 q-mt-md">
        No competitions found.
      </div>

       <!-- Error Message -->
       <div v-if="error" class="text-center text-red q-mt-md">
        Error fetching competitions. Please try again later.
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import axios from "axios";

const searchQuery = ref("");
const competitions = ref([]);
const error = ref(null);

const fetchCompetitions = async () => {
  console.log("Search Query:", searchQuery.value); // Debugging
  try {
    const response = await axios.get("http://127.0.0.1:5000/competitions/", {
      params: { search: searchQuery.value },
    });
    
    competitions.value = response.data;
    error.value = null; // Clear any previous errors
  } catch (err) {
    console.error("Error fetching competitions:", err);
    error.value = "Failed to fetch competitions. Please try again later.";
    competitions.value = []; // Clear competitions in case of error
  }
};

// Watch for changes to searchQuery and debounce the fetchCompetitions call
let timeoutId;
watch(searchQuery, () => {
  if (timeoutId) {
    clearTimeout(timeoutId);
  }
  timeoutId = setTimeout(() => {
    fetchCompetitions();
  }, 300); // 300ms debounce delay
});

onMounted(fetchCompetitions);
</script>
<style scoped>
/* Dark Theme */
.dark-theme {
  background-color: #121212;
  color: white;
  min-height: 100vh;
}

h2{
  line-height: 0px;
  padding-bottom: 25px;
}

.page-title {
  font-size: 1.8rem;
  font-weight: bold;
  /* text-align: center; */
  margin-bottom: 20px;
  color: #f5f5f5;
}

.competition-card {
  margin-bottom: 20px;
  width: 95vw;
}

.competition-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 15px;
}

.competition-item {
  width: 30vw;
  padding: 10px;
  border-radius: 8px;
  background-color: #242424;
  color: white;
  transition: transform 0.2s, box-shadow 0.2s;
}

.competition-item:hover {
  transform: scale(1.02);
  box-shadow: 0px 4px 8px rgba(255, 255, 255, 0.2);
}

.q-avatar img {
  border-radius: 50%;
}

.q-input {
  background: #1e1e1e;
  color: white;
  margin-bottom: 30px !important;
}
</style>
