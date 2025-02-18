<template>
  <q-page class="matches-page q-pa-md">
    <h2 class="matches-title">🎌 Matches</h2>

    <!-- Filters Section -->
    <div class="filter-card">
      <q-input
        v-model="selectedDate"
        type="date"
        label="Select Date"
        filled
        dense
        class="filter-class"
        dark
        @update:model-value="filterMatches"
      />
      <q-select
        v-model="selectedArea"
        :options="areaOptions"
        label="Select Area"
        filled
        dense
        class="filter-class"
        dark
        emit-value
        map-options
        @update:model-value="filterMatches"
      />
    </div>

    <!-- Matches Section -->
    <div class="matches-section">
      <span class="matches-date">{{ formattedSelectedDate }}</span>

      <div v-if="filteredCompetitions.length">
        <div v-for="competition in filteredCompetitions" :key="competition.id" class="competition-group">
          <div class="competition-header">
            <q-img :src="competition.logo" class="competition-logo" />
            <div>
              <h3 class="competition-name">{{ competition.name }}</h3>
              <p class="matchday">Matchday {{ competition.matchday }}</p>
            </div>
          </div>

          <div class="match-list">
            <MatchCard v-for="match in competition.matches" :key="match.id" :match="match" />
          </div>
        </div>
      </div>

      <div v-else class="no-matches">No matches found for the selected filters.</div>
    </div>
  </q-page>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import MatchCard from "../components/MatchCard.vue";

// Filters
const selectedDate = ref(new Date().toISOString().split("T")[0]); // Default to today's date
const selectedArea = ref(null);
const filteredCompetitions = ref([]);

const areaOptions = ref([
  { label: "All", value: null },
  { label: "England", value: "England" },
  { label: "Spain", value: "Spain" },
  { label: "France", value: "France" },
  { label: "Germany", value: "Germany" },
  { label: "Italy", value: "Italy" },
]);

// Format selected date for display
const formattedSelectedDate = computed(() => {
  return new Date(selectedDate.value).toLocaleDateString("en-US", {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
  });
});

// Fetch matches from the backend
const fetchMatches = async () => {
  try {
    const params = new URLSearchParams();
    if (selectedDate.value) params.append("date", selectedDate.value);
    if (selectedArea.value) params.append("area", selectedArea.value);

    const response = await fetch(`http://127.0.0.1:5000/matches?${params.toString()}`);
    if (!response.ok) throw new Error("Failed to fetch matches");
    const data = await response.json();

    // Group matches by competition
    const groupedMatches = data.reduce((acc, match) => {
      const competitionName = match.competition; // Use the competition field from the API
      const competitionLogo = match.competition_logo; // Use the competition_logo field from the API
      if (!acc[competitionName]) {
        acc[competitionName] = {
          id: match.id, // Use a unique identifier for the competition
          name: competitionName,
          logo: competitionLogo || "", // Add competition logo if available
          time: match.time,
          area: match.area || "Unknown", // Use the area field from the API
          matches: [],
        };
      }
      acc[competitionName].matches.push(match);
      return acc;
    }, {});

    // Convert grouped matches to an array
    filteredCompetitions.value = Object.values(groupedMatches);
  } catch (error) {
    console.error("Error fetching matches:", error);
  }
};

// Apply filters
const filterMatches = () => {
  fetchMatches();
};

// Load initial matches
onMounted(() => {
  filterMatches();
});
</script>

<style scoped>
.matches-page {
  background: #121212;
  color: white;
}

/* Calendar Header */
.calendar-header {
  font-size: 1rem;
  font-weight: bold;
  margin-bottom: 15px;
  text-align: center;
}

/* Filters */
.filter-card {
  border-radius: 8px;
  padding-left: 10px;
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
}

.filter-class {
  width: 30vw;
  margin-right: 15px;
  background: #242424;
  color: white;
  border-radius: 8px;
}

/* Matches Section */
.matches-section {
  margin-top: 20px;
}

.matches-title {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 40px;
}

.matches-date {
  color: lightgray;
  padding-left: 10px;
}

/* Competitions */
.competition-group {
  padding-left: 10px;
}

.competition-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  border-bottom: 1px solid gray;
}

.competition-logo {
  width: 60px;
  height: 60px;
}

.competition-name {
  font-size: 1.2rem;
}

.matchday {
  color: lightgray;
}

.match-list {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  margin: 10px 0;
}

.no-matches {
  text-align: center;
  font-size: 1rem;
  color: lightgray;
  margin-top: 20px;
}

h2 {
  line-height: 0;
}

h3 {
  line-height: 0;
}
</style>