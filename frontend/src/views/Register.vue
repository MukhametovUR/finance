<template>
  <div class="register">
    <div>
      <form @submit="prevent.submit">
        <div>
          <label for="username">Username:</label>
          <input type="text" name="username" v-model="form.username">
        </div>
        <div>
          <label for="full_name">Full Name:</label>
          <input type="text" name="full_name" v-model="form.full_name">
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="text" name="password" v-model="form.password">
        </div>
        <custom-button type="submit">Submit</custom-button>
      </form>
    </div>
  </div>
</template>

<script>
import {Action, mapActions} from 'vuex'
import CustomButton from "@/components/CustomButton";
export default {
  name:'Register',
  components: {CustomButton},
  data() {
    return {
      form: {
        username: '',
        full_name: '',
        password: '',
      },
      showError: false
    }
  },

  methods: {
    ...mapActions(['Register']),
    async submit() {
      try {
        await this.Register(this.form)
        this.$store.push('/api/v1/invest/')
      }catch(error) {
        this.showError = true
      }
    }
  }
}
</script>

<style scoped>
  * {
    box-sizing: border-box;
  }
  label {
    padding: 12px 12px 12px 0;
    display: inline-block;
  }

  input {
    margin: 5px;
    box-shadow:0 0 15px 4px rgba(0,0,0,0.06);
    padding:10px;
    border-radius:30px;
  }
  #error {
    color: red;
  }
  </style>