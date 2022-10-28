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

<style scoped lang="sass">
@import "@/assets/styles/styles.scss"
  </style>