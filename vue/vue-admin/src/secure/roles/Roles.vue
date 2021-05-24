<template>
<h2>Section title</h2>
      <div class="table-responsive">
        <table class="table table-striped table-sm">
          <thead>
            <tr>
              <th>#</th>
              <th>Name</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="role in roles" :key="role.id">
              <td>{{role.id}}</td>
              <td>{{role.name}}</td>

              <td>
                <div class="btn-group mr-2">
                  <router-link :to="`/roles/${role.id}/edit`" class="btn btn-sm btn-outline-secondary" >Edit</router-link>
                  <a href="javascript:void(0)" class="btn btn-sm btn-outline-secondary" @click="role_delete(role.id)">Delete</a>
                </div>
              </td>
            </tr>

          </tbody>
        </table>
      </div>
</template>

<script lang="ts">
import {onMounted, ref} from "vue";
import axios from "axios";
import {Entity} from "@/interfaces/Entity";

export default {
  name:'Roles',

  setup() {
    const roles = ref([])

    onMounted(async()=>{
      const response = await axios.get('roles')
      roles.value = response.data.data
    })


      const role_delete = async (id:number) => {
      if(confirm('Are you sure?')) {
        const response = await axios.delete(`roles/${id}`)
        roles.value = roles.value.filter((r: Entity) => r.id !== id) // -> interface
      }
    }
    return {
      roles,
      role_delete
    }
  }
}
</script>