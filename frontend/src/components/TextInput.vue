<template>
  <input :type="type"
         :name="name"
         :value="modelValue"
         @input="$emit('update:modelValue', $event.target.value)"
  />
</template>

<script>
export default {
  name: "TextInput",
  props: {
    'modelValue': {
      type: [String, Number]
    },
    type: String,
    name: String,
    tag_id: {
      type: String,
      default: ''
    }
  }
}
</script>

<style scoped>
input {
  margin: 5px;
  padding: 10px;
  border-radius: 4px;
  background-color: #F8F1FF;
  border: 1px solid rgba(0, 0, 0, 0.25);
}
input:focus {
  outline:none;
  -webkit-box-shadow: 1px 11px 8px 0px rgba(34, 60, 80, 0.2);
  -moz-box-shadow: 1px 11px 8px 0px rgba(34, 60, 80, 0.2);
  box-shadow: 1px 11px 8px 0px rgba(34, 60, 80, 0.2);
   border: 1px solid rgba(0, 0, 0, 0.25);
}
</style>