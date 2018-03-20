<template>
  <section class="hello">
    <h1>{{ msg }}</h1>
    <h2>Um site Qualquer</h2>
    <div class="site">
      <form action = "http://127.0.0.1:5000/receita/<bolodecoco>" >
        <input placeholder="Digite o nome da receita:"></input>
        <button>Enviar</button>
      </form>
      <div class="img">
        <img src="../assets/e.png">
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Aprendendo a juntar o Flask no Vue'
    }
  }
}
</script>


<style scoped>
h1, h2 {
  font-weight: normal;
  color: #3299CC;
}
.site{
  background-color: rgba(60, 142, 169, 0.32);
}
input{
  margin: 6px;
}

button{
/*border: none;*/
}

img{
  width: 4vw;
  margin: 18px;
}

a {
  color: #42b983;
}
</style>
