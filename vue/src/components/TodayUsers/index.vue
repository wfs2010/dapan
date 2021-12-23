<template>
  <common-card title="今日交易用户数" value='81,014'>
    <template>
    <!-- <div id="today-users-chart" :style="{width: '100%', height: '100%'}"></div> -->
    <v-chart :options='getOptions()'></v-chart>
  </template>
   <template v-slot:footer>
    <div>
      <span>退货率 </span>
    <span class="emphasis">5.14%</span>
    </div>
  </template>
  </common-card>
</template>

<script>
import CommonCartMixin from '../../mixins/CommonCartMixin'

export default {
    mixins: [CommonCartMixin],
    methods: {
      getOptions () {
        return {
        color: ['#3398DB'],
        xAxis: {
          type: 'category',
          data: ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00'],
          show: false
        },
        yAxis: {
          show: false
        },
        series: [{
          data: [410, 82, 200, 334, 390, 330, 220, 150, 82, 200, 134, 290, 330, 150],
          type: 'bar',
          barWidth: '60%'
        }],
        grid: {
          top: 0,
          left: 0,
          bottom: 9,
          right: 0
        }
      }
      }
    },
    mounted () {
      // const chartDom = document.getElementById('today-users-chart')
      // const chart = this.$echarts.init(chartDom)
      // chart.setOption({
      //   color: ['#3398DB'],
      //   xAxis: {
      //     type: 'category',
      //     data: ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00'],
      //     show: false
      //   },
      //   yAxis: {
      //     show: false
      //   },
      //   series: [{
      //     data: [410, 82, 200, 334, 390, 330, 220, 150, 82, 200, 134, 290, 330, 150],
      //     type: 'bar',
      //     barWidth: '60%'
      //   }],
      //   grid: {
      //     top: 0,
      //     left: 0,
      //     bottom: 9,
      //     right: 0
      //   }
      // })
    }
}
</script>

<style>

</style>
