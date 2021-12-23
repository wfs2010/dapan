<template>
  <div class="bottom-view">
    <div class="view">
      <el-card shadow='hover' >
        <template v-slot:header>
          <div class="title-wrapper">
            <div class="title">二级分类商品的均价、中位数、最高价、最低价</div>
          </div>
        </template>
         <template>
          <div class="chart-wrapper">
            <!-- <div class="chart-inner">
              <div class="chart">
                <div class="chart-title">搜索用户数</div>
                <div class="chart-data">{{userCount | format}}</div>
                <v-chart :options="searchUserOption" />
              </div>
              <div class="chart">
                <div class="chart-title">搜索量</div>
                <div class="chart-data">{{searchCount | format}}</div>
                <v-chart :options="searchUserOption" />
              </div>
            </div> -->
            <div class="table-wrapper">
              <el-table :data="tableData">
                <el-table-column prop="name" label="二级分类" />
                <el-table-column prop="avg" label="均价" />
                <el-table-column prop="mid" label="中位数" />
                <el-table-column prop="high" label="最高价" />
                <el-table-column prop="min" label="最低价" />
              </el-table>
              <el-pagination
                layout="prev, pager, next"
                :total="total"
                :page-size="pageSize"
                background
                @current-change="onPageChange"
              />
            </div>
          </div>
        </template>
      </el-card>
    </div>
    <div class="view">
      <el-card shadow='hover'>
        <template v-slot:header>
          <div class="title-wrapper">
              <div class="title">评价star</div>
              <!-- <div class="radio-wrapper">
                <el-radio-group v-model="radioSelect" size="small">
                  <el-radio-button label="品类"></el-radio-button>
                  <el-radio-button label="商品"></el-radio-button>
                </el-radio-group>
              </div> -->
          </div>
        </template>
        <template>
          <div class="chart-wrapper">
            <v-chart :options="categoryOption"></v-chart>
          </div>
        </template>
      </el-card>
    </div>
  </div>
</template>

<script>
import commonDataMixin from '../../mixins/CommonDataMixin'

const colors = ['#8d7fec', '#5085f2', '#f8726b', '#e7e702', '#78f283', '#4bc1fc']

