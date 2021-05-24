<template>
  <form @submit.prevent="submit">
    <div class="form-group">
      <label for="first_name">First Name</label>
      <input type="text" class="form-control" name="first_name" id="first_name" placeholder="Bob" v-model="firstName">
    </div>
    <div class="form-group">
      <label for="last_name">Last Name</label>
      <input type="text" class="form-control" name="last_name" id="last_name" placeholder="Bob" v-model="lastName">
    </div>
     <div class="form-group">
       <label for="email">Email address</label>
       <input type="email" class="form-control" name="email" id="email" placeholder="name@example.com" v-model="email">
    </div>
    <div class="form-group">
       <label for="email">Role</label>
       <select name="role_id" id="role" placeholder="" v-model="roleId">
         <option value="0">Select Role</option>
         <option v-for="role in roles" :key="role.id" :value="role.id">{{role.name}}</option>
       </select>
    </div>
    <button class="btn btn-outline-secondary">Save</button>
  </form>
</template>
<script>
import {ref,onMounted} from "vue";
import axios from "axios";
import {useRouter} from "vue-router";

export default {
  name:"UsersCreate",
  setup() {
    const firstName=ref('')
    const lastName=ref('')
    const email = ref('')
    const roleId = ref(0)
    const roles = ref([])
    const router = useRouter()

    onMounted(async ()=> {
      const response = await axios.get('roles')
      roles.value = response.data.data;
    })

    const submit = async () => {
      await axios.post('users', {
        first_name:firstName.value,
        last_name:lastName.value,
        email:email.value,
        role_id:roleId.value
      })
      await router.push('/users')
    }
    return {
      firstName,
      lastName,
      email,
      roleId,
      roles,
      submit
    }
  }
}
</script>