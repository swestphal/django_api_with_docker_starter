<template>
  <div class="table-responsive">
    <table class="table table-striped table-sm">
      <thead>
        <tr>
          <th>#</th>
          <th>Image</th>
          <th>Title</th>
          <th>Description</th>
          <th>Price</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.id">
          <td>{{product.id}}</td>
          <td><img :src="product.image" height="50"/></td>
          <td>{{product.title}}</td>
          <td>{{product.description}}</td>
          <td>{{product.price}}</td>
          <td>
            <div class="btn-group mr-2">
              <router-link :to="`/products/${product.id}/edit`"  class="btn btn-sm btn-outline-secondary" >Edit</router-link>
              <a href="javascript:void(0)" class="btn btn-sm btn-outline-secondary" @click="product_delete(product.id)">Delete</a>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import axios from "axios";
import {onMounted, ref} from "vue";

export default {
  name:'Products',
  setup() {
    const products=ref([])

    onMounted(async()=> {
        const response = await axios.get('products')
        products.value = response.data.data

    })

    const product_delete= ()=> {
      console.log("huhu")
    }
    return {
      products,
      product_delete
    }
  }
}
</script>