<template>
  <section class="login">
    <div class="block">

      <Reg_Auth/>

      <form @submit.prevent="submit">
        <div>
          <label for="username">Username:</label>
          <TextInput
              :type="text"
              :name="username"
              v-model="form.username"/>
        </div>
        <div>
          <label for="password">Password:</label>
          <TextInput
              :type="password"
              :name="password"
              v-model="form.password"/>
        </div>
        <button type="submit">Submit</button>
      </form>
      <p v-if="showError" id="error">Username or Password is incorrect</p>
    </div>
  </section>
</template>

<script>
import { mapActions } from "vuex";
import Posts from "@/views/Posts copy";
import Reg_Auth from "@/views/Reg_Auth";
import TextInput from "@/components/TextInput"
import CustomLabel from "@/components/CustomLabel"

export default {
  name: "Login",
  components: {
    Posts,
    Reg_Auth,
    TextInput,
    CustomLabel,
  },
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
      showError: false
    };
  },
  methods: {
    ...mapActions(["LogIn"]),
    async submit() {
      const User = new FormData();
      User.append("username", this.form.username);
      User.append("password", this.form.password);
      try {
          await this.LogIn(User);
          this.$router.push("/api/v1/invest/");
          this.showError = false
      } catch (error) {
        this.showError = true
      }
    },
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}

label {
  padding: 12px 12px 12px 0;
  display: inline-block;
}

button[type="submit"] {
  background-color: #4caf50;
  color: white;
  padding: 12px 20px;
  cursor: pointer;
  border-radius: 30px;
}

button[type="submit"]:hover {
  background-color: #45a049;
}

#error {
  color: red;
}

.block {
  border: 1px solid;
  display: flex;
  flex-direction: column;
}
</style>