<template>
  <div style="height:500px">
     <v-chart :options="polar"/>
  </div>
</template>

<script>
export default {
  name: 'barChart',
  data () {
    return {
      polar: {
        title: {
            text: '会员数据统计',
            subtext: '动态数据',
            x: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
            show: true,
            orient: 'vertical',
            left: 'left',
            data: ['微信访问', '公众号访问', '扫码进入', '分享进入', '搜索访问']
        },
        series: [
            {
                name: '访问来源',
                type: 'pie',
                radius: '55%',
                center: ['50%', '60%'],
                data: [
                    { value: 335, name: '微信访问' },
                    { value: 310, name: '公众号访问' },
                    { value: 234, name: '扫码进入' },
                    { value: 135, name: '分享进入' },
                    { value: 1548, name: '搜索访问' }
                ],
                itemStyle: {
                    emphasis: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
         ]
       }
    }
  },
  mounted () {
  },
  methods: {}
}
</script>
<style>
.echarts {
  width: 100%;
  height: 100%;
}
</style>
