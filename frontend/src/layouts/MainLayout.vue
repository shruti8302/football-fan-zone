<template>
  <q-layout view="hHh lpR fFf">
    <q-header class="main-container" elevated>
      <q-toolbar>
        <!-- Football Icon -->
        <q-icon name="sports_soccer" size="25px" />
        
        <!-- Title -->
        <q-toolbar-title class="heading">Football Fan Zone</q-toolbar-title>
        
        <!-- Navigation Buttons -->
        <q-btn flat label="Home" to="/" />
        <q-btn flat label="Matches" to="/matches" />
        <q-btn flat label="Teams" to="/teams" />
        <q-btn flat label="Players" to="/players" />
        <q-btn flat label="Competitions" to="/competitions" />
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<style lang="scss">
.main-container {
  background: black !important;

  .heading {
    font-size: 16px !important;
    padding-left: 6px !important;
  }
}
</style>
