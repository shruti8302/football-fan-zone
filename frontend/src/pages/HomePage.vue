<template>
  <q-page class="home-page">
    <!-- Animated Rotating Background -->
    <div class="animated-background"></div>

    <!-- Content -->
    <div class="content">
      <!-- Welcome Text with Icon -->
      <h1 class="welcome-text">
        <q-icon name="sports_soccer" size="40px" class="icon football" /> Welcome to
        <span>Football Fan Zone</span>
      </h1>
      <p class="subtitle typing-text">
        Your ultimate destination for football matches, teams, and competitions
      </p>

      <!-- Icons Row -->
      <div class="icons-row">
        <q-icon name="emoji_events" size="50px" class="icon trophy" />
        <q-icon name="sports_soccer" size="50px" class="icon ball" />
      </div>

      <!-- Featured Matches -->
      <FeaturedMatches />

      <footer class="footer">
  © 2025 Shruti | All rights reserved.
</footer>
    </div>
  </q-page>
</template>

<script setup>
import FeaturedMatches from "../components/FeaturedMatches.vue";
</script>

<style scoped>
/* Background */

.footer {
    margin-top: 20px;
    padding: 10px;
    text-align: center;
    font-size: 14px;
    /* background: #222; */
    color: white;
  }

.football {
    display: inline-block;
    animation: bounce 1s ease-in-out infinite;
  }

  @keyframes bounce {
    0%, 100% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-10px);
    }
  }
.home-page {
  position: relative;
  overflow: hidden;
  background-color: #228b22; /* Ground green */
  color: white;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Rotating Background Animation */
.animated-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: radial-gradient(circle, #3aaf3a 20%, #228b22 80%);
  background-size: 200% 200%;
  z-index: -1;
  animation: rotateBackground 10s infinite linear;
}

@keyframes rotateBackground {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/* Centered Content */
.content {
  text-align: center;
  width: 90%;
  max-width: 800px;
  z-index: 1;
  animation: fadeIn 1.5s ease-in-out;
}

/* Welcome Text */
.welcome-text {
  font-size: 3rem;
  font-weight: bold;
  color: white;
  margin-bottom: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  animation: textPop 1.5s ease-in-out;
}

.welcome-text span {
  color: black;
}

.icon {
  color: #ffd700; /* Gold color */
}

/* Subtitle */
.subtitle {
  font-size: 1.5rem;
  color: #d3d3d3;
  font-weight: bold;
  margin-bottom: 20px;
}

/* Animated Typing Text */
.typing-text {
  display: inline-block;
  white-space: nowrap;
  overflow: hidden;
  width: 0;
  font-size: 1.5rem;
  color: #d3d3d3;
  border-right: 3px solid white;
  animation: typing 4s steps(40, end) forwards, blink 0.7s infinite;
}

@keyframes typing {
  from {
    width: 0;
  }
  to {
    width: 100%;
  }
}

@keyframes blink {
  50% {
    border-color: transparent;
  }
}

/* Icons Row */
.icons-row {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-bottom: 30px;
  animation: slideUp 1.5s ease-in-out;
}

.icon.trophy {
  color: gold;
}

.icon.ball {
  color: white;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
