<template>

  <form class="form-signin" @submit.prevent="submit">
    <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

    <div class="form-floating">
      <input type="email" class="form-control" id="email" placeholder="name@example.com" v-model="email">
      <label for="email">Email address</label>
    </div>
    <div class="form-floating">
      <input type="password" class="form-control" id="password" placeholder="Password" v-model="password">
      <label for="password">Password</label>
    </div>


    <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
  </form>

</template>

<script>
import {ref} from 'vue';
import axios from "axios";
import {useRouter} from 'vue-router';

export default{
  name:'Login',
  setup() {
    const email = ref('');
    const password = ref('');
    const router = useRouter();

    const submit = async () => {
      const response = await axios.post('login', {
        'email': email.value,
        'password':password.value
      })
      console.log(response)
      await router.push('/');
    }
    return {
      email,
      password,
      submit
    }
  }
}
</script>

<style>
html,
body {
  height: 100%;
}

body {
  justify-content: center;
  display: flex;
  align-items: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
}

.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}

.form-signin .checkbox {
  font-weight: 400;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>