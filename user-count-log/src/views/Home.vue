<template>
  <div class="input-field">
    <input
      @keyup="typingLog"
      @blur="countStart"
      @keyup.enter="$refs.input.blur"
      v-model.lazy="text"
      ref="input"
      id="text"
      type="text"
    >
    <label for="text">Type here</label>
  </div>
</template>

<script>
export default {
  name: 'StartPage',
  data() {
    return {
      text: '',
      timeStamp: 0,
      arrMarkTime: [],
      requestLog: [],
      requestInterval: null,
    }
  },
  mounted() {
    this.countStart()
  },
  methods: {
    countStart() {
      if (this.arrMarkTime.length)
        this.sendRequest()

      if (this.requestInterval)
        clearInterval(this.requestInterval)

      this.$refs.input.addEventListener('keydown', () => {
        this.timeStamp = +new Date
        this.requestInterval = setInterval(this.sendRequest, 60000)
      }, {once: true})
    },
    typingLog() {
      const countedTime = `${new Date(new Date - this.timeStamp).getSeconds()}:${new Date(new Date - this.timeStamp).getMilliseconds()}`
      this.arrMarkTime.push(countedTime)
    },
    async sendRequest() {
      const userTypeLog = JSON.stringify(this.arrMarkTime)

      this.arrMarkTime = []
      this.timeStamp = +new Date

      const request = await fetch('/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: userTypeLog,
      })
      this.requestLog.push(request)
    },
  },
}
</script>

<style lang="scss" scoped>
  .input-field {
    margin-top: 12rem;
    width: 100%;
  }
</style>