export default {
  mixins: [commonDataMixin],
  data () {
    return {
      total: 100,
      pageSize: 5,
      tableData: [],
      totalData: [],
      searchUserOption: {
        xAxis: {
          type: 'category',
          boundaryGap: false
        },
        yAxis: {
          show: false
        },
        series: [{
          type: 'line',
          data: [100, 150, 200, 250, 200, 159, 199, 39, 199, 199],
          areaStyle: {
            color: 'rgb(95, 187, 255)'
          },
          lineStyle: {
            color: 'rgb(95, 187, 255)'
          },
          itemStyle: {
            color: 'rgba(95, 187, 255, .5)',
            opacity: 0
          },
          smooth: true
        }],
        grid: {
          top: 0,
          left: 0,
          bottom: 0,
          right: 0
        }
      },
      searchNumberOption: {},
      // tableData: [
      //   { id: 1, rank: 1, keyword: '北京\n', count: 100, users: 90, range: '90%' },
      //   { id: 1, rank: 1, keyword: '北京\n', count: 100, users: 90, range: '90%' },
      //   { id: 1, rank: 1, keyword: '北京\n', count: 100, users: 90, range: '90%' },
      //   { id: 1, rank: 1, keyword: '北京\n', count: 100, users: 90, range: '90%' }
      // ],
      radioSelect: '品类',
      categoryOption: {}
    }
  },
  computed: {
    // tableData () {
    //   return this.two
    // }
  },
  methods: {
    onPageChange (page) {
      this.renderTable(page)
    },
    renderPieChart () {
      // const mockData = [
      //   {
      //     legendname: 'norhface',
      //     value: 67,
      //     percent: '15.40%',
      //     itemStyle: {
      //       color: 'red'
      //     },
      //     name: 'aaa'
      //   },
      //   {
      //     legendname: 'n',
      //     value: 97,
      //     percent: '22.30%',
      //     itemStyle: {
      //       color: '#8d7fec'
      //     },
      //     name: 'ava'

      //   },
      //   {
      //     legendname: 'o',
      //     value: 92,
      //     percent: '21.15%',
      //     itemStyle: {
      //       color: '#5085f2'
      //     },
      //     name: 'aa'
      //   },
      //   {
      //     legendname: 'h',
      //     value: 167,
      //     percent: '15.40%',
      //     itemStyle: {
      //       color: '#e7e702'
      //     },
      //     name: 'a1a'
      //   }
      // ]
      const data = this.category1.data1.slice(0, 5)
      const axis = this.category1.axisX.slice(0, 5)
      const total = data.reduce((s, i) => s + i, 0)
      const chartData = []
        data.forEach((item, index) => {
          const percent = `${(item / total * 100).toFixed(2)}%`
          chartData.push({
            legendname: axis[index],
            value: item,
            percent,
            itemStyle: {
              color: colors[index]
            },
            name: `${axis[index]} | ${percent}`
          })
        })
      this.categoryOption = {
        title: [{
          text: '评价分布',
          textStyle: {
            fontsize: 14,
            color: '#666'
          },
          left: 20,
          top: 20
        }, {
          text: '累计评价',
          subtext: total,
          x: '34.5%',
          y: '42.5%',
          textStyle: {
            fontsize: 14,
            color: '#999'
          },
          subtextStyle: {
            fontsize: 28,
            color: '#333'
          },
          textAlign: 'center'
        }],
        series: [{
          name: '品类分布',
          type: 'pie',
          data: chartData,
          label: {
            normal: {
              show: true,
              position: 'outter',
              formatter: function (params) {
                return params.data.legendname
              }
            }
          },
          center: ['35%', '50%'],
          radius: ['40%', '60%'],
          labelline: {
            normal: {
              length: 5,
              length2: 5,
              smooth: true
            }
          },
          clocksize: true,
          itemStyle: {
            borderWidth: 4,
            borderColor: '#fff'
          }
        }],
        legend: {
          type: 'scroll',
          orient: 'vertical',
          height: 250,
          left: '70%',
          top: 'middle',
          textStyle: {
            color: '#8c8c8c'
          }
        },
        tooltip: {
            trigger: 'item',
            formatter: function (params) {
              return params.seriesName + '<br />' + params.marker + params.data.legendname + '<br/>' +
              '数量:' + params.data.value + '<br />' + '占比:' + params.data.percent
            }
          }
      }
    },
    renderTable (page) {
        this.tableData = this.totalData.slice(
          (page - 1) * this.pageSize,
          (page - 1) * this.pageSize + this.pageSize
        )
      }
  },
  mounted () {
        // this.renderPieChart()
  },
  watch: {
    two () {
      const totalData = []
        this.two.forEach((item, index) => {
          totalData.push({
            id: index + 1,
            name: item.name,
            avg: item.avg,
            mid: item.mid,
            high: item.high,
            min: item.min
          })
        })
        this.totalData = totalData
        console.log(this.totalData.length)
        this.total = this.totalData.length
        this.renderTable(1)
    },
    category1 () {
      this.renderPieChart()
    }
  }
}
</script>
<style lang="scss" scoped>
  .bottom-view {
    display: flex;
    margin-top: 20px;

    .view {
      flex: 1;
      width: 50%;
      box-sizing: border-box;

      &:first-child {
        padding: 0 10px 0 0;
      }

      &:last-child {
        padding: 0 0 0 10px;
      }

      .title-wrapper {
        display: flex;
        align-items: center;
        height: 60px;
        box-sizing: border-box;
        border-bottom: 1px solid #eee;
        font-size: 14px;
        font-weight: 500;
        padding: 0 0 0 20px;

        .radio-wrapper {
          flex: 1;
          display: flex;
          justify-content: flex-end;
          padding-right: 20px;
        }
      }

      .chart-wrapper {
        display: flex;
        flex-direction: column;
        height: 392px;

        .chart-inner {
          display: flex;
          padding: 0 10px;
          margin-top: 20px;

          .chart {
            flex: 1;
            padding: 0 10px;

            .chart-title {
              color: #999;
              font-size: 14px;
            }

            .chart-data {
              font-size: 22px;
              color: #333;
              font-weight: 500;
              letter-spacing: 2px;
            }

            .echarts {
              height: 50px;
            }
          }
        }

        .table-wrapper {
          flex: 1;
          margin-top: 20px;
          padding: 0 20px 20px 0;

          .el-pagination {
            display: flex;
            justify-content: flex-end;
            margin-top: 15px;
          }
        }
      }
    }
  }
</style>
