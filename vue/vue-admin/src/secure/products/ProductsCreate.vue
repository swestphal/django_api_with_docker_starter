<template>
  <form @submit.prevent="submit">
    <div class="form-group">
      <label for="title">Title</label>
      <input type="text" class="form-control" name="title" id="title"  v-model="title">
    </div>
    <div class="form-group">
      <label for="description">Description</label>
      <input type="text" class="form-control" name="description" id="description"  v-model="description">
    </div>
     <div class="form-group">
       <label for="image">Image</label>
       <input type="text" class="form-control" name="image" id="image" placeholder="name@example.com" v-model="image">
    </div>
    <div class="form-group">
      <label for="price">Price</label>
      <input type="text" class="form-control" name="price" id="price"  v-model="price">
    </div>
    <button class="btn btn-outline-secondary">Save</button>
  </form>
</template>
<script>
import axios from "axios";
import {onMounted, ref} from "vue";
import {useRouter} from "vue-router";

export default {
  name:'ProductsCreate',
  setup() {
    const title=ref("")
    const description=ref("")
    const image=ref("")
    const price=ref("")
    const router = useRouter()


    const submit = async ()=> {
      axios.post('products',{
        title:title.value,
        description:description.value,
        image:image.value,
        price:price.value
      })
      await router.push('/products')
    }
    return {
      title,
      description,
      image,
      price,
      submit
    }
  }
}
</script>