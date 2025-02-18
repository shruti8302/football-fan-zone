<template>
  <q-page class="q-pa-md player">
    <!-- Back Button -->
    <q-btn flat icon="arrow_back" label="Back" @click="router.back()" class="q-mb-sm back-btn" />

    <!-- Player Card -->
    <q-card v-if="player" class="player-card">
      <!-- Player Info -->
      <q-card-section class="row items-center">
        <q-avatar size="70px">
          <img :src="player.image" alt="Player Image" />
        </q-avatar>
        <div class="q-ml-md">
          <div class="text-h5 text-weight-bold">{{ player.name }}</div>
          <div class="text-subtitle2 text-grey-7">{{ player.team }} - {{ player.position }}</div>
        </div>
      </q-card-section>

      <q-separator />

      <!-- Statistics and Upcoming Matches -->
      <div class="row q-pa-md q-gutter-md flex">
        <!-- Statistics -->
        <q-card-section class="col-12 col-md-6 statistics">
          <h3 class="section-title">📊 Statistics</h3>
          <q-list bordered separator>
            <q-item v-for="(value, key) in player.stats" :key="key">
              <q-item-section>{{ formatStatName(key) }}</q-item-section>
              <q-item-section side class="text-grey">{{ value }}</q-item-section>
            </q-item>
          </q-list>
        </q-card-section>

        <!-- Upcoming Matches -->
        <q-card-section class="col-12 col-md-6 upcoming-matches">
          <h3 class="section-title">📅 Upcoming Matches</h3>
          <q-list separator v-if="player.upcoming_matches.length">
            <q-item v-for="match in player.upcoming_matches" :key="match.id" class="match-card">
              <q-item-section>
                <div class="match-content">
                  <div class="team-names">
                    ⚽ <span class="home-team">{{ match.home_team }}</span>
                    <strong>vs</strong>
                    <span class="away-team">{{ match.away_team }}</span>
                  </div>
                  <div class="match-date">
                    🗓 {{ formatDate(match.date) }}
                  </div>
                </div>
              </q-item-section>
            </q-item>
          </q-list>
          <div v-else class="text-grey-7 text-center q-pa-md">
            No upcoming matches scheduled.
          </div>
        </q-card-section>
      </div>
    </q-card>

    <!-- Loading State -->
    <q-card v-else class="loading-card">
      <q-card-section>
        <q-spinner color="primary" size="40px" />
        <p>Loading Player Data...</p>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();
const player = ref(null);

// Fetch player details from the backend
const fetchPlayerDetails = async () => {
  try {
    const response = await fetch(`http://127.0.0.1:5000/players/${route.params.id}`);
    if (!response.ok) throw new Error("Failed to fetch player details");
    player.value = await response.json();
  } catch (error) {
    console.error("Error fetching player details:", error);
  }
};

// Fetch player details when the component is mounted
onMounted(fetchPlayerDetails);

// Format statistic names for display
const formatStatName = (key) => {
  const statNames = {
    matches: "Matches Played",
    goals: "Goals Scored",
    assists: "Assists",
    yellow_cards: "Yellow Cards",
    red_cards: "Red Cards",
  };
  return statNames[key] || key;
};

// Format date for display
const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric" });
};
</script>

<style scoped>
.player {
  background-color: #1a1919; /* Dark background for the entire page */
  color: white; /* Light text for dark theme */
}

.back-btn {
  color: white; /* Light text for dark theme */
}

.player-card {
  margin-left: 20px;
  margin-right: 15px;
  border-radius: 12px;
  background: #181818; /* Dark background for the card */
  color: white; /* Light text */
}

.q-avatar img {
  border-radius: 50%;
  border: 3px solid #292828; 
}

.section-title {
  font-size: 1.2rem;
  font-weight: bold;
  line-height: 0;
  padding-bottom: 10px;
  color: #e6ebed; 
}

.match-info {
  font-size: 1rem;
  font-weight: bold;
}

.loading-card {
  text-align: center;
  padding: 30px;
  background: #1e1e1e; /* Dark background for loading card */
  color: white; /* Light text */
}

.upcoming-matches,
.statistics {
  padding: 20px;
  border-radius: 8px;
  background: #2c2c2c; /* Dark background for sections */
  width: 47%;
  color: rgb(220, 216, 216); /* Light text */
}

.upcoming-matches .q-list,
.statistics .q-list {
  border-radius: 8px;
}

.text-grey-7 {
  color: #9e9e9e; /* Muted text color for dark theme */
}

.upcoming-matches {
  margin-top: 20px;
  padding: 15px;
  border-radius: 10px;
  background: #2c2c2c; /* Dark background for upcoming matches */
}

.match-card {
  background: #333333; /* Dark background for match cards */
  border-radius: 8px;
  padding: 14px;
  margin: 14px 0;
  color: white; /* Light text */
}

.match-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.team-names {
  font-size: 1rem;
  font-weight: bold;
}

.home-team {
  color: rgb(214, 209, 209); /* Light text for dark theme */
  padding-right: 5px;
}

.away-team {
  padding-left: 5px;
  color: rgb(214, 209, 209); /* Light text for dark theme */
}

.match-date {
  font-size: 0.9rem;
  font-weight: bold;
  color: #ffffff; /* Light text for dark theme */
  background: #444444; /* Dark background for date */
  padding: 4px 8px;
  border-radius: 5px;
}
</style>