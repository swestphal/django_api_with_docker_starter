<template>


  <form class="form-signin" @submit.prevent="submit" >
    <h1 class="h3 mb-3 fw-normal">Please register</h1>

    <div class="form-floating">
      <input type="text" class="form-control" id="first_name" placeholder="Bob" v-model="firstName">
      <label for="first_name">First Name</label>
    </div>
    <div class="form-floating">
      <input type="text" class="form-control" id="last_name" placeholder="Bob" v-model="lastName">
      <label for="last_name">Last Name</label>
    </div>
     <div class="form-floating">
      <input type="email" class="form-control" id="email" placeholder="name@example.com" v-model="email">
      <label for="email">Email address</label>
    </div>
    <div class="form-floating">
      <input type="password" class="form-control" id="password" placeholder="Password" v-model="password">
      <label for="password">Password</label>
    </div>
    <div class="form-floating">
      <input type="password" class="form-control" id="password_confirm" placeholder="Password" v-model="passwordConfirm">
      <label for="password_confirm">Password confirmation</label>
    </div>

    <button class="w-100 btn btn-lg btn-primary" type="submit">Register</button>

  </form>


</template>

<script>
import {ref} from 'vue';
import axios from 'axios';
import {useRouter} from 'vue-router';
export default {
  name:"Register",
  setup() {
    const firstName = ref('');
    const lastName = ref('');
    const email = ref('');
    const password = ref('');
    const passwordConfirm = ref('');
    const router = useRouter();
    const submit = async () => {
      const response = await axios.post('register', {
        "first_name":firstName.value,
        "last_name":lastName.value,
        "email":email.value,
        "password":password.value,
        "password_confirm":passwordConfirm.value,
        "role":3
      })
      console.log(response)
      await router.push('/login')
    }
    return {
      firstName,
      lastName,
      email,
      password,
      passwordConfirm,
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