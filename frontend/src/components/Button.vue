<template>
  <button :style="{ background: color }" @click="onClick()" class="btn">
    {{ text }}
  </button>
</template>

<script>
export default {
  name: "Button",
  props: {
    text: String,
    color: String,
  },
  methods: {
    onClick: () => {
      console.log("Button Clicked");
    },
  },
};
</script>

<style scoped>
button {
  color: white;
  border: none;
  outline: none;
  margin-top: 8px;
  margin-bottom: 15px;
  border-radius: 3px;
  padding: 12px 24px;
  cursor: pointer;
}
</style>