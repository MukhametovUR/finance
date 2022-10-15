<template>
  <div class="select_reg_auth">
    <router-link to="/login" class="reg_auth__items">
      Вход
    </router-link>
    <router-link to="/register" class="reg_auth__items">
      Регистрация
    </router-link>
  </div>
</template>

<script>
export default {
  name: "Reg_Auth"
}
</script>

<style scoped>
.select_reg_auth {

}

.reg_auth__items {
  text-decoration: none;
  text-transform: uppercase;
  font-weight: bold;
  font-size: 14px;
}
</style>