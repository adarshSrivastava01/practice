<template>
  <div class="container">
    <h1>The Book Store</h1>
    <form>
      <div class="form-control">
        <label>Name</label>
        <input
          type="text"
          name="name"
          placeholder="Enter Name"
          v-model="name"
        />
      </div>
      <div class="form-control">
        <label>Email</label>
        <input
          type="email"
          name="email"
          placeholder="Enter Email"
          v-model="email"
        />
      </div>
      <div class="form-control">
        <label>Password</label>
        <input
          type="password"
          name="password"
          placeholder="Enter Password"
          v-model="password"
        />
      </div>
    </form>
    <div class="button-box">
      <Button text="Hello" color="green" />
      <Button text="Hello" color="green" />
    </div>
  </div>
</template>

<script>
import Button from "./Button";
export default {
  name: "Auth",
  components: {
    Button,
  },
  data() {
    return {
      email: "",
      password: "",
      name: "",
      isLoggedIn: false,
    };
  },
};
</script>

<style scoped>
.container {
  height: 75vh;
  width: 30vw;
  border: 3px solid black;
  padding: 30px;
}
.container h1 {
  text-align: center;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  margin-bottom: 25px;
}
.form-control {
  width: 100%;
  display: flex;
  flex-direction: column;
}
.form-control label {
  font-size: 24px;
  margin-bottom: 12px;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}
.form-control input {
  width: 400px;
  padding: 12px 6px;
  margin-bottom: 15px;
}
.button-box {
    display: flex;
    flex-direction: column;
}
</style>