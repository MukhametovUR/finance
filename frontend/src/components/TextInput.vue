<template>
  <input  class="input_text"
          type="type"
          name="name"
          :value="modelValue"
          @input="$emit('update:modelValue', $event.target.value)"
          :placeholder="placeholder">
</template>

<script>
export default {
  name: 'TextInput',
  emits: ['update:modelValue'],
  props: {
    'modelValue': {
      type: [String, Number]
    },
    'placeholder': String,
    'type': {
      type: String,
      default: ''
    },
  }
}
</script>

<style scoped lang="sass">
@import "@/assets/styles/styles.scss"
</style>