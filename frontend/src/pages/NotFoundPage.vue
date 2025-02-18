<template>
    <q-page class="not-found">
      <div class="content">
        <q-icon name="warning" size="80px" color="red" />
        <h1>404 - Page Not Found</h1>
        <p>The page you are looking for doesn't exist.</p>
        <q-btn label="Go Home" to="/" color="primary" class="go-home-btn" />
      </div>
    </q-page>
  </template>
  
  <script setup></script>
  
  <style scoped>
  .not-found {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 90vh;
    text-align: center;
  }
  
  .content {
    max-width: 500px;
  }
  
  h1 {
    font-size: 2rem;
    color: #ff5252;
    line-height: 3rem;
  }
  
  p {
    font-size: 1.2rem;
    color: #333;
  }
  
  .go-home-btn {
    margin-top: 20px;
  }
  </style>
  