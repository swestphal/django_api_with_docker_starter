<template>
<h2>Section title</h2>
      <div class="table-responsive">
        <table class="table table-striped table-sm">
          <thead>
            <tr>
              <th>#</th>
              <th>Name</th>
              <th>Email</th>
              <th>Role</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in users" :key="user.id">
              <td>{{user.id}}</td>
              <td>{{user.first_name }} {{user.last_name}}</td>
              <td>{{user.email}}</td>
              <td>{{user.role.name}}</td>
              <td>
                <div class="btn-group mr-2">
                  <a href="javascript:void(0)" class="btn btn-sm btn-outline-secondary" @click="user_edit(user.id)">Edit</a>
                  <a href="javascript:void(0)" class="btn btn-sm btn-outline-secondary" @click="user_delete(user.id)">Delete</a>
                </div>
              </td>
            </tr>

          </tbody>
        </table>
      </div>
  <nav>
    <ul class="pagination">
      <li class="page-item">
        <a class="page-link" href="javascript:void(0)" @click="prev">Previous</a>
      </li>
      <li class="page-item">
        <a class="page-link" href="javascript:void(0)" @click="next">Next</a>
      </li>
    </ul>
  </nav>
</template>

<script lang="ts">
import {ref, onMounted} from "vue";
import axios from "axios";
import {User} from "@/classes/class";
import {Entity} from "@/interfaces/Entity";


export default {
  name: "Users",
  setup() {
    const users = ref([])
    const page = ref(1)
    const lastPage = ref(0)

    const load = async ()=> {
      const response = await axios.get(`users?page=${page.value}`)
      users.value = response.data.data
      lastPage.value = response.data.data.last_page
    }
    onMounted(load)

    const next = async () => {
      if(page.value === lastPage.value) return
      page.value++;
      await load();
    }

    const prev = async () =>{
      if (page.value === 1) return
      page.value--;
      await load();
    }

    const user_edit = (id) => {
      console.log("-")
    }

    const user_delete = async (id:number) => {
      if(confirm('Are you sure?')) {
        const response = await axios.delete(`users/${id}`)
        //users.value = users.value.filter((u: {id:number}) => u.id !== id)
        //users.value = users.value.filter((u: User) => u.id !== id) -> classes
        users.value = users.value.filter((u: Entity) => u.id !== id) // -> interface
      }
    }
    return {
      next,
      prev,
      user_edit,
      user_delete,
      users
    }
  }
}
</script>

