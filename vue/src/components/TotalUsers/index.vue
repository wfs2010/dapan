<template>
  <common-card title="累计评价数" value='1,087,503'>
    <template>
    <!-- <div id="total-users-chart" :style="{width: '100%', height: '100%'}"></div> -->
    <v-chart :options="getOptions()"></v-chart>
  </template>
  <template v-slot:footer>
    <div class='total-users-chart'>
        <span>日同比 </span>
      <span class="emphasis">8.73%</span>
      <div class="increase" />
      <span class='month'>月同比 </span>
      <span class="emphasis">35.91%</span>
        <div class="decrease" />
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
        color: ['#e4393c'],
        xAxis: {
          show: false
        },
        yAxis: {
          // data: [1, 2, 3, 4, 5],
          type: 'category',
          show: false
        },
        series: [{
          // data: [20, 34, 50, 59, 20],
          data: [40],
          type: 'bar',
          barWidth: '40%',
          stack: '总量',
          itemStyle: {
            color: '#45c946'
          }
        }, {
          // data: [100, 100, 100, 100, 100],
          data: [100],
          type: 'bar',
          stack: '总量',
          itemStyle: {
            color: '#eee'
          }
        }, {
          type: 'custom',
          // data: [20, 34, 50, 59, 20],
          data: [40],
          stack: '总量',
          renderItem: (params, api) => {
            // 获取第一号元素
            const value = api.value(0)
            const endPoint = api.coord([value, 0])
            return {
              // type: 'path',
              type: 'group',
              children: [{
                type: 'path',
                position: endPoint,
                shape: {
                d: 'M512 682.666667l298.666667-298.666667H213.333333z',
                x: -5,
                y: -20,
                width: 10,
                height: 10
                },
                style: {
                  fill: 'red'
              }
              }, {
                type: 'path',
                position: endPoint,
                shape: {
                d: 'M512 341.333333l-298.666667 298.666667h597.333334zZ',
                x: -5,
                y: 10,
                width: 10,
                height: 10
                },
                style: {
                  fill: 'red'
              }
              }]
            }
          }
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
      // const chartDOM = document.getElementById('total-users-chart')
      // const chart = this.$echarts.init(chartDOM)
      // chart.setOption({
      //   color: ['#e4393c'],
      //   xAxis: {
      //     show: false
      //   },
      //   yAxis: {
      //     // data: [1, 2, 3, 4, 5],
      //     type: 'category',
      //     show: false
      //   },
      //   series: [{
      //     // data: [20, 34, 50, 59, 20],
      //     data: [40],
      //     type: 'bar',
      //     barWidth: '40%',
      //     stack: '总量',
      //     itemStyle: {
      //       color: '#45c946'
      //     }
      //   }, {
      //     // data: [100, 100, 100, 100, 100],
      //     data: [100],
      //     type: 'bar',
      //     stack: '总量',
      //     itemStyle: {
      //       color: '#eee'
      //     }
      //   }, {
      //     type: 'custom',
      //     // data: [20, 34, 50, 59, 20],
      //     data: [40],
      //     stack: '总量',
      //     renderItem: (params, api) => {
      //       // 获取第一号元素
      //       const value = api.value(0)
      //       const endPoint = api.coord([value, 0])
      //       return {
      //         // type: 'path',
      //         type: 'group',
      //         children: [{
      //           type: 'path',
      //           position: endPoint,
      //           shape: {
      //           d: 'M512 682.666667l298.666667-298.666667H213.333333z',
      //           x: -5,
      //           y: -20,
      //           width: 10,
      //           height: 10
      //           },
      //           style: {
      //             fill: 'red'
      //         }
      //         }, {
      //           type: 'path',
      //           position: endPoint,
      //           shape: {
      //           d: 'M512 341.333333l-298.666667 298.666667h597.333334zZ',
      //           x: -5,
      //           y: 10,
      //           width: 10,
      //           height: 10
      //           },
      //           style: {
      //             fill: 'red'
      //         }
      //         }]
      //       }
      //     }
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

<style lang="scss">
 .total-users-chart {
   display: flex;
   align-items: center;
 }

 .month {
   margin-left: 10px;
 }
</style>
