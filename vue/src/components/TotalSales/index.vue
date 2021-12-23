<template>
  <common-card
    title="累计销售额"
    value="￥ 32,039,165"
  >
  <template>
    <div class="compare-wrapper">
      <div class="compare">
      <span>日同比</span>
      <span class="emphasis">7.33%</span>
      <div class="increase"></div>
    </div>
    <div class="compare">
      <span>月同比</span>
      <span class="emphasis">7.33%</span>
      <div class="decrease"></div>
    </div>
    </div>
  </template>
  <template v-slot:footer>
    <div>
      <span>昨日销售额</span>
    <span class="emphasis">$ 30,000,000</span>
    </div>
  </template>
  </common-card>
</template>

<script>
import CommonCartMixin from '../../mixins/CommonCartMixin'
import CommonDataMixin from '../../mixins/CommonDataMixin'

export default {
    mixins: [CommonCartMixin, CommonDataMixin]
}
</script>

<style lang="scss" scoped>
  .compare-wrapper {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
      .compare {
      display: flex;
      align-items: center;
      margin-top: 3px;
      font-size: 12px;
      color: #666;
    }
  }

  span {
    font-size: 12px;
  }

</style>
