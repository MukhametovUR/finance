<template>
  <div id="name">
    <section class="block">
      <div class="block_content">
        <router-link class="block_content__text" to="/">Home</router-link>
        <router-link class="block_content__text" to="/api/v1/invest/">Posts</router-link>
        <span v-if="isLoggedIn">
          <a class="block_content__text" @click="logout">Logout</a>
        </span>
        <span v-else class="reg_auth">
          <router-link to="/login" class="reg_auth__item">
             <img src="../assets/icon_user.svg" alt="lock">
          </router-link>
          <router-link to="/register" class="reg_auth__item">
            <img src="../assets/lock.svg" alt="icon_user">
          </router-link>
        </span>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  computed: {
    isLoggedIn: function() { return this.$store.getters.isAuthenticated}
  },

  methods: {
    async logout() {
      await this.$store.dispatch('LogOut')
      this.$router.push('/login')
    }
  },

}
</script>

<style>
  #nav {
    padding: 30px;
  }
  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }
  a:hover {
    cursor: pointer;
  }
  #nav a.router-link-exact-active {
    color: #42b983;
  }

  .block {
    border: 1px solid;
    border-radius: 24px;
    padding: 20px 0;
    display: flex;
    margin: 0 20%;

  }

  .block_content {
    flex-grow: 1;
    display: flex;
    justify-content: space-around;
  }

  .reg_auth__item {
    padding: 0 10px;
  }

  .block_content__text {
    color: #000000;
    text-decoration: none;
    text-transform: uppercase;
  }
  </style>