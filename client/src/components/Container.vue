<template>
  <div class="row">
    <div class="col-lg-6"></div>
      <div class="col-lg-6">

      </div>
      {{blogs}}
  </div>
</template>

<script>
export default {
  name: 'Container',
  props: {
    msg: String
  },
  data(){
    return{
      blogs:null,
      url:'',
      title:'',
      body:''
    }
  },
  mounted() {
    this.getAll();
  },
  methods: {
    getAll(){
      // eslint-disable-next-line no-undef
      axios
      .get(`https://localhost:8000`)
      .then((res)=>{
        this.blogs:res.data
      })
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
