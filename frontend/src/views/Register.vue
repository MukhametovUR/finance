<template>
  <section>
    <div class="block">
      <div class="content">
        <Reg_Auth/>
        <form @submit="prevent.submit">
          <div>
            <label class="label_input" for="username">Username:</label>
            <text-input id="username"
                        :type="'text'"
                        :name="'username'"
                        :placeholder="'Введите логин'"
                        v-model="form.username"/>
          </div>
          <div>
            <label class="label_input" for="full_name">Full Name:</label>
            <text-input id="username"
                        :type="'text'"
                        :name="'full_name'"
                        :placeholder="'Введите логин'"
                        v-model="form.full_name"/>
          </div>
          <div>
            <label class="label_input" for="password">Password:</label>
            <text-input id="username"
                        :type="'text'"
                        :name="'full_name'"
                        :placeholder="'Введите логин'"
                        v-model="form.password"/>
          </div>
          <custom-button type="submit">Submit</custom-button>
        </form>
      </div>
    <div>

  </div>
    </div>
  </section>
</template>

<script>
import {Action, mapActions} from 'vuex'
import CustomButton from "@/components/CustomButton";
import Reg_Auth from "@/views/Reg_Auth";

export default {
  name:'Register',
  components: {
    CustomButton,
    Reg_Auth,
  },
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

<style scoped lang="sass">
@import '@/assets/styles/styles.scss'
</style>