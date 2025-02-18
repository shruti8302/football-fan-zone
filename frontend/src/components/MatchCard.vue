<template>
  <q-card class="match-card">
    <q-card-section class="match-content">

      <div>
        <div class="team-info">
        <q-img :src="match.home_logo" class="team-logo" />
        <span class="team-name">{{ match.home_team }}</span>
      </div>
      <div class="team-info">
        <q-img :src="match.away_logo" class="team-logo" />
        <span class="team-name">{{ match.away_team }}</span>
        
      </div>
      </div>
      
      <span class="match-time">{{ match.time }}</span>
      
    </q-card-section>
  </q-card>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
  match: Object,
});
</script>

<style scoped>
.match-card {
  background: #222;
  border-radius: 10px;
  margin-top: 10px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 30vw;
}

.match-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.team-info {
  display: flex;
  align-items: center;
}

.team-logo {
  width: 25px;
  height: 25px;
}

.team-name {
  color: white;
  padding: 5px;
}

.match-time {
  font-size: 1.2rem;
  font-weight: bold;
  color: white;
}
</style>
