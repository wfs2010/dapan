<template>
  <div class="home">
    <div class="search">
      <el-input v-model="message" placeholder="请输入内容"></el-input>
    <el-select v-model="value" placeholder="请选择">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
    <el-button icon="el-icon-search" v-on:click="search" circle></el-button>
</div>
    <top-view></top-view>
    <sales-view></sales-view>
    <bottom-view></bottom-view>
    <map-view></map-view>
  </div>
</template>

<script>
// @ is an alias to /src
import TopView from '@/components/TopView'
import BottomView from '@/components/BottomView'
import MapView from '@/components/MapView'
import SalesView from '@/components/SalesView'
import { wordCloud } from '@/api'

export default {
  name: 'Home',
  components: {
    TopView,
    BottomView,
    MapView,
    SalesView
  },
  methods: {
    search: function (event) {
      wordCloud(this.message).then(data => { this.reportData = data })
    },
    getReportData () {
      return this.reportData
    }
  },
  data () {
    return {
      message: '10024990444664',
      reportData: null,
      wordCloud: null,
      mapData: null,
      options: [{
          value: '选项1',
          label: '本地生活/旅游出行'
        }, {
          value: '选项2',
          label: '宠物生活'
        }, {
          value: '选项3',
          label: '厨具'
        }, {
          value: '选项4',
          label: '电脑、办公'
        }, {
          value: '选项5',
          label: '二手商品'
        }, {
          value: '选项2',
          label: '服饰内衣'
        }, {
          value: '选项3',
          label: '个人护理'
        }, {
          value: '选项4',
          label: '家纺'
        }, {
          value: '选项5',
          label: '家居日用'
        }, {
          value: '选项1',
          label: '家具'
        }, {
          value: '选项2',
          label: '家庭清洁'
        }, {
          value: '选项3',
          label: '家用电器'
        }, {
          value: '选项4',
          label: '家装建材'
        }, {
          value: '选项5',
          label: '礼品'
        }, {
          value: '选项2',
          label: '美妆护肤'
        }, {
          value: '选项3',
          label: '母婴'
        }, {
          value: '选项4',
          label: '汽车用品'
        }, {
          value: '选项5',
          label: '生鲜'
        }, {
          value: '选项3',
          label: '食品饮料'
        }, {
          value: '选项4',
          label: '手机通讯'
        }, {
          value: '选项5',
          label: '数码'
        }, {
          value: '选项2',
          label: '图书'
        }, {
          value: '选项3',
          label: '箱包皮具'
        }, {
          value: '选项4',
          label: '鞋靴'
        }, {
          value: '选项5',
          label: '运动户外'
        }, {
          value: '选项5',
          label: '珠宝首饰'
        }],
        value: '手机通讯'
    }
  },
  provide () {
    return {
      getReportData: this.getReportData
    }
  },
  mounted () {
    wordCloud().then(data => { this.reportData = data })
    // test().catch(err => alert(err.message))
  }
}
</script>

<style>
  .search {
    display: flex;
    width: 20%;
    padding: 0;
    margin: 0;
  }
  .home {
    width: 100%;
    height: 100%;
    padding: 20px;
    background: #eee;
    box-sizing: border-box;
  }
</style>
