<template>
  <div>
    <div class="title">{{title}}</div>
    <div class="value">{{value}}</div>
    <div class="chart">
      <slot></slot>
    </div>
    <div class="line" />
    <div class="total">
      <slot name="footer"></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: String,
    value: String
  }
}
</script>

<style>
.title {
  font-size: 12px;
  color: #999;
}

.value {
  font-size: 25px;
  margin-top: 5px;
  color: #000;
  letter-spacing: 1px;
}

.chart {
  height: 50px;
  /* background: red; */
}

.line {
  margin: 10px 0;
  border-top: 1px solid #eee;
}

.total {
  font-size: 12px;
  color: #666;
}

.emphasis {
   margin-left: 5px;
   color: #333;
   font-weight: 700;
}

 .increase {
        height: 0;
        width: 0;
        border-width: 3px;
        border-color: transparent transparent red transparent;
        border-style: solid;
        margin: 0 0 10px 5px;
      }
  .decrease {
        height: 0;
        width: 0;
        border-width: 3px;
        border-color:  green transparent transparent transparent;
        border-style: solid;
        margin: 0 0 3px 5px;
      }
</style>
