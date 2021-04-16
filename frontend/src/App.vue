<template>
  <div class="App">
    <Auth />
  </div>
</template>

<script>
import Auth from "./components/Auth";
export default {
  name: "App",
  components: {
    Auth
  },
  data() {
    return {
      isLoggedIn: false,
    }
  }
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.App {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
