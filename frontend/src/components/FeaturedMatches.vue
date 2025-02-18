<template>
  <div class="featured-matches">
    <h2>Featured Matches</h2>
    <q-carousel
      v-model="activeSlide"
      arrows
      infinite
      swipeable
      animated
      transition-prev="slide-right"
      transition-next="slide-left"
      class="carousel-container"
    >
      <q-carousel-slide
        v-for="(match, index) in matches"
        :key="index"
        :name="index"
        class="match-slide"
      >
        <div class="match-details">
          <!-- Team Logos and Names -->
          <div class="team-names">
            <div class="team">
              <img :src="match.homeTeamLogo" :alt="match.homeTeam" class="team-logo" />
              <span class="home-team">{{ match.homeTeam }}</span>
            </div>
            <span class="vs">vs</span>
            <div class="team">
              <img :src="match.awayTeamLogo" :alt="match.awayTeam" class="team-logo" />
              <span class="away-team">{{ match.awayTeam }}</span>
            </div>
          </div>

          <!-- Match Info -->
          <p class="match-info">
            🗓 {{ formatDate(match.date) }} 
          </p>
        </div>
      </q-carousel-slide>
    </q-carousel>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const activeSlide = ref(0);
const matches = ref([]);
const apiUrl = "http://127.0.0.1:5000/matches/featured";

// Fetch matches from API
const fetchMatches = async () => {
  try {
    const response = await axios.get(apiUrl);
    // Transform the backend response to match frontend expectations
    matches.value = response.data.map((match) => ({
      id: match.id,
      homeTeam: match.home_team,
      awayTeam: match.away_team,
      homeTeamLogo: match.home_team_logo,
      awayTeamLogo: match.away_team_logo,
      date: match.date,
      // venue: match.venue || "Unknown Venue", // Add venue if available
    }));
  } catch (error) {
    console.error("Error fetching matches:", error);
    matches.value = []; // Clear matches in case of error
  }
};

// Format date
const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric" });
};

onMounted(fetchMatches);
</script>

<style scoped>
/* Featured Matches Section */
.featured-matches {
  margin: 40px auto;
  text-align: center;
  width: 100%;
  max-width: 900px;
}

/* Title */
h2 {
  font-size: 2rem;
  color: white;
  margin-bottom: 20px;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: bold;
}

/* Carousel Container */
.carousel-container {
  width: 100%;
  max-width: 800px;
  height: 250px; /* Adjusted height */
  border-radius: 12px;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.3);
  overflow: hidden; /* Prevents scroll */
}

/* Match Slide */
.match-slide {
  display: flex;
  align-items: center;
  justify-content: center;
  background: black; /* Dark theme */
  color: white;
  border-radius: 8px;
  padding: 20px;
  height: 100%;
  transition: transform 0.3s ease-in-out;
}

/* Match Details */
.match-details {
  text-align: center;
}

/* Team Names */
.team-names {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  margin-bottom: 15px;
}

.team {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.team-logo {
  width: 60px;
  height: 60px;
  object-fit: contain;
  border-radius: 50%;
  background: white;
  padding: 5px;
}

.home-team,
.away-team {
  font-size: 1.4rem;
  font-weight: bold;
  color: #f8f9fa;
}

.vs {
  font-size: 1.6rem;
  font-weight: bold;
  color: #ffcc00;
}

/* Match Info */
.match-info {
  font-size: 1.1rem;
  color: #e0e0e0;
  margin-top: 10px;
  opacity: 0.9;
}
</style>