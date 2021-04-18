<template>
  <div id="app">
    <div class="container">
      <router-view/>
    </div>
  </div>
</template>

<style lang="scss">
  @import '~materialize-css/sass/materialize.scss';

  .container {
    display: flex;
    align-content: center;
  }
</style>