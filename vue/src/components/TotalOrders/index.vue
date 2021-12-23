<template>
  <common-card title="累计订单量"
  value="2,134,1234">
  <template>
    <v-chart :options="getOptions()" />
    <!-- <div id="total-orders-chart" :style="{width: '100%', height: '100%'}"></div> -->
  </template>
  <template v-slot:footer>
    <div>
      <span>昨日订单量</span>
    <span class="emphasis">2000,000</span>
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
        xAxis: {
          type: 'category',
          show: false,
          boundaryGap: false
        },
        yAxis: {
          show: false
        },
        series: [{
          type: 'line',
          data: [620, 432, 220, 534, 790, 430, 220, 320, 532, 320, 834, 690, 530, 220, 620],
          areaStyle: {
            color: 'blue'
          },
          lineStyle: {
            width: 0
          },
          itemStyle: {
            opacity: 0
          },
          smooth: true
        }],
        grid: {
          top: 0,
          bottom: 0,
          left: 0,
          right: 0
        }
      }
      }
    },
    mounted () {
      // const chartDom = document.getElementById('total-orders-chart')
      // const chart = this.$echarts.init(chartDom)
      // chart.setOption({
    //     xAxis: {
    //       type: 'category',
    //       show: false,
    //       boundaryGap: false
    //     },
    //     yAxis: {
    //       show: false
    //     },
    //     series: [{
    //       type: 'line',
    //       data: [620, 432, 220, 534, 790, 430, 220, 320, 532, 320, 834, 690, 530, 220, 620],
    //       areaStyle: {
    //         color: 'blue'
    //       },
    //       lineStyle: {
    //         width: 0
    //       },
    //       itemStyle: {
    //         opacity: 0
    //       },
    //       smooth: true
    //     }],
    //     grid: {
    //       top: 0,
    //       bottom: 0,
    //       left: 0,
    //       right: 0
    //     }
    //   })
    }
}
</script>

<style>

</style>
