<template>
    <q-card class="team-card q-ml-sm">
      <q-card-section class="row">
        <!-- Team Logo -->
        <q-avatar size="65px" class="team-logo">
          <img :src="team.logo" :alt="team.name" />
        </q-avatar>
  
        <!-- Team Details -->
        <div class="q-ml-md">
          <div class="team-name">{{ team.name }}</div>
          <div class="text-subtitle2 text-grey-4">{{ team.competition }}</div>
          <div class="text-caption text-grey">🏆 Founded: {{ team.founded }}</div>
          <div class="text-caption text-grey">🏟 Stadium: {{ team.stadium }}</div>
          <div class="text-caption text-grey">👔 Manager: {{ team.manager }}</div>
        </div>
      </q-card-section>
  
      <!-- Squad -->
      <q-card-section v-if="team.squad" class="squad-section">
        <div class="text-subtitle2 text-white">Key Players:</div>
        <div class="text-caption text-grey">{{ team.squad.join(", ") }}</div>
      </q-card-section>
    </q-card>
  </template>
  
  <script setup>
  defineProps({
    team: {
      type: Object,
      required: true,
    },
  });
  </script>
  
  <style scoped>
  /* Card Styling */
  .team-card {
    width: 30vw !important;
    background: #1a1a1a;
    color: white;
    border-radius: 12px;
    margin-bottom: 16px;
    padding: 12px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border: 1px solid #333;
    position: relative;
  }
  
  /* Hover Effect */
  .team-card:hover {
    transform: translateY(-5px);
    border-color: #555;
    box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.1);
  }
  
  /* Team Logo */
  .team-logo img {
    border-radius: 50%;
    border: 2px solid #555;
    transition: transform 0.3s ease;
  }
  
  .team-logo:hover img {
    transform: scale(1.1);
  }
  
  /* Text Styles */
  .team-name {
    font-size: 1.3rem;
    font-weight: bold;
    color: white;
  }
  
  .text-grey {
    color: #b0b0b0;
  }
  
  /* Squad Section */
  .squad-section {
    border-top: 1px solid #333;
    padding-top: 8px;
  }
  </style>
  