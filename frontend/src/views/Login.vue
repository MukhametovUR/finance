<template>
    <div>
       <form class="login" @submit.prevent="login">
         <h1>Sign in</h1>
         <label>Email</label>
         <input required v-model="email" type="email" placeholder="Name"/>
         <label>Password</label>
         <input required v-model="password" type="password" placeholder="Password"/>
         <hr/>
         <button type="submit">Login</button>
       </form>
 </div>
</template>


<script>
export default {
    data() {
      return {
        email: "",
        password: "",
      }
    },
		
		methods: {
			login() {
        let email = this.email 
        let password = this.password
        this.$store.dispatch('login', { email, password })
       .then(() => this.$router.push('/'))
       .catch(err => console.log(err))
      }
    }
}

</script>


<style>

=======
  <div class="main">
    <article class="container">
    <div class="block">
      <form @submit.prevent="submit">
        <div>
          <label for="username">Username:</label>
          <input type="text" name="username" v-model="form.username" />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" name="password" v-model="form.password" />
        </div>
        <button type="submit">Submit</button>
      </form>

      section

      <p v-if="showError" id="error">Username or Password is incorrect</p>
    </div>
  </article>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Login",
  components: {},
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
/*
* {
  box-sizing: border-box;
}
*/
.main {
    font-family: 'Poppins', sans-serif;
    margin: 0;

    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #03a9f4;
}

/* Контейнер */

.container {
    width: 800px;
    height: 500px;
    padding: 40px 0;
}

.block {
  height: 100%;
  background-color: rgba(255, 255, 255, 0.2);
  box-shadow: 0 5px 45px rgba(0, 0, 0, 0.2);
}
</style>