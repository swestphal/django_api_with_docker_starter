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
      <div class="input-group-append">
        <input type="text" class="form-control" name="image" id="image"  v-model="image"/>
        <label class="btn btn-primary">
          Upload <input type="file" @change="change($event.target.files)" hidden/>
        </label>
      </div>
     </div>
    <div class="form-group">
      <label for="price">Price</label>
      <input type="text" class="form-control" name="price" id="price"  v-model="price">
    </div>
    <button class="btn btn-outline-secondary">Save</button>
  </form>
</template>
<script lang="ts">
import axios from "axios";
import {ref} from "vue";
import {useRouter} from "vue-router";

export default {
  name:'ProductsCreate',
  setup() {
    const title=ref("")
    const description=ref("")
    const image=ref("")
    const price=ref("")
    const router = useRouter()

    const change = async (files: FileList) => {
      const file = files.item(0);
      const data = new FormData;
      data.append('image',file);

      const response = await axios.post('upload',data)
      image.value = response.data.url;
    }
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
      submit,
      change
    }
  }
}
</script>