<template>
  <section class="login">
    <div class="block">

      <div class="content">
      <Reg_Auth/>

      <form @submit.prevent="submit">
        <div>
          <label class="label_input"
                 for="username">Username:</label>
          <text-input id="username"
                      :type="'text'"
                      :name="'username'"
                      :placeholder="'Введите логин'"
                      v-model="form.username"/>
        </div>
        <div>
          <label class="label_input" for="password">Password:</label>
          <text-input id="password"
                      :type="'password'"
                      :name="'password'"
                      :placeholder="'Введите пароль'"
                      v-model="form.password"/>
        </div>
        <custom-button type="submit">войти</custom-button>
      </form>
      </div>
      <p v-if="showError" id="error">Логин или пароль некорректны</p>
    </div>
  </section>
</template>

<script>
import { mapActions } from "vuex";
import Posts from "@/views/Posts copy";
import Reg_Auth from "@/views/Reg_Auth";
import CustomButton from "@/components/CustomButton";

export default {
  name: "Login",
  components: {
    CustomButton,
    Posts,
    Reg_Auth,
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

#error {
  color: red;
}

.block {
  border: 1px solid;
  display: flex;
  flex-direction: column;
}
</style>